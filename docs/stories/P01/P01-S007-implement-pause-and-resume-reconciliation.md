# P01-S007: Implement pause and resume reconciliation

| Property | Value |
|---|---|
| Story ID | P01-S007 |
| Phase | P01 — Program Control and Quality Foundation |
| Sequence | 8 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P01-S006 |
| Unlocks | P01-S008 |
| Preferred route | Interface: Codex CLI in the repository; Provider: OpenAI; Model class: architecture-capable implementation; Effort: medium; Fallback: Claude Code with an Anthropic architecture-capable model at medium effort; independent cross-provider review is required and local execution is prohibited before P03 qualification. |
| Research freshness | Current recovery/state-machine guidance checked within 30 days. |

## 1. User story

As the workstation owner, I want this story to implement safe-boundary pause and non-executing resume across clean return, crash, drift, and reboot, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Implement safe-boundary pause and non-executing resume across clean return, crash, drift, and reboot.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P01-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current recovery/state-machine guidance checked within 30 days. Record access date, version, direct links, material claims, conflicts, and inferences. Do not rely on model training memory for changeable facts.

## 5. Preconditions and unlock conditions

P01-S006. Applicable specifications, clean Git state, current research, required model route, and the accepted bootstrap-or-controller checks must pass.

## 6. In scope

Implement pause-request, safe-boundary checkpoint, inspection-only resume, and reconciliation classification in `goagentic/src/Recovery.psm1`; extend command dispatch for `pause` and `resume`; and add fixtures for clean pause, pre-mutation crash, mid-operation crash, drift, missing checkpoint, stale lease, outage, and ambiguity.

## 7. Out of scope and prohibited changes

Automatically continuing pending work on `resume`, guessing through ambiguous state, terminating unrelated processes, rolling back without a declared story operation, or treating chat history as recovery evidence.

## 8. Privilege and human approval

Not applicable — repository implementation and isolated recovery fixtures are covered by the P01 phase authorization; ambiguous real-state recovery is outside this story.

## 9. Risk rationale

The story is High risk because an incorrect resume decision could repeat a destructive operation or skip required verification. Resume therefore remains inspection-only, ambiguity fails closed, and failure injection plus cross-provider review are mandatory.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the currently accepted P01 mutation guard—the bootstrap lock through P01-S006 and the controller lease only after P01-S006 is accepted; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the guard; and route to review or human validation. Failure fixtures classify each recovery case and resume never performs pending implementation.

## 11. Automated acceptance tests

Failure fixtures classify each recovery case and resume never performs pending implementation. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass. A justified not-applicable test is recorded rather than omitted.

## 12. Human validation

Not applicable — every reconciliation class is verified against synthetic state and reviewed independently. Owner-facing pause/restart/resume behavior is accepted in P01-S014.

## 13. Idempotency and rollback

Repeated `pause` requests collapse into one pending request; repeated `resume` on unchanged state returns the same classification and never runs story work. Rollback restores the prior command and recovery modules while preserving the last valid checkpoint and append-only events.

## 14. Required evidence

Story revision; module hashes; fixture inventory; pause-latency and safe-boundary output; every reconciliation classification; proof that no resume fixture invoked mutation; drift, outage, and ambiguity results; repeat comparison; rollback rehearsal; and cross-provider verdict.

## 15. Definition of done

Every fixture maps to the documented classification and one safe next action; pause occurs only at declared boundaries; `resume` produces no story mutation; ambiguous or drifting state remains blocked; and P01-S008 is unblocked after cross-provider review.

## 16. Pause-safe boundaries

Pause after each fixture classification and after a safe checkpoint is durable. Do not pause during an atomic story operation or while changing a reconciliation verdict; on interruption, rerun inspection from the last trusted checkpoint.
