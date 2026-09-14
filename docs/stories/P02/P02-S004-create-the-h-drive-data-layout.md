# P02-S004: Create the H drive data layout

| Property | Value |
|---|---|
| Story ID | P02-S004 |
| Phase | P02 — Windows, WSL, Git, and VS Code Foundation |
| Sequence | 4 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P02-S003 |
| Unlocks | P02-S005 |
| Preferred route | Controller-selected quality route; cross-provider review required; qualified local execution only under current policy. |
| Research freshness | Current Windows ACL and filesystem guidance checked within 30 days. |

## 1. User story

As the workstation owner, I want this story to create the approved H drive AI directories, permissions, manifests, and non-destructive ownership rules, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Create the approved H drive AI directories, permissions, manifests, and non-destructive ownership rules.

## 3. Learning objective

Not applicable — a separate preceding learning story covers the major concept, or this story introduces no new owner-operated concept.

## 4. Current research requirements

Current Windows ACL and filesystem guidance checked within 30 days. Record access date, version, direct links, material claims, conflicts, and inferences. Do not rely on model training memory for changeable facts.

## 5. Preconditions and unlock conditions

P02-S003. Applicable specifications, clean Git state, valid controller state, current research, required model route, and lease checks must pass.

## 6. In scope

Only the objective, declared files and services, automated tests, documentation, evidence, and minimum safe supporting changes.

## 7. Out of scope and prohibited changes

Unrelated phase work, unapproved architecture changes, public exposure, secret disclosure, destructive cleanup, and actions not named in this story.

## 8. Privilege and human approval

Not applicable — no separate human action is required beyond active phase authorization.

## 9. Risk rationale

Work affects services, private data, credentials, networking, integration state, or several components; integration evidence and rollback are mandatory. New facts may raise risk; an LLM cannot lower it.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the lease; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the lease; and route to review or human validation. Dry run, first run, and second run pass; unknown files are preserved; rollback removes only empty managed paths.

## 11. Automated acceptance tests

Dry run, first run, and second run pass; unknown files are preserved; rollback removes only empty managed paths. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass. A justified not-applicable test is recorded rather than omitted.

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

