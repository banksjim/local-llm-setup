# P06-S009: Build and integrate one local MCP server

| Property | Value |
|---|---|
| Story ID | P06-S009 |
| Phase | P06 — Agent Engineering Foundation |
| Sequence | 9 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P06-S008 |
| Unlocks | P06-S010 |
| Preferred route | Controller-selected quality route with cross-provider review; local use only under current qualification policy. |
| Research freshness | Current MCP SDK and client documentation checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to implement a narrow read-only MCP capability with schemas, tests, logs, and denial controls, so progress is inspectable and independent of chat memory.

## 2. Bounded objective

Implement a narrow read-only MCP capability with schemas, tests, logs, and denial controls.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P06-S008; this story introduces no separate learning objective.

## 4. Current research requirements

Current MCP SDK and client documentation checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not use training memory for changeable facts.

## 5. Preconditions and unlock conditions

P06-S008. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

The objective, declared files or services, tests, documentation, evidence, and minimum safe supporting changes.

## 7. Out of scope and prohibited changes

Unrelated phase work, unapproved redesign, public exposure, secret disclosure, destructive cleanup, and unnamed actions.

## 8. Privilege and human approval

Not applicable — phase authorization is sufficient.

## 9. Risk rationale

Work affects services, private data, credentials, networking, or several components; integration evidence and rollback are mandatory. New facts may raise risk; an LLM cannot lower it.

## 10. Execution contract

Preview, validate, lease, execute reversible units, stop on drift, test, record sanitized evidence, release, and review. Codex, Claude, or the agent can call it; malformed and unauthorized requests fail closed.

## 11. Automated acceptance tests

Codex, Claude, or the agent can call it; malformed and unauthorized requests fail closed. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks pass; exclusions are justified.

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
