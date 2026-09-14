# P06-S005: Build the first bounded LangChain tool agent

| Property | Value |
|---|---|
| Story ID | P06-S005 |
| Phase | P06 — Agent Engineering Foundation |
| Sequence | 5 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Medium |
| Actor | LLM |
| Dependencies | P06-S004 |
| Unlocks | P06-S006 |
| Preferred route | Interface: goagentic using Codex or Claude Code inside AI-Workbench; Provider: qualified Ollama model with OpenAI or Anthropic fallback; Model class: economical coding/tool-use model; Effort: medium; Fallback: current Terra- or Sonnet-class implementation route plus independent review. |
| Research freshness | Current LangChain and Ollama integration docs checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to build a read-only agent using a qualified local model and deterministic tool with structured results, so progress is inspectable and independent of chat memory.

## 2. Bounded objective

Build a read-only agent using a qualified local model and deterministic tool with structured results.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P06-S004; this story introduces no separate learning objective.

## 4. Current research requirements

Current LangChain and Ollama integration docs checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not use training memory for changeable facts.

## 5. Preconditions and unlock conditions

P06-S004. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Implement `workloads/agents/foundation/src/local_agents/read_only_agent/` with typed I/O, current LangChain API, P03 model adapter, provider identity, and one `lookup_fixture` tool restricted to `tests/fixtures/read-only/`; add `operations/ubuntu/p06/P06-S005-build-first-agent`.

## 7. Out of scope and prohibited changes

Do not add shell, arbitrary paths/URLs, write/delete tools, private data, memory, RAG, MCP, hidden fallback, background loops, or IDE-inherited authority.

## 8. Privilege and human approval

No new approval is required under the unchanged P06 authorization. A new tool, root, destination, credential, or mutation stops for a revised preview.

## 9. Risk rationale

The agent chooses whether to invoke code, but the sole tool is read-only, schema-bound, fixture-rooted, and repository changes are reversible.

## 10. Execution contract

Validate model qualification; implement schemas, adapter, allowlisted resolution, size/time limits, errors, provider disclosure, and CLI; inject traversal, symlink, malformed, oversized, timeout, missing-model, mutation, and hidden-fallback failures; repeat and review.

## 11. Automated acceptance tests

Assert positive and negative fixtures. Verify correct tool result/citation; reject traversal, absolute paths, symlink escape, invalid schema, oversized output, and mutation; bound retry/timeout; expose identity; fail instead of silently switching. Run deterministic and qualified-local tests; zero fixtures fail.

## 12. Human validation

Not applicable — deterministic fixtures, live model qualification, and independent review cover this nonpersonal read-only agent.

## 13. Idempotency and rollback

Runs are read-only and repeatable; setup is no-op on second apply. Rollback removes only the package/operation or restores Git and preserves the shared workspace and other fixtures.

## 14. Required evidence

Commit agent/operation plus `evidence/P06-S005/` activation, qualification reference, schemas, authority inventory, tests, identity, idempotency, rollback, checkpoint, and review.

## 15. Definition of done

The bounded task succeeds with only the declared tool, every escape/mutation/fallback case fails closed, quality meets threshold, review resolves, and P06-S006 unlocks.

## 16. Pause-safe boundaries

Pause after schema, adapter, tool, deterministic tests, live tests, or rollback. Finish atomic lock/package changes and record the next command in `evidence/P06-S005/checkpoint.json`.
