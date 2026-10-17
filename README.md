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
- `content/` — starter calendar and reusable brief
- `ops/` — approval checklist, metrics and weekly workflow
- `config/` — brand and safety guardrails
- `scripts/` — content-record validation

## Quick start
1. Read `strategy/instagram-growth-plan.md`.
2. Confirm `config/brand-guardrails.json` against the actual product.
3. Copy `content/brief-template.md` for each post.
4. Review claims and get human approval before publishing.
5. Log metrics in `ops/instagram-metrics.csv`.
6. Run `python scripts/validate_content.py content/sample-post.json`.

## Not included yet
No model-provider wiring, automated research ingestion, Instagram API publishing, analytics integrations, or verified compliance/security claims. Add these only after selecting providers, access scopes and approval controls.
