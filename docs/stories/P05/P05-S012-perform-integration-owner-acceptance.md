# P05-S012: Perform integration owner acceptance

| Property | Value |
|---|---|
| Story ID | P05-S012 |
| Phase | P05 — Desktop and Development Tool Integrations |
| Sequence | 12 |
| Status | Planned |
| Step | Human Validation |
| Hold reason | Dependency |
| Risk | High |
| Actor | Human + LLM |
| Dependencies | P05-S011 |
| Unlocks | P06-S001 |
| Preferred route | Human through a goagentic-guided checklist with the controller-selected current assistant model; no unattended substitution. |
| Research freshness | Not applicable — validation is experiential. |

## 1. User story

As the workstation owner, I want this story to have the owner complete normal VS Code, Codex, Claude, Open WebUI, and dictation tasks, so that progress is inspectable and independent of chat memory.

## 2. Bounded objective

Have the owner complete normal VS Code, Codex, Claude, Open WebUI, and dictation tasks.

## 3. Learning objective

Not applicable — a separate learning story covers the major concept, or no new owner-operated concept is introduced.

## 4. Current research requirements

Not applicable — validation is experiential. Record dates, versions, direct links, claims, conflicts, and inferences; do not rely on training memory for changeable facts.

## 5. Preconditions and unlock conditions

P05-S011. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

The objective, declared files or services, tests, documentation, evidence, and minimum safe supporting changes.

## 7. Out of scope and prohibited changes

Unrelated phase work, unapproved redesign, public exposure, secret disclosure, destructive cleanup, and unnamed actions.

## 8. Privilege and human approval

Required — the human performs or validates the work; an LLM cannot create completion evidence.

## 9. Risk rationale

Work affects services, private data, credentials, networking, integration state, or several components; integration evidence and rollback are mandatory. New facts may raise risk; an LLM cannot lower it.

## 10. Execution contract

Preview, validate, lease, execute reversible units, stop on drift, test, record sanitized evidence, release, and route to review. Owner confirms usability and can identify which model and endpoint are active.

## 11. Automated acceptance tests

Owner confirms usability and can identify which model and endpoint are active. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks pass; justified exclusions are recorded.

## 12. Human validation

The owner completes the story checklist and records the result through the controller.

## 13. Idempotency and rollback

Second execution reports no unintended change; rollback restores only story-owned changes and preserves user data.

## 14. Required evidence

Story revision; actor and model; dated sources; change inventory; sanitized output; test, approval, idempotency, rollback, review, and human records.

## 15. Definition of done

Objective and tests pass; evidence and review are accepted; human evidence is genuine; no prohibited change occurred; state agrees; next story unlocks.

## 16. Pause-safe boundaries

Pause before mutation and after each reversible unit, tests, and durable evidence. Finish or roll back any atomic replacement before pausing.
