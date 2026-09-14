# P06-S007: Convert the agent to a durable LangGraph workflow

| Property | Value |
|---|---|
| Story ID | P06-S007 |
| Phase | P06 — Agent Engineering Foundation |
| Sequence | 7 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P06-S006 |
| Unlocks | P06-S008 |
| Preferred route | Interface: goagentic using Codex or Claude Code inside AI-Workbench; Provider: OpenAI or Anthropic with qualified Ollama for bounded iterations; Model class: strong coding/reasoning model; Effort: high; Fallback: current Sol- or Sonnet-class route with cross-provider review. |
| Research freshness | Current LangGraph persistence and durable execution docs checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to add explicit state, checkpoints, bounded retries, interruption, approval node, and recovery, so progress is inspectable and independent of chat memory.

## 2. Bounded objective

Add explicit state, checkpoints, bounded retries, interruption, approval node, and recovery.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P06-S006; this story introduces no separate learning objective.

## 4. Current research requirements

Current LangGraph persistence and durable execution docs checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not use training memory for changeable facts.

## 5. Preconditions and unlock conditions

P06-S006. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create `workloads/agents/foundation/src/local_agents/durable_agent/` with typed graph/state, a dedicated least-privilege P04 PostgreSQL database/role and accepted checkpointer, thread IDs, bounded retry taxonomy, interrupt approval boundary, effect-intent ledger, state migration, and `operations/ubuntu/p06/P06-S007-durable-langgraph-agent`; do not share the Open WebUI or MLflow database identity.

## 7. Out of scope and prohibited changes

Do not add write tools, daemons, arbitrary graphs, unbounded retries, in-memory production persistence, raw secrets, automatic approval, or replayable external effects.

## 8. Privilege and human approval

No new approval is required under P06 authorization. The approval node tests a boundary; any real authority expansion or unpreviewed schema scope requires reauthorization.

## 9. Risk rationale

Persistent state and migrations span agent and PostgreSQL, while replay defects can duplicate effects; failure injection, isolated migration rehearsal, and cross-provider review are required.

## 10. Execution contract

Back up the checkpoint schema; implement contracts; use an isolated namespace; terminate/resume at every node; inject timeout/permanent errors and denial; prove effect deduplication; rehearse migration and restore; repeat apply; and obtain cross-provider review.

## 11. Automated acceptance tests

Assert every node/failure fixture runs. Verify restart resume, concurrent thread isolation, no duplicate intent, bounded retries, terminal failure, denial, stale-resume rejection, redaction, migration round trip, restore checksum, and unchanged authority. Zero-node, in-memory-only, or skipped migration tests fail.

## 12. Human validation

Not applicable — synthetic state, fake effects, deterministic failure injection, and cross-provider review cover behavior without owner credentials.

## 13. Idempotency and rollback

Setup/migrations are repeat-safe. Rollback restores only the dedicated checkpoint schema and durable-agent files, preserving P04 data and P06-S005.

## 14. Required evidence

Commit graph/operation plus `evidence/P06-S007/` activation, diagrams, schemas, migrations, failure/concurrency results, redaction, idempotency, restore proof, checkpoint, and cross-provider review.

## 15. Definition of done

Transitions, restart, denial, retries, deduplication, migration, and restore pass without authority expansion; review resolves; and P06-S008 unlocks.

## 16. Pause-safe boundaries

Pause only before migration, at a committed graph checkpoint, after a test group, or after restore. Never pause mid-migration; record schema/thread state in `evidence/P06-S007/checkpoint.json`.
