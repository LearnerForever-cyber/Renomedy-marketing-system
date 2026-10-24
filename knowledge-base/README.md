# Renomedy Brand Knowledge Base

**Version:** 0.4.0  
**Status:** Twelve-stage working draft — owner approval pending  
**Last reviewed:** 2026-10-24

## Purpose
A source-aware knowledge base for Renomedy's future marketing and AI-agent workflows. It separates recorded public statements from owner context, hypotheses, recommendations, and unknowns. It is not proof that a feature is implemented.

The latest recorded public-site snapshot (source register access date: 2026-10-22) says Renomedy is in development, not yet available, and that the screens are illustrative concepts. A fresh retrieval attempt on 2026-10-24 failed through the available web retrieval tool, so the status was not independently rechecked on that date. Do not market Renomedy as a live app unless newer evidence is recorded.

## Master structure

- [Block 1 — Core Truth](01-core-truth/README.md)
  - [Stage 1 — Company Foundation](01-core-truth/stage-01-company-foundation/README.md) — expanded working draft; owner approval pending.
  - [Stage 2 — Product Truth](01-core-truth/stage-02-product-truth/README.md) — evidence-aware working draft; owner approval pending.
  - [Stage 3 — Audience, Strategy & Safety](01-core-truth/stage-03-audience-strategy-safety/README.md) — evidence-aware working draft; owner approval pending.
- [Block 2 — Brand System](02-brand-system/README.md) — Stages 4–6 drafted; owner approval pending.
  - [Stage 4 — Identity System](02-brand-system/stage-04-identity-system/README.md).
  - [Stage 5 — Visual Design System](02-brand-system/stage-05-visual-design-system/README.md).
  - [Stage 6 — Messaging & Brand Voice](02-brand-system/stage-06-messaging-brand-voice/README.md).
- [Block 3 — Growth System](03-growth-system/README.md) — Stages 7–9 drafted; owner approval pending.
  - [Stage 7 — Research & Validation](03-growth-system/stage-07-research-validation/README.md).
  - [Stage 8 — Marketing & Distribution](03-growth-system/stage-08-marketing-distribution/README.md).
  - [Stage 9 — Measurement & Optimization](03-growth-system/stage-09-measurement-optimization/README.md).
- [Block 4 — Evidence System](04-evidence-system/README.md) — Stages 10–12 drafted; owner approval pending.
  - [Stage 10 — Sources & Fact Ledger](04-evidence-system/stage-10-sources-fact-ledger/README.md).
  - [Stage 11 — Decisions & Open Questions](04-evidence-system/stage-11-decisions-open-questions/README.md).
  - [Stage 12 — Experiments & Continuous Learning](04-evidence-system/stage-12-experiments-continuous-learning/README.md).

## Existing reference folders

These remain the evidence and operational reference layer while the stage folders are expanded:

- `brand/` — existing brand notes and rules.
- `product/` — product concept and capability-status documents.
- `audience/` — audience notes and hypotheses.
- `strategy/` — positioning, strategy, and open questions.
- `safety/` — health and claim guardrails.
- `sources/` — provenance, source register, and fact ledger.
- `templates/` — reusable campaign templates.

Stage documents should link to these sources rather than silently creating competing facts. If a stage and a source-of-truth file conflict, flag the conflict and resolve it explicitly.

## Mandatory instructions for future AI agents

1. Read `sources/source-register.md`, `sources/fact-ledger.md`, and `safety/health-claims-and-guardrails.md` before generating health-related marketing content.
2. Current product status is **in development / not yet available** according to the latest recorded public-site snapshot from 2026-10-22. This is not a fresh live-site verification; recheck before time-sensitive use.
3. Describe the current offering as a concept under development focused on helping families organize everyday medicine-routine details and share family context.
4. Do not state that prescription OCR, AI prescription interpretation, dose tracking, refill prediction, reminders, accounts, family sharing, or another specific feature is live without current verification.
5. Do not invent launch dates, pricing, signup availability, traction, testimonials, clinical evidence, certifications, security implementations, partnerships, or outcomes.
6. Treat audience, positioning, customer pain points, channel fit, and willingness to pay as hypotheses unless supported by recorded evidence.
7. Do not make medical decisions, diagnoses, treatment recommendations, or dosage claims. Renomedy is not medical advice and does not replace healthcare professionals.
8. AI review is a linting aid, not medical, legal, privacy, regulatory, or publication clearance. Human approval remains required.
9. When evidence is missing, state Unknown, label the claim as a hypothesis, omit it, or request owner confirmation.
10. Do not use acquisition CTAs such as “Download now” or “Sign up” unless the owner confirms current availability and a working destination.
11. Do not present owner approval as independent clinical, legal, regulatory, privacy, or security verification.

## Evidence-status vocabulary

- **Publicly stated:** Explicitly present in a dated public source; proves what the source says, not necessarily product implementation.
- **Owner-context:** Present in internal project material; not automatically externally verified.
- **Verified behavior:** Directly checked in a relevant running product/environment, with date and test scope recorded.
- **Hypothesis:** A proposition requiring validation.
- **Unconfirmed / Unknown:** Evidence is insufficient or missing.
- **Approved:** Explicitly approved by the owner for a defined purpose and scope.
- **Superseded:** Replaced by newer evidence or a decision; preserve history and link the replacement.
- **Proposed:** A recommended policy or strategy that has not yet been approved.

## Work sequence and completion standard

All twelve stages now have working draft files. This means the documentation structure and proposed operating rules have been drafted; it does **not** mean every stage is verified, owner-approved, or ready for production use.

For each stage:
1. Review existing source material and decisions.
2. Separate supported facts, internal context, hypotheses, recommendations, and unknowns.
3. Record source dates, limitations, and evidence needed.
4. Check consistency with the existing source register, fact ledger, safety guardrails, and adjacent stages.
5. Keep unverified claims out of public-facing fact statements.
6. Publish the stage for owner review; publication is not approval.

The canonical public site could not be freshly retrieved during this review, and no reviewed evidence establishes validated demand, campaign performance, clinical validation, or specific security implementation. These gaps remain open rather than being filled with guesses.

No codebase or technical-app implementation work is part of this knowledge-base expansion. Complete owner review of the four blocks before building agents.

## Mandatory stage-numbering convention

Every stage has its own folder inside its parent block. Filenames use the stage number as the prefix and the file sequence after the decimal: Stage 1 uses `1.1.md`, `1.2.md`; Stage 2 uses `2.1.md`, `2.2.md`; Stage 10 uses `10.1.md`, `10.2.md`. Continue through Stage 12. Never restart numbering at `1.x` for another stage. List every file in its stage README.
