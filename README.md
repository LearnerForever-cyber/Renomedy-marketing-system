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

Run the full approval-first pipeline (draft → AI review → PNG assets):
    python scripts/run_content_pipeline.py content/sample-post.json

Individual stages remain available for debugging:
    python scripts/generate_draft.py content/sample-post.json

Generate actual PNG assets from a draft record (no image API required):
    python scripts/generate_assets.py content/drafts/<draft-record>.json

The asset renderer writes PNG carousel slides, Story frames, or feed/Reel cover graphics plus an asset-manifest.json under content/assets/<content-id>/. Reel covers and scripts are not finished video files; Reel records remain incomplete until an MP4 is supplied and checked.

Run the separate AI review:
    python scripts/review_draft.py content/drafts/sample-001-ai-draft.json

The review tool writes a new record under content/reviewed/. A PASS moves the record only to awaiting_human_approval. NEEDS_EDITS and BLOCK map to their matching workflow states. The original draft is not overwritten. The API key and model name are required; otherwise scripts exit without making an API call.

Validate content records and run tests:
    python scripts/validate_content.py content/
    PYTHONPATH=scripts python -m unittest discover -s tests -v

## Ready-to-post launch batch

The first 11-post Instagram batch is prepared. See [launch batch and asset inventory](content/launch-batch-01.md) and [launch-readiness checklist](ops/launch-readiness.md). The conversation deliverable `renomedy-instagram-launch-pack.zip` contains 25 PNG graphics (3 carousels, 3 static posts, 4 Story frames, 3 Reel covers), 11 captions, hashtags, alt-text guidance, 3 Reel scripts, and a posting guide. Story polls still need native Instagram stickers; Reel videos still need recording/editing. The graphics use provisional colors and a placeholder mascot mark, so confirm brand approval before posting.

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


## GitHub Copilot marketing agents

Five repository custom-agent definitions live in `.github/agents/`: Research, Content Strategist, Content Drafter, Safety and Brand Review, and Performance Learning. Each definition is grounded in the canonical role prompts in `agents/` and the repository's brand, product-truth, privacy, and healthcare guardrails.

See [Copilot agent setup and validation](docs/copilot-agent-validation.md) for the handoff contract, static checks, and manual editor smoke tests. These definitions make the roles available as custom agents in a compatible Copilot client; they do not by themselves implement autonomous agent-to-agent orchestration. Human approval and manual publishing remain mandatory.
