# P06-S002: Learn agent fundamentals and tool safety

| Property | Value |
|---|---|
| Story ID | P06-S002 |
| Phase | P06 — Agent Engineering Foundation |
| Sequence | 2 |
| Status | Planned |
| Step | Learning |
| Hold reason | Dependency |
| Risk | Low |
| Actor | Human + LLM |
| Dependencies | P06-S001 |
| Unlocks | P06-S003 |
| Preferred route | Interface: goagentic guided lesson in the owner's cloud IDE or CLI; Provider: OpenAI or Anthropic; Model class: economical teaching model with strong tool-safety reasoning; Effort: medium; Fallback: current Sol- or Sonnet-class tutor, never an unqualified local model. |
| Research freshness | Current P06 research record. |

## 1. User story

As the workstation owner, I want this story to teach model versus agent, loop, tools, state, permissions, structured output, failures, and human oversight, so progress is inspectable and independent of chat memory.

## 2. Bounded objective

Teach model versus agent, loop, tools, state, permissions, structured output, failures, and human oversight.

## 3. Learning objective

Complete the targeted concepts and demonstrate them through the acceptance exercise.

## 4. Current research requirements

Current P06 research record. Record dates, versions, direct links, claims, conflicts, and inferences; do not use training memory for changeable facts.

## 5. Preconditions and unlock conditions

P06-S001. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create `docs/learning/p06/P06-S002-agent-fundamentals-and-tool-safety.md`, a bounded-agent diagram, authority worksheet, prompt-injection and failure scenarios, vetted short/deep learning resources, and a blank owner rubric under `evidence/P06-S002/`.

## 7. Out of scope and prohibited changes

Do not teach framework APIs, build an agent, request credentials, grant live tools, access private data, or use an LLM answer as owner evidence.

## 8. Privilege and human approval

No privileged authorization is required. The owner completes the lesson and explain-back personally; this is participation, not permission for later implementation.

## 9. Risk rationale

The lesson changes no system state, but misunderstanding authority, state, or oversight would make later agent work unsafe and blocks progression.

## 10. Execution contract

Generate the lesson from P06-S001 sources; teach in short modules; require the owner to diagram model, loop, tool, state, permission, and human gate; run two authority scenarios; collect an owner-authored explain-back; score only against the published rubric; and checkpoint each module.

## 11. Automated acceptance tests

Assert the lesson, diagram, two scenarios, and blank rubric exist. Verify freshness and rubric coverage, blank answers before handoff, and genuine owner text afterward. Fail on zero exercises, answer leakage, live-tool execution, or an LLM-authored response.

## 12. Human validation

The owner completes the diagram and scenarios, explains why tool access is authority, identifies the unsafe expansion, and writes `evidence/P06-S002/human-validation.md`. The LLM cannot author or replace the response.

## 13. Idempotency and rollback

Repeating creates a dated attempt without overwriting accepted owner evidence. Rollback removes only an unaccepted lesson revision or attempt.

## 14. Required evidence

Commit the lesson, sources, diagram, scenarios, blank rubric, test results, genuine `evidence/P06-S002/human-validation.md`, activation, rollback, checkpoint, and review records.

## 15. Definition of done

The owner meets every rubric item without answer substitution, the sources and evidence pass review, and P06-S003 unlocks.

## 16. Pause-safe boundaries

Pause between modules or before handoff. Record completed modules, packet state, next prompt, model, and provider in `evidence/P06-S002/checkpoint.json`.
