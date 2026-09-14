# P01-S004: Implement read-only orientation commands

| Property | Value |
|---|---|
| Story ID | P01-S004 |
| Phase | P01 — Program Control and Quality Foundation |
| Sequence | 4 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Medium |
| Actor | LLM |
| Dependencies | P01-S003 |
| Unlocks | P01-S005 |
| Preferred route | Controller-selected value route; qualified local model allowed after P03; cloud fallback per SYS-CTL. |
| Research freshness | Current PowerShell and CLI conventions checked within 30 days. |

## 1. User story

As the workstation owner, I want this story to implement a static zero-context entry document plus bare goagentic, status, next, and model on Windows without workstation dependencies, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Implement a static `START-HERE.md` plus bare goagentic, status, next, and model on Windows without workstation dependencies. The static document points to the command and never duplicates dynamic status.

## 3. Learning objective

Not applicable — a separate preceding learning story covers the major concept, or this story introduces no new owner-operated concept.

## 4. Current research requirements

Current PowerShell and CLI conventions checked within 30 days. Record access date, version, direct links, material claims, conflicts, and inferences. Do not rely on model training memory for changeable facts.

## 5. Preconditions and unlock conditions

P01-S003. Applicable specifications, clean Git state, valid controller state, current research, required model route, and lease checks must pass.

## 6. In scope

Only the objective, declared files and services, automated tests, documentation, evidence, and minimum safe supporting changes.

## 7. Out of scope and prohibited changes

Unrelated phase work, unapproved architecture changes, public exposure, secret disclosure, destructive cleanup, and actions not named in this story.

## 8. Privilege and human approval

Not applicable — no separate human action is required beyond active phase authorization.

## 9. Risk rationale

Work changes bounded repository or user-level configuration and is directly reversible from versioned backup. New facts may raise risk; an LLM cannot lower it.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the lease; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the lease; and route to review or human validation. Each command returns schema-valid output and exactly one safe next action without mutating project work; `START-HERE.md` stays accurate after state changes.

## 11. Automated acceptance tests

Each command returns schema-valid output and exactly one safe next action without mutating project work. `START-HERE.md` contains no generated status and remains accurate across fixture state changes. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass.

## 12. Human validation

Not applicable — automated evidence and independent review are sufficient for this story.

## 13. Idempotency and rollback

A second execution must report no unintended change. Before mutation, capture the exact rollback point; rollback restores only story-owned changes and preserves user data.

## 14. Required evidence

Story revision; actor, provider/model and effort when applicable; dated sources; changed-file and operation inventory; sanitized outputs; acceptance results; approval; idempotency and rollback; independent verdict; and human evidence when required.

## 15. Definition of done

The objective and tests pass; evidence is complete; no prohibited change occurred; review is accepted; human validation is genuine; controller and Git/GitHub agree; and the next story is unblocked.

## 16. Pause-safe boundaries

Pause before mutation, after each independently reversible operation, after tests, and after durable evidence. Never pause during partial replacement; finish or roll back that atomic operation first.
