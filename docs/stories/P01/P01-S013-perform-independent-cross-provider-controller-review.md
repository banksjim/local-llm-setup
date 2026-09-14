# P01-S013: Perform independent cross-provider controller review

| Property | Value |
|---|---|
| Story ID | P01-S013 |
| Phase | P01 — Program Control and Quality Foundation |
| Sequence | 14 |
| Status | Planned |
| Step | Review |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P01-S012 |
| Unlocks | P01-S014 |
| Preferred route | Fresh cross-provider reviewer selected by goagentic; current model confirmed at activation. |
| Research freshness | Current provider availability checked at activation. |

## 1. User story

As the workstation owner, I want this story to review the controller design, implementation, tests, and threat boundaries in a fresh provider context, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Review the controller design, implementation, tests, and threat boundaries in a fresh provider context.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P01-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current provider availability checked at activation. Record access date, version, direct links, material claims, conflicts, and inferences. Do not rely on model training memory for changeable facts.

## 5. Preconditions and unlock conditions

P01-S012. Applicable specifications, clean Git state, current research, required model route, and the accepted bootstrap-or-controller checks must pass.

## 6. In scope

Only the objective, declared files and services, automated tests, documentation, evidence, and minimum safe supporting changes.

## 7. Out of scope and prohibited changes

Unrelated phase work, unapproved architecture changes, public exposure, secret disclosure, destructive cleanup, and actions not named in this story.

## 8. Privilege and human approval

Not applicable — no separate human action is required beyond active phase authorization.

## 9. Risk rationale

Work affects services, private data, credentials, networking, integration state, or several components; integration evidence and rollback are mandatory. New facts may raise risk; an LLM cannot lower it.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the lease; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the lease; and route to review or human validation. Every finding is resolved or explicitly accepted by the owner with evidence.

## 11. Automated acceptance tests

Every finding is resolved or explicitly accepted by the owner with evidence. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass. A justified not-applicable test is recorded rather than omitted.

## 12. Human validation

Not applicable — automated evidence and independent review are sufficient for this story.

## 13. Idempotency and rollback

A repeat produces an updated or identical evidence record without changing accepted implementation. Rollback is reversion of the story commit or evidence record.

## 14. Required evidence

Story revision; actor, provider/model and effort when applicable; dated sources; changed-file and operation inventory; sanitized outputs; acceptance results; approval; idempotency and rollback; independent verdict; and human evidence when required.

## 15. Definition of done

The objective and tests pass; evidence is complete; no prohibited change occurred; review is accepted; human validation is genuine; controller and Git/GitHub agree; and the next story is unblocked.

## 16. Pause-safe boundaries

Pause before mutation, after each independently reversible operation, after tests, and after durable evidence. Never pause during partial replacement; finish or roll back that atomic operation first.
