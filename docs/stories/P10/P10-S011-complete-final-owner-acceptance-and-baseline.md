# P10-S011: Complete final owner acceptance and baseline

| Property | Value |
|---|---|
| Story ID | P10-S011 |
| Phase | P10 — Operations and Final Acceptance |
| Sequence | 15 |
| Status | Planned |
| Step | Human Validation |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | Human + LLM |
| Dependencies | P10-S010 |
| Unlocks | Not applicable — final planned story. |
| Preferred route | Human through a goagentic-guided checklist with the controller-selected assistant; no unattended substitution. |
| Research freshness | Not applicable — validation uses the completed workstation. |

## 1. User story

As the workstation owner, I want this story to guide daily workflows, incident recovery, update preview, full restore evidence, and zero-context goagentic return, so progress is inspectable and independent of chat memory.

## 2. Bounded objective

Guide daily workflows, incident recovery, update preview, full restore evidence, and zero-context goagentic return.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P10-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Not applicable — validation uses the fixed workstation release candidate and accepted evidence and makes no new product recommendation.

## 5. Preconditions and unlock conditions

P10-S010. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

The objective, declared files or services, tests, documentation, evidence, and minimum safe supporting changes.

## 7. Out of scope and prohibited changes

Unrelated phase work, unapproved redesign, public exposure, secret disclosure, destructive cleanup, and unnamed actions.

## 8. Privilege and human approval

Required — the human performs or validates the work; an LLM cannot create completion evidence.

## 9. Risk rationale

Work crosses a security, privilege, destructive-data, authentication, or acceptance boundary and requires explicit owner control. New facts may raise risk; an LLM cannot lower it.

## 10. Execution contract

Preview, validate, lease, execute reversible units, stop on drift, test, record sanitized evidence, release, and review. Owner accepts the system; final versions and evidence are tagged; future changes begin as new phases and stories.

## 11. Automated acceptance tests

Owner accepts the system; final versions and evidence are tagged; future changes begin as new phases and stories. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks pass; exclusions are justified.

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
