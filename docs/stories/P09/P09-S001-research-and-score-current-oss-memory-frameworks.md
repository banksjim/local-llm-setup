# P09-S001: Research and score current OSS memory frameworks

| Property | Value |
|---|---|
| Story ID | P09-S001 |
| Phase | P09 — Durable Agent Memory |
| Sequence | 1 |
| Status | Planned |
| Step | Research |
| Hold reason | Phase Not Activated |
| Risk | Medium |
| Actor | LLM |
| Dependencies | P08-S010 |
| Unlocks | P09-S002 |
| Preferred route | Controller-selected economical research route with web access. |
| Research freshness | Official repositories, docs, releases, issues, licenses, and security advisories checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to evaluate current Mem0, Letta, Zep community options, LangGraph components, and credible new GitHub projects against SYS-MEM, so progress is inspectable and independent of chat memory.

## 2. Bounded objective

Evaluate current Mem0, Letta, Zep community options, LangGraph components, and credible new GitHub projects against SYS-MEM.

## 3. Learning objective

Not applicable — a separate learning story covers the concept, or no owner-operated concept is introduced.

## 4. Current research requirements

Official repositories, docs, releases, issues, licenses, and security advisories checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not use training memory for changeable facts.

## 5. Preconditions and unlock conditions

P08-S010. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

The objective, declared files or services, tests, documentation, evidence, and minimum safe supporting changes.

## 7. Out of scope and prohibited changes

Unrelated phase work, unapproved redesign, public exposure, secret disclosure, destructive cleanup, and unnamed actions.

## 8. Privilege and human approval

Not applicable — phase authorization is sufficient.

## 9. Risk rationale

Work changes bounded repository or user-level configuration and is directly reversible. New facts may raise risk; an LLM cannot lower it.

## 10. Execution contract

Preview, validate, lease, execute reversible units, stop on drift, test, record sanitized evidence, release, and review. A reproducible scorecard covers license, self-hosting, integration, provenance, review, security, portability, and maintenance.

## 11. Automated acceptance tests

A reproducible scorecard covers license, self-hosting, integration, provenance, review, security, portability, and maintenance. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks pass; exclusions are justified.

## 12. Human validation

Not applicable — automated evidence and independent review suffice.

## 13. Idempotency and rollback

Repeat updates or reproduces evidence without changing accepted implementation; rollback reverts the story record.

## 14. Required evidence

Story revision; actor and model; dated sources; changes; sanitized output; tests; approvals; idempotency; rollback; review; and human records.

## 15. Definition of done

Objective and tests pass; evidence and review are accepted; genuine human evidence exists when required; state agrees; next story unlocks.

## 16. Pause-safe boundaries

Pause before mutation and after each reversible unit, tests, and durable evidence. Finish or roll back atomic replacement before pausing.
