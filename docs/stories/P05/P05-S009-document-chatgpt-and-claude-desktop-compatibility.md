# P05-S009: Document ChatGPT and Claude desktop compatibility

| Property | Value |
|---|---|
| Story ID | P05-S009 |
| Phase | P05 — Desktop and Development Tool Integrations |
| Sequence | 9 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Low |
| Actor | LLM |
| Dependencies | P05-S008 |
| Unlocks | P05-S010 |
| Preferred route | Controller-selected value route; qualified local model allowed after P03; cloud fallback per SYS-CTL. |
| Research freshness | Current official OpenAI, Anthropic, and Ollama documentation checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to provide accurate setup or limitations for ChatGPT, Codex desktop, Claude Desktop, and Claude Cowork, so that progress is inspectable and independent of chat memory.

## 2. Bounded objective

Provide accurate setup or limitations for ChatGPT, Codex desktop, Claude Desktop, and Claude Cowork.

## 3. Learning objective

Not applicable — a separate learning story covers the major concept, or no new owner-operated concept is introduced.

## 4. Current research requirements

Current official OpenAI, Anthropic, and Ollama documentation checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not rely on training memory for changeable facts.

## 5. Preconditions and unlock conditions

P05-S008. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

The objective, declared files or services, tests, documentation, evidence, and minimum safe supporting changes.

## 7. Out of scope and prohibited changes

Unrelated phase work, unapproved redesign, public exposure, secret disclosure, destructive cleanup, and unnamed actions.

## 8. Privilege and human approval

Not applicable — active phase authorization is sufficient.

## 9. Risk rationale

No privileged mutation or user-data risk is expected; output is documentation, research, or learning evidence. New facts may raise risk; an LLM cannot lower it.

## 10. Execution contract

Preview, validate, lease, execute reversible units, stop on drift, test, record sanitized evidence, release, and route to review. Every claim is sourced; unsupported local-backend claims are rejected with alternatives.

## 11. Automated acceptance tests

Every claim is sourced; unsupported local-backend claims are rejected with alternatives. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks pass; justified exclusions are recorded.

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

