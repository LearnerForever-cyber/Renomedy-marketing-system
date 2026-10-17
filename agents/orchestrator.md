# Agent 00 — Orchestration contract

## Purpose
Coordinate the research → strategy → drafting → review → human approval → measurement loop. This file defines the workflow; it is not yet connected to an autonomous runtime.

## Run contract
1. Read the approved brand guardrails and product truth notes.
2. Request research insights with source/date/confidence metadata.
3. Ask strategy to turn only supported insights into a prioritized brief.
4. Ask drafting to create the requested Instagram format.
5. Pass the complete draft and claims list to the review agent.
6. If review returns BLOCK, stop and return the reasons. If NEEDS EDITS, revise and re-review.
7. If review returns PASS, mark the content as **awaiting human approval**. PASS is not publication permission.
8. Only after a human explicitly approves may the content be scheduled for manual publishing.
9. Record the published URL and metrics after 48 hours and 7 days.
10. Send observed results and caveats to the learning agent.

## Required content states
`idea → briefed → drafted → review_needed → needs_edits | blocked | awaiting_human_approval → approved → published → measured`

## Stop conditions
- Missing or unverifiable product capability.
- Unsupported health claim or absent source for a material medical statement.
- Personal or identifiable health information.
- No human approval.
- Any request to autonomously publish before the team enables and tests a separate publishing integration.

## Required audit fields
Content ID, author/agent role, source URLs and dates, prompt/config version, reviewer result, human approver and timestamp, published URL, metrics window, and learning summary.

## Failure behavior
Fail closed. If a source, review result or approval state is missing or ambiguous, do not publish. Never silently downgrade a BLOCK to PASS.
