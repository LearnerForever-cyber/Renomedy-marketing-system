# Renomedy Marketing System

An approval-first, agent-ready operating system for Renomedy's Instagram content and organic growth.

> v0.1 is a human-operated scaffold: it drafts and organizes work, but does not autonomously publish. A human must review healthcare-related claims and approve every post.

## First-release goals
- Turn audience questions into Instagram content briefs.
- Maintain a repeatable content calendar and brand voice.
- Draft carousel, Reel, Story and caption concepts.
- Apply healthcare-safety, privacy and brand checks.
- Track organic performance and feed learning into future experiments.

## Product-truth rule
Renomedy is being explored as a family medication-intelligence product. Do not claim features are live unless the product team verifies them. This system must not provide individualized medical advice, recommend medication changes, or promise clinical outcomes.

## Structure
- `strategy/` — audience hypotheses, positioning and growth plan
- `agents/` — prompts for research, strategy, drafting, review and learning
- `content/` — starter calendar, reusable brief and JSON content records
- `ops/` — approval checklist, metrics and weekly workflow
- `config/` — brand and safety guardrails
- `scripts/` — content-record validation and draft scaffolding
- `tests/` — regression tests for validation guardrails

## Quick start
Install the validator dependency:

```bash
python -m pip install -r requirements.txt
```

Create a new content record (it starts as an unapproved idea):

```bash
python scripts/new_content.py \
  --title "A family medication information checklist" \
  --format carousel \
  --pillar clarity \
  --audience "Family members coordinating appointments" \
  --takeaway "Keep an up-to-date list to review with a qualified professional." \
  --cta "Save this checklist for your next appointment."
```

Validate every JSON record in `content/` (including drafts in subfolders):

```bash
python scripts/validate_content.py content/
```

Run the automated tests:

```bash
PYTHONPATH=scripts python -m unittest discover -s tests -v
```

## Human approval is mandatory
1. Read `strategy/instagram-growth-plan.md`.
2. Confirm `config/brand-guardrails.json` against the actual product.
3. Review every factual claim and its source; get qualified review where needed.
4. Review privacy, brand voice, and product truth.
5. Get explicit human approval before publishing.
6. Log metrics in `ops/instagram-metrics.csv`.

A passing validator means the record meets structural and hard-coded checks. It is not a medical, legal, privacy, or brand clearance and never grants publishing permission.

## Not included yet
No model-provider wiring, automated research ingestion, Instagram API publishing, analytics integrations, or verified compliance/security claims. Add these only after selecting providers, access scopes and approval controls.
