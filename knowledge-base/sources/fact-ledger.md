# Fact Ledger

The marketing agent must consult this ledger before making product claims.

| Claim / fact | Status | Source | Allowed use |
|---|---|---|---|
| Product name is Renomedy | Publicly stated | S1 | May use |
| Public headline is “Care works better, together.” | Publicly stated | S1 | May use as current site wording |
| Product is in development and not yet available | Publicly stated | S1 | Must be reflected where availability matters |
| Website screens are illustrative concepts, not a live product | Publicly stated | S1 | Must not imply screens are live |
| Concept concerns organizing everyday medicine-routine details | Publicly stated | S1 | May describe as concept direction |
| Concept concerns family context and coordination | Publicly stated | S1 | May describe as concept direction |
| Parents, adult children and family caregivers are named audiences | Publicly stated | S1 | May target carefully; demand not validated |
| Renomedy is not medical advice, diagnosis or treatment recommendation and does not replace professionals | Publicly stated | S1 | Use as a boundary |
| AI-assisted prescription understanding is part of long-term vision | Owner-context | S2 | Internal planning only; not a live feature claim |
| Dose-event tracking is part of long-term vision | Owner-context | S2 | Internal planning only; not a live feature claim |
| Refill/supply-gap estimation is part of long-term vision | Owner-context | S2 | Internal planning only; not a live feature claim |
| ML Kit, Tesseract, MedGemma, Groq and Gemini have been explored | Owner-context | S2 | Do not claim current integration or production use |
| Exact production stack is known | Unconfirmed | S2 says it is not reliably established | Do not state |
| Product is clinically validated or certified | Unconfirmed | No verified evidence supplied | Prohibited unless evidenced and approved |
| Product has a particular encryption/security implementation | Unconfirmed | No verified evidence supplied | Prohibited unless evidenced and approved |
| Brand hex colors, typography and final mascot rules are approved | Unconfirmed | Not established by reviewed source | Do not invent |
| Adult children managing parents' medicines are the best converting segment | Hypothesis | S1/S2 and project discussion | Test, do not state as proven |
| Renomedy has product-market fit or validated retention | Unconfirmed | No verified evidence supplied | Do not claim |

## Rule

If a requested output needs a fact not marked `Publicly stated` or `Approved`, the agent must either:
1. avoid the claim,
2. label it clearly as a concept/hypothesis, or
3. request human confirmation.

The agent must never promote an `Owner-context`, `Hypothesis` or `Unconfirmed` item into a public product fact on its own.
