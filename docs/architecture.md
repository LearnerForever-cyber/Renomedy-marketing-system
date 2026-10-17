# Architecture and implementation roadmap

## v0.1 — repository foundation
- Agent role prompts and workflow contract
- Instagram content strategy and starter calendar
- Brand/healthcare guardrails
- Human approval checklist
- Metrics CSV
- JSON content validator
- GitHub Actions workflow to run the validator on relevant changes

## v0.2 — structured content operations
Recommended next implementation:
- Define and enforce a JSON Schema for post records.
- Add content status and owner fields consistently.
- Add a small CLI to create a new post brief from a template.
- Add unit tests for validator blocking/warning behavior.
- Add a human-readable weekly report from the metrics CSV.

## v0.3 — model orchestration
Before wiring a model provider:
- Select provider and model.
- Store API keys in repository Actions secrets or an appropriate secret manager; never commit them.
- Use structured outputs for research notes, briefs, drafts and review decisions.
- Keep research citations and source dates attached to claims.
- Log prompt/config versions and agent outputs.
- Make the reviewer an independent stage, not just a self-review in the drafting prompt.

## v0.4 — integrations
- Add research connectors with terms/access checks.
- Add analytics import after confirming Instagram account access and permissions.
- Consider scheduling/publishing only after platform requirements and human approval controls are clear.

## Non-goals until explicitly approved
- Autonomous publishing
- Individualized medical advice
- Sensitive-health profiling or ad targeting
- Unverified claims about clinical outcomes, privacy, security or regulatory compliance

## Definition of done for the first usable workflow
A team member can turn an insight into a draft, see all claims and sources, run validation, obtain a human review, approve the post, publish manually, and record results without losing the audit trail.
