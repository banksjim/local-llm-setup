# P03-S002: Learn local inference, parameters, quantization, and context

| Property | Value |
|---|---|
| Story ID | P03-S002 |
| Phase | P03 — Local Inference and Model Foundation |
| Sequence | 2 |
| Status | Planned |
| Step | Learning |
| Hold reason | Dependency |
| Risk | Low |
| Actor | Human + LLM |
| Dependencies | P03-S001 |
| Unlocks | P03-S003 |
| Preferred route | Human through a goagentic-guided checklist with the controller-selected current assistant model; no unattended substitution. |
| Research freshness | Current P03 research and official Ollama guidance. |

## 1. User story

As the workstation owner, I want this story to teach what B means, how quantization, context, and KV cache affect quality and VRAM, and how to choose a task profile, so that progress is inspectable and independent of chat memory.

## 2. Bounded objective

Teach what B means, how quantization, context, and KV cache affect quality and VRAM, and how to choose a task profile.

## 3. Learning objective

Complete the targeted concepts and demonstrate them through the acceptance exercise.

## 4. Current research requirements

Current P03 research and official Ollama guidance. Record dates, versions, direct links, claims, conflicts, and inferences; do not rely on training memory for changeable facts.

## 5. Preconditions and unlock conditions

P03-S001. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

The objective, declared files or services, tests, documentation, evidence, and minimum safe supporting changes.

## 7. Out of scope and prohibited changes

Unrelated phase work, unapproved redesign, public exposure, secret disclosure, destructive cleanup, and unnamed actions.

## 8. Privilege and human approval

Required — the human performs or validates the work; an LLM cannot create completion evidence.

## 9. Risk rationale

No privileged mutation or user-data risk is expected; output is documentation, research, or learning evidence. New facts may raise risk; an LLM cannot lower it.

## 10. Execution contract

Preview, validate, lease, execute reversible units, stop on drift, test, record sanitized evidence, release, and route to review. The owner completes a sizing exercise and explains why advertised maximum context is not the default.

## 11. Automated acceptance tests

The owner completes a sizing exercise and explains why advertised maximum context is not the default. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks pass; justified exclusions are recorded.

## 12. Human validation

The owner completes the story checklist and records the result through the controller.

## 13. Idempotency and rollback

Repeat updates or reproduces evidence without changing accepted implementation; rollback reverts the story record.

## 14. Required evidence

Story revision; actor and model; dated sources; change inventory; sanitized output; test, approval, idempotency, rollback, review, and human records.

## 15. Definition of done

Objective and tests pass; evidence and review are accepted; human evidence is genuine; no prohibited change occurred; state agrees; next story unlocks.

## 16. Pause-safe boundaries

Pause before mutation and after each reversible unit, tests, and durable evidence. Finish or roll back any atomic replacement before pausing.

