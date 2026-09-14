# P02-S010: Install the approved VS Code extension baseline

| Property | Value |
|---|---|
| Story ID | P02-S010 |
| Phase | P02 — Windows, WSL, Git, and VS Code Foundation |
| Sequence | 10 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Medium |
| Actor | LLM |
| Dependencies | P02-S009 |
| Unlocks | P02-S011 |
| Preferred route | Controller-selected value route; qualified local model allowed after P03; cloud fallback per SYS-CTL. |
| Research freshness | Marketplace and maintainer documentation checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to install and document the minimum extensions for WSL, Git, Python, Go, Node/TypeScript, containers, YAML, Markdown, PowerShell, and later AI work, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Install and document the minimum extensions for WSL, Git, Python, Go, Node/TypeScript, containers, YAML, Markdown, PowerShell, and later AI work.

## 3. Learning objective

Not applicable — a separate preceding learning story covers the major concept, or this story introduces no new owner-operated concept.

## 4. Current research requirements

Marketplace and maintainer documentation checked within 7 days. Record access date, version, direct links, material claims, conflicts, and inferences. Do not rely on model training memory for changeable facts.

## 5. Preconditions and unlock conditions

P02-S009. Applicable specifications, clean Git state, valid controller state, current research, required model route, and lease checks must pass.

## 6. In scope

Only the objective, declared files and services, automated tests, documentation, evidence, and minimum safe supporting changes.

## 7. Out of scope and prohibited changes

Unrelated phase work, unapproved architecture changes, public exposure, secret disclosure, destructive cleanup, and actions not named in this story.

## 8. Privilege and human approval

Not applicable — no separate human action is required beyond active phase authorization.

## 9. Risk rationale

Work changes bounded repository or user-level configuration and is directly reversible from versioned backup. New facts may raise risk; an LLM cannot lower it.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the lease; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the lease; and route to review or human validation. An extension manifest is versioned; each extension has a purpose; conflicts and deprecated choices are absent.

## 11. Automated acceptance tests

An extension manifest is versioned; each extension has a purpose; conflicts and deprecated choices are absent. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass. A justified not-applicable test is recorded rather than omitted.

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

