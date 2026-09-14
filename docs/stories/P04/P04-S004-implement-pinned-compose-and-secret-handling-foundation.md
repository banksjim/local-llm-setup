# P04-S004: Implement pinned Compose and secret handling foundation

| Property | Value |
|---|---|
| Story ID | P04-S004 |
| Phase | P04 — Open WebUI and Supporting AI Services |
| Sequence | 4 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P04-S003 |
| Unlocks | P04-S005 |
| Preferred route | Controller-selected quality route; cross-provider review required; qualified local execution only under current policy. |
| Research freshness | Current Compose specification and image documentation checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to create versioned Compose, environment templates, private network, health checks, volumes, and secret boundaries, so that progress is inspectable and independent of chat memory.

## 2. Bounded objective

Create versioned Compose, environment templates, private network, health checks, volumes, and secret boundaries.

## 3. Learning objective

Not applicable — a separate learning story covers the major concept, or no new owner-operated concept is introduced.

## 4. Current research requirements

Current Compose specification and image documentation checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not rely on training memory for changeable facts.

## 5. Preconditions and unlock conditions

P04-S003. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

The objective, declared files or services, tests, documentation, evidence, and minimum safe supporting changes.

## 7. Out of scope and prohibited changes

Unrelated phase work, unapproved redesign, public exposure, secret disclosure, destructive cleanup, and unnamed actions.

## 8. Privilege and human approval

Not applicable — active phase authorization is sufficient.

## 9. Risk rationale

Work affects services, private data, credentials, networking, integration state, or several components; integration evidence and rollback are mandatory. New facts may raise risk; an LLM cannot lower it.

## 10. Execution contract

Preview, validate, lease, execute reversible units, stop on drift, test, record sanitized evidence, release, and route to review. Compose and secret scans pass; no floating tags or public listeners exist.

## 11. Automated acceptance tests

Compose and secret scans pass; no floating tags or public listeners exist. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks pass; justified exclusions are recorded.

## 12. Human validation

Not applicable — automated evidence and independent review are sufficient.

## 13. Idempotency and rollback

Second execution reports no unintended change; rollback restores only story-owned changes and preserves user data.

## 14. Required evidence

Story revision; actor and model; dated sources; change inventory; sanitized output; test, approval, idempotency, rollback, review, and human records.

## 15. Definition of done

Objective and tests pass; evidence and review are accepted; human evidence is genuine; no prohibited change occurred; state agrees; next story unlocks.

## 16. Pause-safe boundaries

Pause before mutation and after each reversible unit, tests, and durable evidence. Finish or roll back any atomic replacement before pausing.

