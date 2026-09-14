# P02-S012: Perform foundation human acceptance

| Property | Value |
|---|---|
| Story ID | P02-S012 |
| Phase | P02 — Windows, WSL, Git, and VS Code Foundation |
| Sequence | 12 |
| Status | Planned |
| Step | Human Validation |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | Human + LLM |
| Dependencies | P02-S011 |
| Unlocks | P03-S001 |
| Preferred route | Human through a goagentic-guided checklist with the controller-selected current assistant model; no unattended substitution. |
| Research freshness | Not applicable — validation uses the configured machine. |

## 1. User story

As the workstation owner, I want this story to verify daily VS Code, shell, Git, restart, backup-export, and rollback workflows on the actual workstation, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Verify daily VS Code, shell, Git, restart, backup-export, and rollback workflows on the actual workstation.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P02-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Not applicable — validation uses the configured machine, recorded versions, and accepted P02 specification; it makes no new current-product recommendation.

## 5. Preconditions and unlock conditions

P02-S011. Applicable specifications, clean Git state, valid controller state, current research, required model route, and lease checks must pass.

## 6. In scope

Only the objective, declared files and services, automated tests, documentation, evidence, and minimum safe supporting changes.

## 7. Out of scope and prohibited changes

Unrelated phase work, unapproved architecture changes, public exposure, secret disclosure, destructive cleanup, and actions not named in this story.

## 8. Privilege and human approval

Required — the human performs or validates the declared work; an LLM may guide but cannot create completion evidence.

## 9. Risk rationale

Work crosses a security, privilege, destructive-data, authentication, or program-acceptance boundary and requires explicit owner control. New facts may raise risk; an LLM cannot lower it.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the lease; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the lease; and route to review or human validation. The owner completes the checklist and P02 evidence shows no unintended Windows access from Ubuntu.

## 11. Automated acceptance tests

The owner completes the checklist and P02 evidence shows no unintended Windows access from Ubuntu. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass. A justified not-applicable test is recorded rather than omitted.

## 12. Human validation

The owner completes the story-specific checklist and records the result through the controller.

## 13. Idempotency and rollback

A second execution must report no unintended change. Before mutation, capture the exact rollback point; rollback restores only story-owned changes and preserves user data.

## 14. Required evidence

Story revision; actor, provider/model and effort when applicable; dated sources; changed-file and operation inventory; sanitized outputs; acceptance results; approval; idempotency and rollback; independent verdict; and human evidence when required.

## 15. Definition of done

The objective and tests pass; evidence is complete; no prohibited change occurred; review is accepted; human validation is genuine; controller and Git/GitHub agree; and the next story is unblocked.

## 16. Pause-safe boundaries

Pause before mutation, after each independently reversible operation, after tests, and after durable evidence. Never pause during partial replacement; finish or roll back that atomic operation first.
