# P06-S003: Create the agent development workspace

| Property | Value |
|---|---|
| Story ID | P06-S003 |
| Phase | P06 — Agent Engineering Foundation |
| Sequence | 3 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Medium |
| Actor | LLM |
| Dependencies | P06-S002 |
| Unlocks | P06-S004 |
| Preferred route | Controller-selected value route; qualified local model allowed after P03; cloud fallback per SYS-CTL. |
| Research freshness | Current Python packaging and selected framework docs checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to create a tested Python-first workspace with pinned dependencies, formatting, typing, tests, configuration, and secret handling, so progress is inspectable and independent of chat memory.

## 2. Bounded objective

Create a tested Python-first workspace with pinned dependencies, formatting, typing, tests, configuration, and secret handling.

## 3. Learning objective

Not applicable — a separate learning story covers the concept, or no owner-operated concept is introduced.

## 4. Current research requirements

Current Python packaging and selected framework docs checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not use training memory for changeable facts.

## 5. Preconditions and unlock conditions

P06-S002. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

The objective, declared files or services, tests, documentation, evidence, and minimum safe supporting changes.

## 7. Out of scope and prohibited changes

Unrelated phase work, unapproved redesign, public exposure, secret disclosure, destructive cleanup, and unnamed actions.

## 8. Privilege and human approval

Not applicable — phase authorization is sufficient.

## 9. Risk rationale

Work changes bounded repository or user-level configuration and is directly reversible. New facts may raise risk; an LLM cannot lower it.

## 10. Execution contract

Preview, validate, lease, execute reversible units, stop on drift, test, record sanitized evidence, release, and review. Clean setup and repeat setup pass; a smoke test runs in Ubuntu.

## 11. Automated acceptance tests

Clean setup and repeat setup pass; a smoke test runs in Ubuntu. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks pass; exclusions are justified.

## 12. Human validation

Not applicable — automated evidence and independent review suffice.

## 13. Idempotency and rollback

Second execution reports no unintended change; rollback restores story-owned changes and preserves user data.

## 14. Required evidence

Story revision; actor and model; dated sources; changes; sanitized output; tests; approvals; idempotency; rollback; review; and human records.

## 15. Definition of done

Objective and tests pass; evidence and review are accepted; genuine human evidence exists when required; state agrees; next story unlocks.

## 16. Pause-safe boundaries

Pause before mutation and after each reversible unit, tests, and durable evidence. Finish or roll back atomic replacement before pausing.

