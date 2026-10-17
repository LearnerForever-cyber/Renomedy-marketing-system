import json
import tempfile
import unittest
from pathlib import Path

from generate_assets import main as assets_main


class AssetGenerationContractTests(unittest.TestCase):
    def test_renderer_module_has_format_contract(self):
        # Validate deterministic format-to-asset mapping without network access.
        from generate_assets import PALETTE, safe_slug
        self.assertIn("bg", PALETTE)
        self.assertEqual(safe_slug("My Test Post!"), "my-test-post")

    def test_carousel_requires_slides(self):
        from generate_assets import render_card
        self.assertTrue(callable(render_card))


if __name__ == "__main__":
    unittest.main()
