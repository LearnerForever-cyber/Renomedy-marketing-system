# Stage 10 — Sources & Fact Ledger

**Status:** Working evidence-governance draft — owner approval pending

## Files
- [10.1 — Source Register Standard and Provenance](10.1.md)
- [10.2 — Fact Ledger Schema and Claim Rules](10.2.md)
- [10.3 — Source Review, Conflict and Freshness Protocol](10.3.md)

## Existing source-of-truth files
- ../../sources/source-register.md
- ../../sources/fact-ledger.md
- ../../safety/health-claims-and-guardrails.md

Do not create competing factual ledgers without linking and reconciling them. Existing records have known freshness limits: the public site snapshot is dated 2026-10-22, and fresh retrieval failed on 2026-10-24.

## Completion gate
- [ ] Owner approves source and claim-status conventions.
- [ ] All material new claims are entered in the existing source register/fact ledger.
- [ ] Conflicts and stale evidence are flagged rather than silently resolved.
