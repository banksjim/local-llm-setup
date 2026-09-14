# P02-S005: Create and locate the dedicated Ubuntu distribution

| Property | Value |
|---|---|
| Story ID | P02-S005 |
| Phase | P02 — Windows, WSL, Git, and VS Code Foundation |
| Sequence | 5 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | Human + LLM |
| Dependencies | P02-S004 |
| Unlocks | P02-S006 |
| Preferred route | Human through a goagentic-guided checklist with the controller-selected current assistant model; no unattended substitution. |
| Research freshness | Current Microsoft WSL import/export/move documentation checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to provision the named Ubuntu WSL2 distribution and place its VHDX under the approved H drive location using a previewed reversible procedure, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Provision the named Ubuntu WSL2 distribution and place its VHDX under the approved H drive location using a previewed reversible procedure.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P02-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current Microsoft WSL import/export/move documentation checked within 7 days. Record access date, version, direct links, material claims, conflicts, and inferences. Do not rely on model training memory for changeable facts.

## 5. Preconditions and unlock conditions

P02-S004. Applicable specifications, clean Git state, valid controller state, current research, required model route, and lease checks must pass.

## 6. In scope

Only the objective, declared files and services, automated tests, documentation, evidence, and minimum safe supporting changes.

## 7. Out of scope and prohibited changes

Unrelated phase work, unapproved architecture changes, public exposure, secret disclosure, destructive cleanup, and actions not named in this story.

## 8. Privilege and human approval

Required — the human performs or validates the declared work; an LLM may guide but cannot create completion evidence.

## 9. Risk rationale

Work crosses a security, privilege, destructive-data, authentication, or program-acceptance boundary and requires explicit owner control. New facts may raise risk; an LLM cannot lower it.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the lease; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the lease; and route to review or human validation. The distribution boots, location is verified, export backup succeeds, and no other distribution changes.

## 11. Automated acceptance tests

The distribution boots, location is verified, export backup succeeds, and no other distribution changes. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass. A justified not-applicable test is recorded rather than omitted.

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
