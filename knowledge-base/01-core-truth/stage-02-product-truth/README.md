# Stage 2 — Product Truth

**Status:** Working draft — owner approval pending  
**Block:** 1 — Core Truth

## Purpose
Establish what Renomedy is publicly documented to be, what is only intended, what is unknown, and which claims are allowed.

## Stage files
- [2.1 — Product Definition & Public Status](2.1.md)
- [2.2 — Concept Scope & Intended User Tasks](2.2.md)
- [2.3 — Capability Status Matrix](2.3.md)
- [2.4 — AI, OCR & Automation Claims](2.4.md)
- [2.5 — Clinical, Safety, Privacy & Trust Boundaries](2.5.md)
- [2.6 — Verification Protocol, Review Checklist & Open Questions](2.6.md)

## Evidence policy
This stage uses the repository's [Source Register](../../sources/source-register.md), [Fact Ledger](../../sources/fact-ledger.md), and [Health Claims, Trust and Safety Guardrails](../../safety/health-claims-and-guardrails.md). It also uses the owner-provided Renomedy Context file as internal planning evidence—not independent proof of a shipped feature.

### Evidence labels
- **Publicly stated (source snapshot):** stated by the public website in the source register, whose last recorded access is 2026-10-22. This is evidence of what the website said at that time, not proof of implementation.
- **Internal record:** documented in owner-provided context or repository files; not independently verified unless a separate source is recorded.
- **Hypothesis:** a proposed user need, audience, or product proposition requiring validation.
- **Unknown / unverified:** no adequate evidence available.
- **Conflicting / stale:** evidence differs or needs a fresh check.

## Mandatory rules
1. Do not call a feature live merely because it appears in the product vision, a mock-up, a prototype plan, or an old conversation.
2. Do not infer technical implementation from a list of technologies that were explored.
3. Do not describe illustrative screens as the live application.
4. Do not claim clinical validation, regulatory approval, certification, security controls, encryption, or privacy guarantees without current, specific evidence and owner approval.
5. Record the exact source, access date, what it proves, and limitations for material claims.
6. If the public website cannot be accessed during review, say so explicitly; do not treat an old source-register entry as a fresh verification.
7. When evidence is missing, use **Unknown** rather than filling the gap with a plausible guess.
8. Owner approval is required before these working drafts become canonical.

## Current verification limitation
The public website is listed as S1 in the source register and was last recorded as accessed on **2026-10-22**. A fresh access attempt on **2026-10-24** through the available web retrieval tool was unsuccessful. Therefore, this draft is grounded in the recorded S1 snapshot and existing fact ledger, **not a successful live re-check on 2026-10-24**. Re-check the canonical page manually or through a working browser before treating its wording as freshly verified.

## Completion gate
Stage 2 is ready for owner review only when each material claim has an evidence label; feature status is not inferred from intent; source dates and limitations are visible; unresolved questions remain explicit; no unverified feature or health/security claim is promoted to public fact; and the owner confirms current product status and the capability matrix.

Publication to GitHub means **working draft available for review**, not owner-approved, technically verified, or clinically validated.
