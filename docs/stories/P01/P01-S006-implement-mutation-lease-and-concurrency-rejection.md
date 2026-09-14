# P01-S006: Implement mutation lease and concurrency rejection

| Property | Value |
|---|---|
| Story ID | P01-S006 |
| Phase | P01 — Program Control and Quality Foundation |
| Sequence | 7 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P01-S005 |
| Unlocks | P01-S007 |
| Preferred route | Interface: Codex CLI in the repository; Provider: OpenAI; Model class: architecture-capable implementation; Effort: medium; Fallback: Claude Code with an Anthropic architecture-capable model at medium effort; independent cross-provider review is required and local execution is prohibited before P03 qualification. |
| Research freshness | Current process-locking guidance checked within 30 days. |

## 1. User story

As the workstation owner, I want this story to permit one writer and safe read-only observers, including stale-lease inspection, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Permit one writer and safe read-only observers, including stale-lease inspection.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P01-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current process-locking guidance checked within 30 days. Record access date, version, direct links, material claims, conflicts, and inferences. Do not rely on model training memory for changeable facts.

## 5. Preconditions and unlock conditions

P01-S005. Applicable specifications, clean Git state, current research, required model route, and the accepted bootstrap-or-controller checks must pass.

## 6. In scope

Implement lease acquisition, heartbeat, inspection, release, and explicit recovery in `goagentic/src/Lease.psm1`; add process, host, story, operation, checkpoint, and observed-time metadata to the runtime schema; and add concurrency, expiry, crash, and clock-skew fixtures and tests.

## 7. Out of scope and prohibited changes

Distributed multi-host locking, force-breaking a lease solely because its timestamp expired, allowing two mutation roles, modifying Git or external services while testing, and embedding credentials or full sensitive command payloads in lease records.

## 8. Privilege and human approval

Not applicable — controller-module and isolated concurrency-fixture changes are covered by the P01 phase authorization and require no human prompt.

## 9. Risk rationale

The story is High risk because lease failure could permit concurrent agents to corrupt shared controller, Git, or later workstation state. Recovery ambiguity is intentionally fail-closed and requires integration testing, failure injection, and cross-provider review.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the currently accepted P01 mutation guard—the bootstrap lock through P01-S006 and the controller lease only after P01-S006 is accepted; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the guard; and route to review or human validation. Concurrent writers are rejected and an expired timestamp alone never removes a lease.

## 11. Automated acceptance tests

Concurrent writers are rejected and an expired timestamp alone never removes a lease. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass. A justified not-applicable test is recorded rather than omitted.

## 12. Human validation

Not applicable — controlled multi-process fixtures and cross-provider review prove exclusive ownership. The owner later experiences rejection and recovery behavior in P01-S014.

## 13. Idempotency and rollback

Repeated acquisition by the same proven owner renews rather than duplicates the lease; a different writer is rejected. Normal rollback releases only a lease owned by the current operation. Suspected stale leases are preserved for inspection and may be cleared only through the documented recovery decision.

## 14. Required evidence

Story revision; lease schema and module hashes; two-writer race output; same-owner renewal; reader coexistence; expired-but-live, crashed, clock-skew, and ambiguous-owner results; state/event correlation; repeat result; rollback rehearsal; and cross-provider verdict.

## 15. Definition of done

Exactly one writer succeeds in every race; read-only commands remain available; timestamp expiry alone never clears ownership; crash recovery reports one safe action; lease events correlate with state; and P01-S007 is unblocked after cross-provider review.

## 16. Pause-safe boundaries

Pause before acquisition, after ownership is durably recorded, after each race fixture, and after verified release. Never pause while transferring or clearing ownership; an interruption leaves the lease intact for inspection.
