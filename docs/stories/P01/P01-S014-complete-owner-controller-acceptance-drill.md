# P01-S014: Complete owner controller acceptance drill

| Property | Value |
|---|---|
| Story ID | P01-S014 |
| Phase | P01 — Program Control and Quality Foundation |
| Sequence | 14 |
| Status | Planned |
| Step | Human Validation |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | Human + LLM |
| Dependencies | P01-S013 |
| Unlocks | P02-S001 |
| Preferred route | Human through a goagentic-guided checklist with the controller-selected current assistant model; no unattended substitution. |
| Research freshness | Not applicable — acceptance uses the built controller and approved specification. |

## 1. User story

As the workstation owner, I want this story to guide the owner through zero-context start, lesson, execution, pause, restart, resume, review, rejection, and completion, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Guide the owner through zero-context start, lesson, execution, pause, restart, resume, review, rejection, and completion.

## 3. Learning objective

Not applicable — a separate preceding learning story covers the major concept, or this story introduces no new owner-operated concept.

## 4. Current research requirements

Not applicable — acceptance uses the built controller and approved specification. Record access date, version, direct links, material claims, conflicts, and inferences. Do not rely on model training memory for changeable facts.

## 5. Preconditions and unlock conditions

P01-S013. Applicable specifications, clean Git state, valid controller state, current research, required model route, and lease checks must pass.

## 6. In scope

Only the objective, declared files and services, automated tests, documentation, evidence, and minimum safe supporting changes.

## 7. Out of scope and prohibited changes

Unrelated phase work, unapproved architecture changes, public exposure, secret disclosure, destructive cleanup, and actions not named in this story.

## 8. Privilege and human approval

Required — the human performs or validates the declared work; an LLM may guide but cannot create completion evidence.

## 9. Risk rationale

Work crosses a security, privilege, destructive-data, authentication, or program-acceptance boundary and requires explicit owner control. New facts may raise risk; an LLM cannot lower it.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the lease; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the lease; and route to review or human validation. The owner completes every step without relying on this chat; the accepted baseline is tagged Controller Core Trusted.

## 11. Automated acceptance tests

The owner completes every step without relying on this chat; the accepted baseline is tagged Controller Core Trusted. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass. A justified not-applicable test is recorded rather than omitted.

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
