"""Unit tests for Renomedy's content validation and draft scaffolding."""
import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from jsonschema import Draft202012Validator
from new_content import create_record, slugify
from validate_content import SCHEMA_PATH, validate_record


class ContentValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(cls.schema)
        cls.valid_record = {
            "id": "test-001",
            "status": "drafted",
            "format": "carousel",
            "pillar": "clarity",
            "working_title": "A practical checklist",
            "audience_hypothesis": "Family coordinators",
            "takeaway": "Keep a current list to review with a qualified professional.",
            "cta": "Save this checklist.",
            "claims": [],
            "product_features_mentioned": [],
            "asks_for_public_health_details": False,
            "human_approved": False
        }

    def test_valid_draft_passes_schema(self):
        errors, _ = validate_record(self.valid_record, self.schema)
        self.assertEqual(errors, [])

    def test_unknown_status_fails_schema(self):
        record = {**self.valid_record, "status": "draft"}
        errors, _ = validate_record(record, self.schema)
        self.assertTrue(any("status" in error for error in errors))

    def test_public_health_details_request_is_blocked(self):
        record = {**self.valid_record, "asks_for_public_health_details": True}
        errors, _ = validate_record(record, self.schema)
        self.assertTrue(any("personal health details" in error for error in errors))

    def test_approved_status_requires_human_approval(self):
        record = {**self.valid_record, "status": "approved", "human_approved": False}
        errors, _ = validate_record(record, self.schema)
        self.assertTrue(any("requires human_approved=true" in error for error in errors))

    def test_published_status_requires_url(self):
        record = {**self.valid_record, "status": "published", "human_approved": True}
        errors, _ = validate_record(record, self.schema)
        self.assertTrue(any("published_url" in error for error in errors))

    def test_unverified_claim_generates_warning(self):
        record = {
            **self.valid_record,
            "claims": [{"text": "Example claim", "source_url": "", "verified": False, "review_required": True}]
        }
        errors, warnings = validate_record(record, self.schema)
        self.assertEqual(errors, [])
        self.assertTrue(any("not verified" in warning for warning in warnings))
        self.assertTrue(any("qualified human review" in warning for warning in warnings))


class DraftScaffoldingTests(unittest.TestCase):
    def test_slugify_title(self):
        self.assertEqual(slugify("Family Medication Checklist!"), "family-medication-checklist")

    def test_created_record_matches_schema_and_stays_unapproved(self):
        record = create_record(
            "Family checklist", "carousel", "clarity", "Family coordinators",
            "Keep a list to review with a qualified professional.", "Save this post."
        )
        errors, _ = validate_record(record, ContentValidationTests.schema)
        self.assertEqual(errors, [])
        self.assertEqual(record["status"], "idea")
        self.assertFalse(record["human_approved"])

    def test_invalid_format_is_rejected(self):
        with self.assertRaises(ValueError):
            create_record("Title", "thread", "clarity", "", "Takeaway", "CTA")

    def test_cli_output_directory_can_be_used(self):
        with TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "draft.json"
            record = create_record("Starter post", "story", "trust", "", "A clear takeaway", "Save this")
            output.write_text(json.dumps(record), encoding="utf-8")
            parsed = json.loads(output.read_text(encoding="utf-8"))
            errors, _ = validate_record(parsed, ContentValidationTests.schema)
            self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
