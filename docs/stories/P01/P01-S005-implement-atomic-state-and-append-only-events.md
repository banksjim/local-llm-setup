# P01-S005: Implement atomic state and append-only events

| Property | Value |
|---|---|
| Story ID | P01-S005 |
| Phase | P01 — Program Control and Quality Foundation |
| Sequence | 6 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P01-S004 |
| Unlocks | P01-S006 |
| Preferred route | Interface: Codex CLI in the repository; Provider: OpenAI; Model class: architecture-capable implementation; Effort: medium; Fallback: Claude Code with an Anthropic architecture-capable model at medium effort; independent cross-provider review is required and local execution is prohibited before P03 qualification. |
| Research freshness | Current filesystem atomic-write guidance checked within 30 days. |

## 1. User story

As the workstation owner, I want this story to implement crash-safe checkpoints, tamper-evident events, and authority reconciliation, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Implement crash-safe checkpoints, tamper-evident events, and authority reconciliation.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P01-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current filesystem atomic-write guidance checked within 30 days. Record access date, version, direct links, material claims, conflicts, and inferences. Do not rely on model training memory for changeable facts.

## 5. Preconditions and unlock conditions

P01-S004. Applicable specifications, clean Git state, current research, required model route, and the accepted bootstrap-or-controller checks must pass.

## 6. In scope

Implement state serialization and atomic replacement in `goagentic/src/State.psm1`, hash-linked append-only events in `goagentic/src/EventLog.psm1`, corruption and interrupted-write fixtures, and unit/integration tests. Runtime files live under ignored `.goagentic/`; sanitized accepted evidence lives under `evidence/P01-S005/`.

## 7. Out of scope and prohibited changes

Mutation leasing, pause/resume policy, GitHub synchronization, storing secrets in events, treating wall-clock order as authority, automatic repair of ambiguous corruption, and writing runtime state outside `.goagentic/`.

## 8. Privilege and human approval

Not applicable — implementation and disposable-fixture writes are covered by the P01 phase authorization; tests may not touch external, privileged, or user-data state.

## 9. Risk rationale

The story is High risk because corrupt or partially written controller state could misidentify the authorized story and cause later out-of-scope mutations. Although confined to controller files, it requires integration tests, failure injection, recoverable backups, and cross-provider review.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the currently accepted P01 mutation guard—the bootstrap lock through P01-S006 and the controller lease only after P01-S006 is accepted; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the guard; and route to review or human validation. Interrupted writes preserve the last valid checkpoint; corrupt state is detected; events remain auditable.

## 11. Automated acceptance tests

Interrupted writes preserve the last valid checkpoint; corrupt state is detected; events remain auditable. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass. A justified not-applicable test is recorded rather than omitted.

## 12. Human validation

Not applicable — deterministic interruption and tamper fixtures plus cross-provider review validate persistence. The owner does not manually judge binary state integrity.

## 13. Idempotency and rollback

Writing an unchanged logical state creates no conflicting transition; duplicate event IDs are rejected. Each atomic replacement preserves the last valid checkpoint until verification succeeds. Rollback restores the prior module revision and copied fixture state; it never rewrites accepted evidence or silently truncates events.

## 14. Required evidence

Story revision; state/event schema versions; module and fixture hashes; clean-write, interrupted-write, duplicate-event, reordered-event, tamper, and corruption results; recovered checkpoint identity; secret scan; repeat result; rollback rehearsal; and cross-provider review verdict.

## 15. Definition of done

The last complete checkpoint survives every injected interruption; altered, missing, duplicate, or reordered events are detected; ambiguous corruption stops with one non-destructive recovery action; unchanged writes are idempotent; and P01-S006 is unblocked after cross-provider review.

## 16. Pause-safe boundaries

Pause before a state transition, after an atomic replacement verifies, and after an event append verifies. Never pause between temporary-file durability and atomic rename or between event hash calculation and append; on interruption, retain both artifacts for reconciliation.
