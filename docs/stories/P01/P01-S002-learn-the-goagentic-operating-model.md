# P01-S002: Learn the goagentic operating model

| Property | Value |
|---|---|
| Story ID | P01-S002 |
| Phase | P01 — Program Control and Quality Foundation |
| Sequence | 3 |
| Status | Planned |
| Step | Learning |
| Hold reason | Dependency |
| Risk | Low |
| Actor | Human + LLM |
| Dependencies | P01-S001 |
| Unlocks | P01-S003 |
| Preferred route | Human through a goagentic-guided checklist with the controller-selected current assistant model; no unattended substitution. |
| Research freshness | Current project specifications; external sources are not required. |

## 1. User story

As the workstation owner, I want this story to teach the owner the state, step, hold, lease, evidence, pause, resume, review, and authorization concepts needed for controller acceptance, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Teach the owner the state, step, hold, lease, evidence, pause, resume, review, and authorization concepts needed for controller acceptance.

## 3. Learning objective

Complete the targeted concepts in the objective and demonstrate them through the acceptance exercise.

## 4. Current research requirements

Current project specifications; external sources are not required. Record access date, version, direct links, material claims, conflicts, and inferences. Do not rely on model training memory for changeable facts.

## 5. Preconditions and unlock conditions

P01-S001. Applicable specifications, clean Git state, current research, required model route, and the accepted bootstrap-or-controller checks must pass.

## 6. In scope

Only the objective, declared files and services, automated tests, documentation, evidence, and minimum safe supporting changes.

## 7. Out of scope and prohibited changes

Unrelated phase work, unapproved architecture changes, public exposure, secret disclosure, destructive cleanup, and actions not named in this story.

## 8. Privilege and human approval

Required — the human performs or validates the declared work; an LLM may guide but cannot create completion evidence.

## 9. Risk rationale

No privileged mutation or user-data risk is expected; output is documentation, research, or learning evidence. New facts may raise risk; an LLM cannot lower it.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the lease; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the lease; and route to review or human validation. The owner completes the exercise and accurately explains why resume does not execute and why only goagentic go authorizes work.

## 11. Automated acceptance tests

The owner completes the exercise and accurately explains why resume does not execute and why only goagentic go authorizes work. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass. A justified not-applicable test is recorded rather than omitted.

## 12. Human validation

The owner completes the story-specific checklist and records the result through the controller.

## 13. Idempotency and rollback

A repeat produces an updated or identical evidence record without changing accepted implementation. Rollback is reversion of the story commit or evidence record.

## 14. Required evidence

Story revision; actor, provider/model and effort when applicable; dated sources; changed-file and operation inventory; sanitized outputs; acceptance results; approval; idempotency and rollback; independent verdict; and human evidence when required.

## 15. Definition of done

The objective and tests pass; evidence is complete; no prohibited change occurred; review is accepted; human validation is genuine; controller and Git/GitHub agree; and the next story is unblocked.

## 16. Pause-safe boundaries

Pause before mutation, after each independently reversible operation, after tests, and after durable evidence. Never pause during partial replacement; finish or roll back that atomic operation first.
