# P03-S010: Reassess every remaining story for local execution

| Property | Value |
|---|---|
| Story ID | P03-S010 |
| Phase | P03 — Local Inference and Model Foundation |
| Sequence | 10 |
| Status | Planned |
| Step | Review |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P03-S009 |
| Unlocks | P03-S011 |
| Preferred route | Interface: goagentic in the designated cloud IDE or CLI; Provider: OpenAI or Anthropic, different from the implementer for acceptance review; Model class: current quality or review model; Effort: high; Fallback: stop and switch to the current Sol or Sonnet-class route; qualified local models remain advisory during probation. |
| Research freshness | Current provider and model availability checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to review all unstarted P04 through P10 stories and propose qualified local roles without reducing quality gates, so that progress is inspectable and independent of chat memory.

## 2. Bounded objective

Review all unstarted P04 through P10 stories and propose qualified local roles without reducing quality gates.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P03-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current provider and model availability checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not rely on training memory for changeable facts.

## 5. Preconditions and unlock conditions

P03-S009. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create and verify the complete P04-P10 story inventory, per-story routing decision ledger, supporting qualification links, cost and review rules, and unchanged dependency and gate comparison. Store versioned implementation or guidance at the story-owned output path already named by this contract and sanitized run evidence under evidence/P03-S010/.

## 7. Out of scope and prohibited changes

Do not install containers or desktop clients, expose Ollama to the LAN, delete existing models, change BIOS or GPU drivers, accept floating model tags, or route unqualified controller work to a local model.

## 8. Privilege and human approval

No new approval is required while the revision-bound P03 phase authorization still matches the work. The LLM may execute only the previewed story-owned operations; any changed target, network boundary, data class, risk, or destructive action stops for a new preview.

## 9. Risk rationale

This changes routing for all remaining stories and can reduce quality or cost control if evidence is weak.

## 10. Execution contract

Create an activation packet; verify dependencies, freshness, and targets; preview the exact change; confirm revision-bound phase authorization where mutation is privileged; acquire the controller lease; produce evidence/P03-S010/routing-reassessment.md; run the named positive and negative checks; record sanitized evidence; release the lease. Acceptance criterion: every unstarted P04-P10 story has a recorded route decision, qualification evidence or cloud requirement, reviewer rule, and cost and quality rationale without changing its gate.

## 11. Automated acceptance tests

Assert the expected story inventory is nonzero, then verify that every unstarted P04-P10 story has a recorded route decision, qualification evidence or cloud requirement, reviewer rule, and cost and quality rationale without changing its gate. Fail on missing evidence, unexpected targets, secrets, stale sources, an untested negative boundary, or a validator that matched zero fixtures.

## 12. Human validation

Not applicable — P03-S010 is accepted through deterministic checks plus an independent review; no experiential or credential-bearing action is delegated to the LLM.

## 13. Idempotency and rollback

A repeat run refreshes evidence/P03-S010/routing-reassessment.md without duplicate records. Rollback restores its pre-story Git version and removes only unaccepted evidence/P03-S010/ evidence.

## 14. Required evidence

Commit evidence/P03-S010/routing-reassessment.md or its versioned result plus evidence/P03-S010/activation.json, evidence/P03-S010/change-inventory.json, evidence/P03-S010/test-results.json, evidence/P03-S010/rollback.json, and evidence/P03-S010/review.md; include exact versions or digests, sanitized commands or observations, timestamps, and an explicit not-applicable human record.

## 15. Definition of done

P03-S010 is Done only when every unstarted P04-P10 story has a recorded route decision, qualification evidence or cloud requirement, reviewer rule, and cost and quality rationale without changing its gate; the story-owned output and evidence inventory exist, independent review has no unresolved material finding, rollback and idempotency evidence is accepted, and controller state unlocks the declared next story.

## 16. Pause-safe boundaries

Pause after the activation packet, after each download, install, configuration backup, or other atomic unit, after tests, and after evidence is committed. Before pausing, finish or roll back the active unit and record the exact next command plus current model and provider in evidence/P03-S010/checkpoint.json.
