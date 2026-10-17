# Renomedy Marketing System

An approval-first operating system for Renomedy's Instagram content and organic growth.

The system can create structured ideas, generate AI-assisted creative drafts, and run a separate first-pass AI review through an OpenAI-compatible chat API. It does not publish automatically. Human review and approval are required for every post.

## Product-truth rule
Renomedy is being explored as a family medication-intelligence product. Do not claim features are live unless the product team verifies them. This system must not provide individualized medical advice, recommend medication changes, or promise clinical outcomes.

## Quick start

Install dependencies:
    python -m pip install -r requirements.txt

Create a starter idea:
    python scripts/new_content.py --title "A family medication information checklist" --format carousel --pillar clarity --audience "Family members coordinating appointments" --takeaway "Keep an up-to-date list to review with a qualified professional." --cta "Save this checklist for your next appointment."

Configure the model API in your shell. Never commit API keys to Git:
    export RENOMEDY_LLM_API_KEY="your-api-key"
    export RENOMEDY_LLM_MODEL="your-enabled-model"
    export RENOMEDY_LLM_BASE_URL="https://api.openai.com/v1"

Generate an AI-assisted draft:
    python scripts/generate_draft.py content/sample-post.json

Run the separate AI review:
    python scripts/review_draft.py content/drafts/sample-001-ai-draft.json

The review tool writes a new record under content/reviewed/. A PASS moves the record only to awaiting_human_approval. NEEDS_EDITS and BLOCK map to their matching workflow states. The original draft is not overwritten. The API key and model name are required; otherwise scripts exit without making an API call.

Validate content records and run tests:
    python scripts/validate_content.py content/
    PYTHONPATH=scripts python -m unittest discover -s tests -v

## Workflow
1. Research audience questions and retain sources/date/confidence.
2. Turn supported insights into a brief.
3. Generate a format-specific creative draft.
4. Run first-pass AI review, then human review of claims, product truth, privacy, tone, and source quality.
5. Obtain explicit human approval before manual publishing.
6. Log the published URL and performance at consistent intervals.

## Safety boundaries
- Never ask people to share personal health details publicly.
- Never advise an individual to start, stop, skip, combine, or change medication.
- Never invent medical sources, statistics, product capabilities, endorsements, or clinical outcomes.
- AI review is a linting aid, not medical, legal, privacy, or regulatory clearance.
- PASS never means approved or safe to publish. Human review is always required.
- No Instagram publishing integration or analytics integration is included.

## Repository structure
- strategy/ — positioning, voice and growth plan
- agents/ — role prompts and orchestration contract
- content/ — calendar, briefs, schema and draft records
- config/ — brand and safety guardrails
- ops/ — approval and measurement workflows
- scripts/ — idea creation, AI drafting, review and validation
- tests/ — regression tests
