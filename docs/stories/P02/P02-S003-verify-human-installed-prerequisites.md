# P02-S003: Verify human-installed prerequisites

| Property | Value |
|---|---|
| Story ID | P02-S003 |
| Phase | P02 — Windows, WSL, Git, and VS Code Foundation |
| Sequence | 3 |
| Status | Planned |
| Step | Human Validation |
| Hold reason | Dependency |
| Risk | Medium |
| Actor | Human + LLM |
| Dependencies | P02-S002 |
| Unlocks | P02-S004 |
| Preferred route | Human through a goagentic-guided checklist with the controller-selected current assistant model; no unattended substitution. |
| Research freshness | Current prerequisite requirements from P02 research. |

## 1. User story

As the workstation owner, I want this story to verify Windows updates, WSL2, Rancher Desktop, Git, virtualization, NVIDIA driver, H drive, and available space without installing them, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Verify Windows updates, WSL2, Rancher Desktop, Git, virtualization, NVIDIA driver, H drive, and available space without installing them.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P02-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current prerequisite requirements from P02 research. Record access date, version, direct links, material claims, conflicts, and inferences. Do not rely on model training memory for changeable facts.

## 5. Preconditions and unlock conditions

P02-S002. Applicable specifications, clean Git state, valid controller state, current research, required model route, and lease checks must pass.

## 6. In scope

Only the objective, declared files and services, automated tests, documentation, evidence, and minimum safe supporting changes.

## 7. Out of scope and prohibited changes

Unrelated phase work, unapproved architecture changes, public exposure, secret disclosure, destructive cleanup, and actions not named in this story.

## 8. Privilege and human approval

Required — the human performs or validates the declared work; an LLM may guide but cannot create completion evidence.

## 9. Risk rationale

Work changes bounded repository or user-level configuration and is directly reversible from versioned backup. New facts may raise risk; an LLM cannot lower it.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the lease; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the lease; and route to review or human validation. A sanitized preflight report records versions, health, free space, and exact remediations. It estimates initial and growth storage for models, containers, WSL, source versions, Git knowledge output, indexes, logs, and backup retention; insufficient headroom blocks the next story.

## 11. Automated acceptance tests

A sanitized preflight report records versions, health, free space, and exact remediations. It estimates initial and growth storage for models, containers, WSL, immutable sources, Git knowledge output, indexes, logs, and at least one restorable backup generation; insufficient headroom blocks the next story. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass.

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
