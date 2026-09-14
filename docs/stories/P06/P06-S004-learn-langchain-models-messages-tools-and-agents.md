# P06-S004: Learn LangChain models, messages, tools, and agents

| Property | Value |
|---|---|
| Story ID | P06-S004 |
| Phase | P06 — Agent Engineering Foundation |
| Sequence | 4 |
| Status | Planned |
| Step | Learning |
| Hold reason | Dependency |
| Risk | Low |
| Actor | Human + LLM |
| Dependencies | P06-S003 |
| Unlocks | P06-S005 |
| Preferred route | Interface: goagentic lesson in the P06 VS Code/WSL workspace; Provider: qualified Ollama model with OpenAI or Anthropic teaching fallback; Model class: economical tool-capable model; Effort: medium; Fallback: current Sol- or Sonnet-class tutor. |
| Research freshness | Current official LangChain tutorials selected at activation. |

## 1. User story

As the workstation owner, I want this story to teach only the LangChain abstractions needed to build the first agent, so progress is inspectable and independent of chat memory.

## 2. Bounded objective

Teach only the LangChain abstractions needed to build the first agent.

## 3. Learning objective

Complete the targeted concepts and demonstrate them through the acceptance exercise.

## 4. Current research requirements

Current official LangChain tutorials selected at activation. Record dates, versions, direct links, claims, conflicts, and inferences; do not use training memory for changeable facts.

## 5. Preconditions and unlock conditions

P06-S003. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create `docs/learning/p06/P06-S004-langchain-foundations.md` and `workloads/agents/foundation/learning/langchain/` covering current model calls, messages, structured output, tool schemas and call IDs, agent loops, provider swapping, timeouts, and errors with one deterministic read-only fixture tool.

## 7. Out of scope and prohibited changes

Do not teach obsolete chain APIs, enable LangSmith, call shell/arbitrary network tools, use private data, mutate the main agent, hide provider identity, or treat the tutorial as production.

## 8. Privilege and human approval

No new authorization is required. The owner runs the tutorial and explain-back personally; the LLM cannot prefill the exercise or owner record.

## 9. Risk rationale

Only disposable fixtures are used, but misunderstanding tool schemas or provider behavior would compromise the first real agent.

## 10. Execution contract

Build from accepted APIs; run a direct call, structured response, and tool call; switch local and mocked/cloud adapters without changing business logic; demonstrate invalid schema and timeout handling; collect owner explain-back; and checkpoint.

## 11. Automated acceptance tests

Assert nonzero tutorial tests and blank questions. Verify current imports, deterministic result, schema validation, matching call ID, invalid-argument rejection, timeout, provider identity, and fixture-only authority. Fail on obsolete APIs, answer substitution, zero tests, or hidden fallback.

## 12. Human validation

The owner runs the tutorial, predicts the sequence, repairs one invalid argument, explains model versus agent and the provider boundary, and writes `evidence/P06-S004/human-validation.md`. The LLM cannot author the answers.

## 13. Idempotency and rollback

The tutorial resets its fixture and repeats deterministically. Rollback removes only tutorial outputs/files and preserves the foundation workspace.

## 14. Required evidence

Commit lesson/tutorial plus `evidence/P06-S004/` activation, sources, tests, provider trace, blank rubric, genuine human record, rollback, checkpoint, and review.

## 15. Definition of done

All behaviors and denial cases pass on accepted APIs, the owner meets the rubric without substitution, evidence resolves, and P06-S005 unlocks.

## 16. Pause-safe boundaries

Pause between modules, after fixture reset, or before handoff; record exercise state and next action in `evidence/P06-S004/checkpoint.json`.
