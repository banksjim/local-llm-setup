# P06-S014: Perform first-agent owner acceptance

| Property | Value |
|---|---|
| Story ID | P06-S014 |
| Phase | P06 — Agent Engineering Foundation |
| Sequence | 14 |
| Status | Planned |
| Step | Human Validation |
| Hold reason | Dependency |
| Risk | High |
| Actor | Human + LLM |
| Dependencies | P06-S013 |
| Unlocks | P07-S001 |
| Preferred route | Human through a goagentic-guided checklist with the controller-selected assistant; no unattended substitution. |
| Research freshness | Not applicable — validation uses the implemented agent. |

## 1. User story

As the workstation owner, I want this story to have the owner inspect code, run the agent, interrupt and resume it, view traces, and reject an unsafe action, so progress is inspectable and independent of chat memory.

## 2. Bounded objective

Have the owner inspect code, run the agent, interrupt and resume it, view traces, and reject an unsafe action.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P06-S011; this story introduces no separate learning objective.

## 4. Current research requirements

Not applicable — validation uses the accepted agent build and recorded dependency versions and makes no new product recommendation.

## 5. Preconditions and unlock conditions

P06-S013. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

The objective, declared files or services, tests, documentation, evidence, and minimum safe supporting changes.

## 7. Out of scope and prohibited changes

Unrelated phase work, unapproved redesign, public exposure, secret disclosure, destructive cleanup, and unnamed actions.

## 8. Privilege and human approval

Required — the human performs or validates the work; an LLM cannot create completion evidence.

## 9. Risk rationale

Work affects services, private data, credentials, networking, or several components; integration evidence and rollback are mandatory. New facts may raise risk; an LLM cannot lower it.

## 10. Execution contract

Preview, validate, lease, execute reversible units, stop on drift, test, record sanitized evidence, release, and review. Owner demonstrates the workflow and records learning completion.

## 11. Automated acceptance tests

Owner demonstrates the workflow and records learning completion. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks pass; exclusions are justified.

## 12. Human validation

Owner completes the story checklist and records it through the controller.

## 13. Idempotency and rollback

Second execution reports no unintended change; rollback restores story-owned changes and preserves user data.

## 14. Required evidence

Story revision; actor and model; dated sources; changes; sanitized output; tests; approvals; idempotency; rollback; review; and human records.

## 15. Definition of done

Objective and tests pass; evidence and review are accepted; genuine human evidence exists when required; state agrees; next story unlocks.

## 16. Pause-safe boundaries

Pause before mutation and after each reversible unit, tests, and durable evidence. Finish or roll back atomic replacement before pausing.
