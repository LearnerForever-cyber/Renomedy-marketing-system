"""Unit tests for content validation, draft helpers and review-state mapping."""
import json
import unittest

from jsonschema import Draft202012Validator
from new_content import create_record, slugify
from generate_draft import build_user_prompt, parse_model_json
from review_draft import apply_review, parse_review
from validate_content import SCHEMA_PATH, validate_record


class ContentValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(cls.schema)
        cls.valid_record = {
            "id": "test-001", "status": "drafted", "format": "carousel",
            "pillar": "clarity", "working_title": "A practical checklist",
            "audience_hypothesis": "Family coordinators",
            "takeaway": "Keep a current list to review with a qualified professional.",
            "cta": "Save this checklist.", "claims": [],
            "product_features_mentioned": [], "asks_for_public_health_details": False,
            "human_approved": False
        }

    def test_valid_draft_passes_schema(self):
        errors, _ = validate_record(self.valid_record, self.schema)
        self.assertEqual(errors, [])

    def test_unknown_status_fails_schema(self):
        errors, _ = validate_record({**self.valid_record, "status": "draft"}, self.schema)
        self.assertTrue(any("status" in error for error in errors))

    def test_public_health_details_request_is_blocked(self):
        errors, _ = validate_record({**self.valid_record, "asks_for_public_health_details": True}, self.schema)
        self.assertTrue(any("personal health details" in error for error in errors))

    def test_approved_status_requires_human_approval(self):
        errors, _ = validate_record({**self.valid_record, "status": "approved", "human_approved": False}, self.schema)
        self.assertTrue(any("requires human_approved=true" in error for error in errors))

    def test_published_status_requires_url(self):
        errors, _ = validate_record({**self.valid_record, "status": "published", "human_approved": True}, self.schema)
        self.assertTrue(any("published_url" in error for error in errors))

    def test_unverified_claim_generates_warning(self):
        record = {**self.valid_record, "claims": [{"text": "Example", "source_url": "", "verified": False, "review_required": True}]}
        errors, warnings = validate_record(record, self.schema)
        self.assertEqual(errors, [])
        self.assertTrue(any("not verified" in warning for warning in warnings))
        self.assertTrue(any("qualified human review" in warning for warning in warnings))


class DraftScaffoldingTests(unittest.TestCase):
    def test_slugify_title(self):
        self.assertEqual(slugify("Family Medication Checklist!"), "family-medication-checklist")

    def test_created_record_matches_schema_and_stays_unapproved(self):
        record = create_record("Family checklist", "carousel", "clarity", "Family coordinators",
                               "Keep a list to review with a qualified professional.", "Save this post.")
        errors, _ = validate_record(record, ContentValidationTests.schema)
        self.assertEqual(errors, [])
        self.assertEqual(record["status"], "idea")
        self.assertFalse(record["human_approved"])

    def test_invalid_format_is_rejected(self):
        with self.assertRaises(ValueError):
            create_record("Title", "thread", "clarity", "", "Takeaway", "CTA")


class AIDraftHelperTests(unittest.TestCase):
    def test_model_json_parsing(self):
        self.assertEqual(parse_model_json('{"hook":"A simple checklist"}')["hook"], "A simple checklist")

    def test_model_json_parsing_accepts_fences(self):
        fenced = chr(96) * 3 + 'json\n{"hook":"A simple checklist"}\n' + chr(96) * 3
        self.assertEqual(parse_model_json(fenced)["hook"], "A simple checklist")

    def test_prompt_uses_brief_data(self):
        prompt = build_user_prompt({"format": "carousel", "pillar": "clarity", "working_title": "Checklist",
                                    "takeaway": "Keep a list.", "cta": "Save this."})
        self.assertIn('"format": "carousel"', prompt)
        self.assertNotIn("RENOMEDY_LLM_API_KEY", prompt)


class AIReviewTests(unittest.TestCase):
    def test_review_parser_rejects_unknown_verdict(self):
        with self.assertRaises(ValueError):
            parse_review('{"verdict":"APPROVED","summary":"ok","findings":[]}')

    def test_pass_only_moves_to_human_approval_queue(self):
        record = {**ContentValidationTests.valid_record, "human_approved": False}
        review = {"verdict": "PASS", "summary": "No obvious issue found.", "findings": []}
        output = apply_review(record, review)
        self.assertEqual(output["status"], "awaiting_human_approval")
        self.assertFalse(output["human_approved"])
        self.assertTrue(output["review_report"]["human_review_required"])

    def test_needs_edits_and_block_map_to_safe_states(self):
        record = ContentValidationTests.valid_record
        self.assertEqual(apply_review(record, {"verdict": "NEEDS_EDITS", "summary": "", "findings": []})["status"], "needs_edits")
        self.assertEqual(apply_review(record, {"verdict": "BLOCK", "summary": "", "findings": []})["status"], "blocked")

    def test_reviewed_record_matches_schema(self):
        record = {**ContentValidationTests.valid_record, "creative": {
            "hook": "Checklist", "caption": "Save this.", "body": ["Cover", "Slide 1"],
            "visual_notes": "Use simple icons.", "alt_text": "Checklist graphic",
            "reel_script": "", "story_frames": [], "cover_text": "Checklist"
        }}
        review = {"verdict": "PASS", "summary": "No obvious issue found.", "findings": []}
        output = apply_review(record, review)
        errors = list(Draft202012Validator(ContentValidationTests.schema).iter_errors(output))
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
