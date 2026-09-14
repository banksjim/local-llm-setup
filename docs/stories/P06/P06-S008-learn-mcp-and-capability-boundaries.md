# P06-S008: Learn MCP and capability boundaries

| Property | Value |
|---|---|
| Story ID | P06-S008 |
| Phase | P06 — Agent Engineering Foundation |
| Sequence | 8 |
| Status | Planned |
| Step | Learning |
| Hold reason | Dependency |
| Risk | Low |
| Actor | Human + LLM |
| Dependencies | P06-S007 |
| Unlocks | P06-S009 |
| Preferred route | Human through a goagentic-guided checklist with the controller-selected assistant; no unattended substitution. |
| Research freshness | Current official MCP specification and security guidance checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to teach MCP servers, clients, tools, resources, trust, schemas, credentials, and prompt-injection boundaries, so progress is inspectable and independent of chat memory.

## 2. Bounded objective

Teach MCP servers, clients, tools, resources, trust, schemas, credentials, and prompt-injection boundaries.

## 3. Learning objective

Complete the targeted concepts and demonstrate them through the acceptance exercise.

## 4. Current research requirements

Current official MCP specification and security guidance checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not use training memory for changeable facts.

## 5. Preconditions and unlock conditions

P06-S007. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

The objective, declared files or services, tests, documentation, evidence, and minimum safe supporting changes.

## 7. Out of scope and prohibited changes

Unrelated phase work, unapproved redesign, public exposure, secret disclosure, destructive cleanup, and unnamed actions.

## 8. Privilege and human approval

Required — the human performs or validates the work; an LLM cannot create completion evidence.

## 9. Risk rationale

No privileged mutation or user-data risk is expected. New facts may raise risk; an LLM cannot lower it.

## 10. Execution contract

Preview, validate, lease, execute reversible units, stop on drift, test, record sanitized evidence, release, and review. Owner inspects a tool manifest and identifies minimum authority.

## 11. Automated acceptance tests

Owner inspects a tool manifest and identifies minimum authority. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks pass; exclusions are justified.

## 12. Human validation

Owner completes the story checklist and records it through the controller.

## 13. Idempotency and rollback

Repeat updates or reproduces evidence without changing accepted implementation; rollback reverts the story record.

## 14. Required evidence

Story revision; actor and model; dated sources; changes; sanitized output; tests; approvals; idempotency; rollback; review; and human records.

## 15. Definition of done

Objective and tests pass; evidence and review are accepted; genuine human evidence exists when required; state agrees; next story unlocks.

## 16. Pause-safe boundaries

Pause before mutation and after each reversible unit, tests, and durable evidence. Finish or roll back atomic replacement before pausing.

