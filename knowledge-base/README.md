# Renomedy Brand Knowledge Base

**Version:** 0.2.0  
**Status:** Source-audited draft — owner approval still required  
**Last reviewed:** 2026-10-22

## What this is

A source-aware knowledge base for Renomedy's future marketing automation. It distinguishes what the current public website says from the broader product vision in the owner-provided project context, and from assumptions that still need validation.

**Do not treat this knowledge base as proof that a feature is implemented.** The current public website explicitly says Renomedy is in development, not yet available, and that the screens are illustrative concepts.

## Source priority

1. Current owner-approved product facts and verified running-product behavior.
2. Current public Renomedy website for claims made to prospective users.
3. Owner-provided Renomedy project context for internal vision and explored technologies.
4. Prior project discussions for current plans and hypotheses.
5. AI inference — never promote this to fact without confirmation.

See `sources/source-register.md` and `sources/fact-ledger.md`.

## Structure

- `brand/` — public identity, voice and messaging rules
- `product/` — public concept, internal vision and capability status
- `audience/` — audiences named publicly and hypotheses to validate
- `strategy/` — positioning and validation hypotheses
- `safety/` — health, trust and claim guardrails
- `sources/` — sources, provenance, confidence and fact ledger
- `templates/` — campaign brief for future campaigns

## Mandatory instructions for AI agents

1. Read `sources/source-register.md`, `sources/fact-ledger.md` and `safety/health-claims-and-guardrails.md` before generating content.
2. The current product status is **in development / not yet available**, based on the current public website checked on 2026-10-22. Do not market Renomedy as a live app.
3. Publicly describe the current offering as a concept under development, focused on helping families organize everyday medicine-routine details and share family context.
4. Do not state that prescription OCR, AI prescription interpretation, dose tracking, refill prediction, reminders, accounts, family sharing, or any other specific feature is live. The internal context describes some of these as intended capability areas, not verified shipped functionality.
5. Do not invent launch dates, pricing, sign-up availability, traction, testimonials, clinical evidence, certifications, security implementations, partnerships or outcomes.
6. Treat the audience, positioning and customer pain points as hypotheses unless explicitly supported by the source register.
7. Do not make medical decisions, diagnoses, treatment recommendations or dosage claims. Renomedy is not a source of medical advice and does not replace healthcare professionals.
8. Treat trend content as inspiration only. Do not copy scripts, captions or distinctive creative work.
9. If the requested campaign depends on an unconfirmed fact, flag it for owner review or choose a safer concept.
10. Do not use an acquisition CTA such as "Download now", "Start today" or "Sign up" unless the owner confirms the destination and product availability. A concept-exploration CTA may be used only if it points to the current public page/working section.

## Status vocabulary

- **Publicly stated:** Explicitly present on the public site.
- **Owner-context:** Present in the owner-provided internal project context, but not necessarily publicly verified.
- **Hypothesis:** Plausible but not validated.
- **Unconfirmed:** Not established in the available sources.
- **Approved:** Explicitly approved by the owner for marketing use.

## Next step

The owner should review `strategy/open-questions.md` and approve a canonical fact list before connecting this knowledge base to CrewAI.
