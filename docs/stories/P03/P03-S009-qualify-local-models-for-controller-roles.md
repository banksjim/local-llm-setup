# P03-S009: Qualify local models for controller roles

| Property | Value |
|---|---|
| Story ID | P03-S009 |
| Phase | P03 — Local Inference and Model Foundation |
| Sequence | 9 |
| Status | Planned |
| Step | Testing |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P03-S008 |
| Unlocks | P03-S010 |
| Preferred route | Interface: goagentic in the designated cloud IDE or CLI; Provider: OpenAI or Anthropic, different from the implementer for acceptance review; Model class: current quality or review model; Effort: high; Fallback: stop and switch to the current Sol or Sonnet-class route; qualified local models remain advisory during probation. |
| Research freshness | Current cloud comparison route confirmed at activation. |

## 1. User story

As the workstation owner, I want this story to test structured output, instructions, repository work, tools, uncertainty, correction, and review behavior, so that progress is inspectable and independent of chat memory.

## 2. Bounded objective

Test structured output, instructions, repository work, tools, uncertainty, correction, and review behavior.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P03-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current cloud comparison route confirmed at activation. Record dates, versions, direct links, claims, conflicts, and inferences; do not rely on training memory for changeable facts.

## 5. Preconditions and unlock conditions

P03-S008. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create and verify controller-role fixture pack, local-model evaluator, per-capability pass or fail report, probation policy update, and disqualification record; no live story is delegated during qualification. Store versioned implementation or guidance at the story-owned output path already named by this contract and sanitized run evidence under evidence/P03-S009/.

## 7. Out of scope and prohibited changes

Do not install containers or desktop clients, expose Ollama to the LAN, delete existing models, change BIOS or GPU drivers, accept floating model tags, or route unqualified controller work to a local model.

## 8. Privilege and human approval

No new approval is required while the revision-bound P03 phase authorization still matches the work. The LLM may execute only the previewed story-owned operations; any changed target, network boundary, data class, risk, or destructive action stops for a new preview.

## 9. Risk rationale

Granting a local model controller work can cause repository mutations; qualification must fail closed and retain cloud review.

## 10. Execution contract

Create an activation packet; verify dependencies, freshness, and targets; preview the exact change; confirm revision-bound phase authorization where mutation is privileged; acquire the controller lease; produce tests/p03/P03-S009-qualify-local-models-for-controller-roles; run the named positive and negative checks; record sanitized evidence; release the lease. Acceptance criterion: each proposed controller role passes frozen structured-output, instruction, repository, tool, uncertainty, correction, and adversarial-scope fixtures; failures cannot be averaged away.

## 11. Automated acceptance tests

Assert the expected story inventory is nonzero, then verify that each proposed controller role passes frozen structured-output, instruction, repository, tool, uncertainty, correction, and adversarial-scope fixtures; failures cannot be averaged away. Fail on missing evidence, unexpected targets, secrets, stale sources, an untested negative boundary, or a validator that matched zero fixtures.

## 12. Human validation

Not applicable — P03-S009 is accepted through deterministic checks plus an independent review; no experiential or credential-bearing action is delegated to the LLM.

## 13. Idempotency and rollback

Tests use synthetic or owner-approved fixtures and leave accepted services and configuration unchanged. Rollback removes story-created fixtures and restores the pre-test snapshot recorded in evidence/P03-S009/rollback.json.

## 14. Required evidence

Commit tests/p03/P03-S009-qualify-local-models-for-controller-roles or its versioned result plus evidence/P03-S009/activation.json, evidence/P03-S009/change-inventory.json, evidence/P03-S009/test-results.json, evidence/P03-S009/rollback.json, and evidence/P03-S009/review.md; include exact versions or digests, sanitized commands or observations, timestamps, and an explicit not-applicable human record.

## 15. Definition of done

P03-S009 is Done only when each proposed controller role passes frozen structured-output, instruction, repository, tool, uncertainty, correction, and adversarial-scope fixtures; failures cannot be averaged away; the story-owned output and evidence inventory exist, independent review has no unresolved material finding, rollback and idempotency evidence is accepted, and controller state unlocks the declared next story.

## 16. Pause-safe boundaries

Pause after the activation packet, after each download, install, configuration backup, or other atomic unit, after tests, and after evidence is committed. Before pausing, finish or roll back the active unit and record the exact next command plus current model and provider in evidence/P03-S009/checkpoint.json.
