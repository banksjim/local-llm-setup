# P03-S004: Configure the WSL inference-only gateway

| Property | Value |
|---|---|
| Story ID | P03-S004 |
| Phase | P03 — Local Inference and Model Foundation |
| Sequence | 4 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | Human + LLM |
| Dependencies | P03-S003 |
| Unlocks | P03-S005 |
| Preferred route | Human through a goagentic-guided checklist with the controller-selected current assistant model; no unattended substitution. |
| Research freshness | Current Ollama APIs, Windows Firewall, and WSL networking checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to expose only required inference and read routes from Ubuntu through a dedicated port and WSL-subnet firewall rule, so that progress is inspectable and independent of chat memory.

## 2. Bounded objective

Expose only required inference and read routes from Ubuntu through a dedicated port and WSL-subnet firewall rule.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P03-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current Ollama APIs, Windows Firewall, and WSL networking checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not rely on training memory for changeable facts.

## 5. Preconditions and unlock conditions

P03-S003. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

The objective, declared files or services, tests, documentation, evidence, and minimum safe supporting changes.

## 7. Out of scope and prohibited changes

Unrelated phase work, unapproved redesign, public exposure, secret disclosure, destructive cleanup, and unnamed actions.

## 8. Privilege and human approval

Required — the human performs or validates the work; an LLM cannot create completion evidence.

## 9. Risk rationale

Work crosses a security, privilege, destructive-data, authentication, or program-acceptance boundary and requires explicit owner control. New facts may raise risk; an LLM cannot lower it.

## 10. Execution contract

Preview, validate, lease, execute reversible units, stop on drift, test, record sanitized evidence, release, and route to review. Allowed inference works; administration, LAN access, and direct Ollama access fail; firewall rollback is proven.

## 11. Automated acceptance tests

Allowed inference works; administration, LAN access, and direct Ollama access fail; firewall rollback is proven. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks pass; justified exclusions are recorded.

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
