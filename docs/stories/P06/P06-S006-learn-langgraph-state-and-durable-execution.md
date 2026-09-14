# P06-S006: Learn LangGraph state and durable execution

| Property | Value |
|---|---|
| Story ID | P06-S006 |
| Phase | P06 — Agent Engineering Foundation |
| Sequence | 6 |
| Status | Planned |
| Step | Learning |
| Hold reason | Dependency |
| Risk | Low |
| Actor | Human + LLM |
| Dependencies | P06-S005 |
| Unlocks | P06-S007 |
| Preferred route | Interface: goagentic lesson in the P06 VS Code/WSL workspace; Provider: qualified Ollama model with OpenAI or Anthropic fallback; Model class: economical reasoning tutor; Effort: medium; Fallback: current Sol- or Sonnet-class tutor. |
| Research freshness | Current official LangGraph tutorials selected at activation. |

## 1. User story

As the workstation owner, I want this story to teach graphs, nodes, edges, checkpoints, interrupts, retries, and human-in-the-loop, so progress is inspectable and independent of chat memory.

## 2. Bounded objective

Teach graphs, nodes, edges, checkpoints, interrupts, retries, and human-in-the-loop.

## 3. Learning objective

Complete the targeted concepts and demonstrate them through the acceptance exercise.

## 4. Current research requirements

Current official LangGraph tutorials selected at activation. Record dates, versions, direct links, claims, conflicts, and inferences; do not use training memory for changeable facts.

## 5. Preconditions and unlock conditions

P06-S005. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create `docs/learning/p06/P06-S006-langgraph-durable-execution.md` and `workloads/agents/foundation/learning/langgraph/` covering typed state, nodes, edges, thread IDs, durable checkpoints, interrupts, resume, retries, replay, idempotent effects, and schema migration.

## 7. Out of scope and prohibited changes

Do not deploy production, accept in-memory persistence as restart proof, perform a real side effect, enable cloud tracing, expose private state, or let replay repeat a mutation.

## 8. Privilege and human approval

No new authorization is required. The owner runs, interrupts, terminates, resumes, and explains the tutorial personally; the LLM cannot create those observations.

## 9. Risk rationale

Disposable state is used, but misunderstanding replay and effects could cause duplicate real actions later.

## 10. Execution contract

Use accepted LangGraph APIs; run with a durable disposable checkpointer and thread ID; interrupt, terminate, resume, inject transient/permanent failures, replay with a fake effect ledger, migrate one fixture state, and collect explain-back.

## 11. Automated acceptance tests

Assert transition/failure fixtures. Verify process-death resume, thread isolation, JSON-safe interrupt, denial, bounded retry, permanent stop, no duplicate effect, and state migration. Fail on in-memory-only proof, secret-bearing interrupt, repeated effect, prefilled answers, or zero fixtures.

## 12. Human validation

The owner predicts transitions, resumes after process termination, denies one action, explains checkpoint versus durable memory and replay risk, and writes `evidence/P06-S006/human-validation.md`. The LLM cannot author it.

## 13. Idempotency and rollback

Each run uses a disposable thread namespace and reset. Rollback drops only that namespace/tutorial and preserves P04 data and the first agent.

## 14. Required evidence

Commit lesson/tutorial plus `evidence/P06-S006/` activation, transitions, resume/replay results, rubric, genuine human record, cleanup, rollback, checkpoint, and review.

## 15. Definition of done

Durable state, interrupt, retry, replay, and migration cases pass; owner meets the rubric; evidence resolves; and P06-S007 unlocks.

## 16. Pause-safe boundaries

Pause only at graph checkpoints, after cleanup, or before handoff; record thread/checkpoint ID, next node, model, provider, and command in `evidence/P06-S006/checkpoint.json`.
