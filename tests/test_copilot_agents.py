import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AGENT_DIR = ROOT / ".github" / "agents"

EXPECTED = {
    "renomedy-research.agent.md": ("Renomedy Research", "agents/01-research-agent.md"),
    "renomedy-strategy.agent.md": ("Renomedy Content Strategist", "agents/02-strategy-agent.md"),
    "renomedy-drafter.agent.md": ("Renomedy Content Drafter", "agents/03-draft-agent.md"),
    "renomedy-reviewer.agent.md": ("Renomedy Safety and Brand Review", "agents/04-review-agent.md"),
    "renomedy-learning.agent.md": ("Renomedy Performance Learning", "agents/05-learning-agent.md"),
}


class CopilotAgentDefinitionTests(unittest.TestCase):
    def test_exactly_five_expected_agent_definitions_exist(self):
        actual = {p.name for p in AGENT_DIR.glob("*.agent.md")}
        self.assertEqual(actual, set(EXPECTED))

    def test_each_agent_has_frontmatter_name_description_and_role_reference(self):
        for filename, (expected_name, role_path) in EXPECTED.items():
            with self.subTest(agent=filename):
                content = (AGENT_DIR / filename).read_text(encoding="utf-8")
                match = re.match(r"^---\n(.*?)\n---\n", content, flags=re.DOTALL)
                self.assertIsNotNone(match, "Missing YAML frontmatter")
                frontmatter = match.group(1)
                self.assertRegex(frontmatter, r"(?m)^name:\s*.+$")
                self.assertRegex(frontmatter, r"(?m)^description:\s*.+$")
                self.assertIn(f"name: {expected_name}", frontmatter)
                self.assertTrue((ROOT / role_path).is_file(), f"Missing canonical role spec: {role_path}")
                self.assertIn(role_path, content)
                self.assertIn("config/brand-guardrails.json", content)
                self.assertIn("strategy/brand-voice.md", content)

    def test_reviewer_has_independent_fail_closed_verdicts(self):
        content = (AGENT_DIR / "renomedy-reviewer.agent.md").read_text(encoding="utf-8")
        for verdict in ("PASS", "NEEDS_EDITS", "BLOCK"):
            self.assertIn(verdict, content)
        self.assertIn("fail closed", content.lower())
        self.assertIn("human approval", content.lower())
        self.assertIn("Never mark", content)

    def test_agents_preserve_human_approval_and_manual_publishing(self):
        for filename in EXPECTED:
            with self.subTest(agent=filename):
                content = (AGENT_DIR / filename).read_text(encoding="utf-8").lower()
                self.assertTrue("human" in content)
        guardrails = (ROOT / "config" / "brand-guardrails.json").read_text(encoding="utf-8")
        self.assertIn('"human_approval_required_before_publishing": true', guardrails)
        self.assertIn('"publishing_mode": "manual_until_explicitly_enabled"', guardrails)

    def test_handoff_and_manual_validation_are_documented(self):
        doc = (ROOT / "docs" / "copilot-agent-validation.md").read_text(encoding="utf-8")
        for phrase in ("Research → Strategy", "Strategy → Drafter", "Drafter → Reviewer", "Manual editor validation"):
            self.assertIn(phrase, doc)
        self.assertIn("not create automatic agent-to-agent execution", doc)


if __name__ == "__main__":
    unittest.main()
