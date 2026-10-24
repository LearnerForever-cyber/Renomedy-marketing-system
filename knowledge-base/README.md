# Renomedy Brand Knowledge Base

**Version:** 0.3.0  
**Status:** Source-audited draft — owner approval still required  
**Last reviewed:** 2026-10-24

## What this is

A source-aware knowledge base for Renomedy's future marketing and AI-agent workflows. It distinguishes current public statements from internal vision, hypotheses, and unknowns. It is not proof that a feature is implemented.

The latest recorded public-site snapshot (accessed 2026-10-22, per the source register) says Renomedy is in development, not yet available, and that the screens are illustrative concepts. A fresh access attempt on 2026-10-24 failed through the available web retrieval tool, so this status has not been independently rechecked today. Do not market Renomedy as a live app unless newer evidence is recorded.

## Master structure

The knowledge base is being expanded as four blocks containing twelve stages. The numbered stage files are intended to make each topic easy for future agents to locate and review.

- [Block 1 — Core Truth](01-core-truth/README.md)
  - [Stage 1 — Company Foundation](01-core-truth/stage-01-company-foundation/README.md) — expanded draft, owner review pending.
  - [Stage 2 — Product Truth](01-core-truth/stage-02-product-truth/README.md) — expanded evidence-aware draft; owner review pending.
  - Stage 3 — Audience, Strategy & Safety — pending.
- Block 2 — Brand System — pending expansion.
  - Stage 4 — Identity System.
  - Stage 5 — Visual Design System.
  - Stage 6 — Messaging & Brand Voice.
- Block 3 — Growth System — pending expansion.
  - Stage 7 — Research & Validation.
  - Stage 8 — Marketing & Distribution.
  - Stage 9 — Measurement & Optimization.
- Block 4 — Evidence System — pending expansion.
  - Stage 10 — Sources & Fact Ledger.
  - Stage 11 — Decisions & Open Questions.
  - Stage 12 — Experiments & Continuous Learning.

## Existing reference folders

These source folders remain in place and should be maintained as the evidence and operational reference layer while the staged structure is expanded:

- `brand/` — existing brand notes and rules.
- `product/` — existing product concept and capability-status documents.
- `audience/` — audience notes and hypotheses.
- `strategy/` — positioning, strategy, and open questions.
- `safety/` — health and claim guardrails.
- `sources/` — provenance, source register, and fact ledger.
- `templates/` — reusable campaign templates.

New stage documents should link to these sources rather than copying unsupported claims or allowing two conflicting versions to drift.

## Mandatory instructions for AI agents

1. Read `sources/source-register.md`, `sources/fact-ledger.md`, and `safety/health-claims-and-guardrails.md` before generating health-related marketing content.
2. Current public product status is **in development / not yet available**, based on the public website reviewed on 2026-10-22. Update only when newer evidence is recorded.
3. Describe the current offering as a concept under development focused on helping families organize everyday medicine-routine details and share family context.
4. Do not state that prescription OCR, AI prescription interpretation, dose tracking, refill prediction, reminders, accounts, family sharing, or another specific feature is live without verification.
5. Do not invent launch dates, pricing, sign-up availability, traction, testimonials, clinical evidence, certifications, security implementations, partnerships, or outcomes.
6. Treat audience, positioning, and customer pain points as hypotheses unless the source register supports stronger status.
7. Do not make medical decisions, diagnoses, treatment recommendations, or dosage claims. Renomedy is not medical advice and does not replace healthcare professionals.
8. AI review is a linting aid, not medical, legal, privacy, regulatory, or publication clearance. Human approval is required before publishing.
9. When a document depends on an unconfirmed fact, avoid the claim, label it as a hypothesis, or request owner confirmation.
10. Do not use acquisition CTAs such as “Download now” or “Sign up” unless the owner confirms both availability and the destination.

## Status vocabulary

- **Publicly stated:** Explicitly present in a dated public source.
- **Owner-context:** Present in internal project material; not necessarily externally verified.
- **Verified behavior:** Directly checked in a relevant running product/environment, with date and scope recorded.
- **Hypothesis:** Plausible and awaiting validation.
- **Unconfirmed:** Not established by available evidence.
- **Approved:** Explicitly approved by the owner for a defined purpose and scope.
- **Superseded:** Replaced by a newer source or decision; retain history and link to the replacement.

## Work sequence

Expand one stage at a time. For each stage:
1. Review existing source material and decisions.
2. Draft the stage README and numbered Markdown files.
3. Separate evidence, assumptions, recommendations, and owner decisions.
4. Check consistency against the current knowledge base.
5. Publish the stage files on the `Marketing-Crew` branch.
6. Mark the stage as awaiting owner review; do not treat publication as approval.

No codebase or technical-app implementation work is part of this knowledge-base expansion. The priority is to complete and review all four knowledge-base blocks before moving on to building the agents.

## Existing repository workflow

The marketing-system repository has a separate approval-first content workflow. This knowledge base supports that workflow; it does not replace its human review requirements. Never publish content merely because an AI reviewer passes it.


## Mandatory stage-numbering convention

Every stage has its own folder inside its parent block. Markdown filenames use the stage number as the prefix and the file sequence after the decimal: Stage 1 uses `1.1.md`, `1.2.md`, etc.; Stage 2 uses `2.1.md`, `2.2.md`, etc.; Stage 10 uses `10.1.md`, `10.2.md`, etc. **Never restart file numbering at `1.x` for another stage.** Keep each file inside that stage's folder and list it in that stage's README.
