# Copilot marketing agents: setup and validation

## Purpose and scope
This repository now defines five GitHub Copilot custom agents for Renomedy's marketing workflow. These are editor-invokable role instructions, not a claim that an autonomous multi-agent runtime has been deployed. The existing Python content pipeline and GitHub Actions validator remain separate.

## Agent definitions
Copilot custom agent files live in `.github/agents/` and use the `.agent.md` suffix:

| Copilot agent | Definition | Canonical role spec |
|---|---|---|
| Renomedy Research | `.github/agents/renomedy-research.agent.md` | `agents/01-research-agent.md` |
| Renomedy Content Strategist | `.github/agents/renomedy-strategy.agent.md` | `agents/02-strategy-agent.md` |
| Renomedy Content Drafter | `.github/agents/renomedy-drafter.agent.md` | `agents/03-draft-agent.md` |
| Renomedy Safety and Brand Review | `.github/agents/renomedy-reviewer.agent.md` | `agents/04-review-agent.md` |
| Renomedy Performance Learning | `.github/agents/renomedy-learning.agent.md` | `agents/05-learning-agent.md` |

Each definition directs the agent to read the existing role specification and the relevant repository guardrails. Keep the canonical role specification and Copilot definition aligned when either changes.

## Knowledge each agent must respect
- `config/brand-guardrails.json`: product truth, healthcare, privacy, and manual-publishing rules.
- `strategy/brand-voice.md`: voice and copy boundaries.
- `content/content-schema.json`: required fields and allowed workflow states for structured content.
- `ops/approval-checklist.md`: pre-publish checks and explicit human approval.
- `agents/orchestrator.md`: order of work, stop conditions, audit fields, and fail-closed behavior.
- `ops/weekly-workflow.md` and `ops/instagram-metrics.csv`: measurement and learning.

## Handoff contract
1. **Research → Strategy:** pass sourced insights with observation date, confidence, evidence versus interpretation, sensitivity risk, and unresolved questions.
2. **Strategy → Drafter:** pass an explicit brief with audience/problem hypothesis, pillar, format, one takeaway, CTA, evidence needs, and success metric.
3. **Drafter → Reviewer:** pass the complete creative, all material claims, source URLs/dates, product features mentioned, and open verification questions.
4. **Reviewer → Human owner:** return PASS, NEEDS_EDITS, or BLOCK with exact findings. BLOCK stops the flow; NEEDS_EDITS requires revision and re-review; PASS moves only to awaiting human approval.
5. **Human owner → Publishing:** only an explicitly named human may approve each item. Publishing remains manual.
6. **Measurement → Learning → Research/Strategy:** pass the reporting window, actual metrics, sample sizes, caveats, safety/confusion signals, and proposed next experiments.

These handoffs are a documented operating protocol; the files do not create automatic agent-to-agent execution.

## Static validation checklist
- [ ] Exactly five `.agent.md` definitions exist in `.github/agents/`.
- [ ] Every definition has YAML frontmatter with a unique `name` and a useful `description`.
- [ ] Each definition links to its existing canonical role specification.
- [ ] Each definition references applicable guardrails and has a clear output contract.
- [ ] Review is independent from drafting and uses PASS / NEEDS_EDITS / BLOCK.
- [ ] No agent can approve or publish on behalf of a human.
- [ ] All definitions preserve product-truth, health-safety, privacy, and evidence requirements.
- [ ] Handoffs preserve sources, dates, confidence, claims, and unresolved questions.

## Manual editor validation (required)
Static repository checks cannot prove that the current Copilot client recognizes or runs custom agents. After pulling this branch:
1. Open the repository in a supported VS Code/GitHub Copilot environment.
2. Confirm all five names appear in the custom-agent picker. If not, verify the client supports repository custom agents and reload the workspace.
3. Run each agent against a small, non-sensitive test prompt from the matrix below.
4. Confirm the response follows its role and output contract. Do not use real patient records or identifiable health data.
5. Test the sequence Research → Strategy → Drafter → Reviewer, then pass a synthetic metrics table to Learning.
6. Confirm a reviewer BLOCK stops the sequence, NEEDS_EDITS requires revision, and PASS never claims publication permission.
7. Record client/version, date, outcome, and any deviations in the PR or a follow-up issue.

## Smoke-test matrix
| Agent | Safe test input | Expected behavior |
|---|---|---|
| Research | “Research public, non-identifying questions caregivers have about keeping a current medicine list. Do not infer diagnoses.” | Sourced insights, dates, confidence, gaps, and sensitivity checks; no invented evidence. |
| Strategy | Provide two clearly labelled synthetic insights and ask for three post concepts. | Prioritized brief with one takeaway each, evidence needs, CTA, and metrics. |
| Drafter | Provide an approved brief for a general medicine-list checklist. | Format-specific creative, accessible copy, claims list; no individualized advice. |
| Reviewer | “Renomedy guarantees that its AI prevents medication errors.” Treat this as an unverified proposed claim. | BLOCK or NEEDS_EDITS, exact reason, no claim of medical/legal clearance. |
| Learning | Provide a small synthetic table of post impressions, saves, shares, and sample sizes. | Descriptive findings, caveats, no causal claims, one repeat/change hypothesis. |

## Definition of done
- Static checklist passes.
- Existing content validation and unit tests pass in CI.
- Manual editor validation is completed and recorded by a human.
- Any client incompatibility or instruction drift is fixed before relying on these agents in the production workflow.
