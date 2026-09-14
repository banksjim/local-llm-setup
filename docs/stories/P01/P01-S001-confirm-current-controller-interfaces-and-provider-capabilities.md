# P01-S001: Confirm current controller interfaces and provider capabilities

| Property | Value |
|---|---|
| Story ID | P01-S001 |
| Phase | P01 — Program Control and Quality Foundation |
| Sequence | 2 |
| Status | Planned |
| Step | Research |
| Hold reason | Dependency |
| Risk | Low |
| Actor | LLM |
| Dependencies | P01-S015 |
| Unlocks | P01-S002 |
| Preferred route | Controller-selected economical research route with web access; architecture model only for unresolved synthesis. |
| Research freshness | Official product documentation and live CLI capability checks no older than 7 days. |

## 1. User story

As the workstation owner, I want this story to produce a dated compatibility record for Codex, Claude Code, PowerShell, WSL, GitHub CLI, GitHub Projects, and available model tiers, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Produce a dated compatibility record for Codex, Claude Code, PowerShell, WSL, GitHub CLI, GitHub Projects, and available model tiers.

## 3. Learning objective

Not applicable — this research story prepares the evidence used by the following learning gate and does not teach an owner-operated procedure.

## 4. Current research requirements

Official product documentation and live CLI capability checks no older than 7 days. Record access date, version, direct links, material claims, conflicts, and inferences. Do not rely on model training memory for changeable facts.

## 5. Preconditions and unlock conditions

P01-S015. Applicable specifications, clean Git state, current research, and the P01 bootstrap-protocol checks must pass.

## 6. In scope

Only the objective, declared files and services, automated tests, documentation, evidence, and minimum safe supporting changes.

## 7. Out of scope and prohibited changes

Unrelated phase work, unapproved architecture changes, public exposure, secret disclosure, destructive cleanup, and actions not named in this story.

## 8. Privilege and human approval

Not applicable — no separate human action is required beyond active phase authorization.

## 9. Risk rationale

No privileged mutation or user-data risk is expected; output is documentation, research, or learning evidence. New facts may raise risk; an LLM cannot lower it.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the lease; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the lease; and route to review or human validation. The record cites current primary documentation, distinguishes verified facts from assumptions, and lists blocking incompatibilities.

## 11. Automated acceptance tests

The record cites current primary documentation, distinguishes verified facts from assumptions, and lists blocking incompatibilities. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass. A justified not-applicable test is recorded rather than omitted.

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
