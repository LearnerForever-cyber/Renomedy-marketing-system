"""Unit tests for Renomedy's content validation guardrails."""
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

from validate_content import SCHEMA_PATH, validate_record
import json


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


if __name__ == "__main__":
    unittest.main()
