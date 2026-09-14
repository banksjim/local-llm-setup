# P01-S010: Implement Codex and Claude controller adapters

| Property | Value |
|---|---|
| Story ID | P01-S010 |
| Phase | P01 — Program Control and Quality Foundation |
| Sequence | 11 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P01-S009 |
| Unlocks | P01-S011 |
| Preferred route | Controller-selected quality route; cross-provider review required; qualified local execution only under current policy. |
| Research freshness | Current official Codex skills and Claude Code skills/commands documentation checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to provide provider-independent Codex instructions and Claude Code command skills using the same controller core, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Provide provider-independent Codex instructions and Claude Code command skills using the same controller core. P01 validates portable packages and fixture contracts; live authenticated client validation is explicitly deferred to P05-S007 and P05-S008.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P01-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current official Codex skills and Claude Code skills/commands documentation checked within 7 days. Record access date, version, direct links, material claims, conflicts, and inferences. Do not rely on model training memory for changeable facts.

## 5. Preconditions and unlock conditions

P01-S009. Applicable specifications, clean Git state, current research, required model route, and the accepted bootstrap-or-controller checks must pass.

## 6. In scope

Only the objective, declared files and services, automated tests, documentation, evidence, and minimum safe supporting changes.

## 7. Out of scope and prohibited changes

Unrelated phase work, unapproved architecture changes, public exposure, secret disclosure, destructive cleanup, and actions not named in this story.

## 8. Privilege and human approval

Not applicable — no separate human action is required beyond active phase authorization.

## 9. Risk rationale

Work affects services, private data, credentials, networking, integration state, or several components; integration evidence and rollback are mandatory. New facts may raise risk; an LLM cannot lower it.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the lease; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the lease; and route to review or human validation. Fixture contract tests prove equivalent structured requests and results; they do not claim live client acceptance.

## 11. Automated acceptance tests

Fixture contract tests prove equivalent requests, state, and next-action results from both adapter packages. Live Codex CLI and Claude Code tests are deferred to P05-S007 and P05-S008 and therefore cannot be used to mark Cross-Interface Trusted in P01. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass.

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
