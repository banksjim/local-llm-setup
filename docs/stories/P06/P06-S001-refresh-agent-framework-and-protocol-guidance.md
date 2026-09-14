# P06-S001: Refresh agent framework and protocol guidance

| Property | Value |
|---|---|
| Story ID | P06-S001 |
| Phase | P06 — Agent Engineering Foundation |
| Sequence | 1 |
| Status | Planned |
| Step | Research |
| Hold reason | Phase Not Activated |
| Risk | Low |
| Actor | LLM |
| Dependencies | P05-S012 |
| Unlocks | P06-S002 |
| Preferred route | Interface: goagentic through a web-enabled cloud IDE or CLI; Provider: OpenAI or Anthropic with primary-source web access; Model class: current economical research model; Effort: medium; Fallback: current Sol- or Sonnet-class synthesis route when compatibility evidence conflicts. |
| Research freshness | Official framework and protocol docs and releases checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to research current LangChain, LangGraph, MCP, Ollama integration, MLflow tracing, and recommended project structures, so progress is inspectable and independent of chat memory.

## 2. Bounded objective

Research current LangChain, LangGraph, MCP, Ollama integration, MLflow tracing, and recommended project structures.

## 3. Learning objective

Not applicable — this research story prepares the evidence used by the following learning gate and does not teach an owner-operated procedure.

## 4. Current research requirements

Official framework and protocol docs and releases checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not use training memory for changeable facts.

## 5. Preconditions and unlock conditions

P05-S012. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create `docs/research/p06/P06-S001-agent-framework-compatibility-matrix.md` with current LangChain, LangGraph, `langchain-ollama`, MCP Python SDK/protocol, PostgreSQL checkpointer, and MLflow versions; Python requirements; licenses; supported APIs; breaking changes; security notes; and a mutually compatible pinned set. Include official short/deep learning candidates and sanitized evidence under `evidence/P06-S001/`.

## 7. Out of scope and prohibited changes

Do not install packages, run migrations, enable LangSmith or another SaaS, select a memory framework, grant tool authority, copy tutorial code into implementation, or treat popularity as compatibility evidence.

## 8. Privilege and human approval

No privileged authorization is required because this story performs read-only research and writes versioned documentation. Any discovered runtime mutation is routed to a later previewed story.

## 9. Risk rationale

The story changes recommendations but no runtime state; stale or mutually incompatible package claims would misdirect every later P06 story.

## 10. Execution contract

Verify exact upstream repositories and documentation, record release and retrieval dates, distinguish stable from prerelease APIs, build the compatibility matrix, resolve or block conflicting constraints, validate each learning-resource claim, and checkpoint after every technology family.

## 11. Automated acceptance tests

Assert all six technology families are present. Verify every selected package has a current official source, compatible Python range, immutable version constraint, license, breaking-change disposition, and supported integration path. Fail on a prerelease silently selected as stable, unresolved conflict, stale source, missing license, zero rows, or training-memory-only recommendation.

## 12. Human validation

Not applicable — compatibility and source provenance are deterministically reviewable; no owner preference, credential, or experiential judgment is needed.

## 13. Idempotency and rollback

Rerunning refreshes dated matrix rows without duplicates and preserves Git history. Rollback restores only the prior matrix and evidence index; it changes no packages or services.

## 14. Required evidence

Commit the matrix plus `evidence/P06-S001/activation.json`, `source-inventory.json`, `test-results.json`, `rollback.json`, `review.md`, `checkpoint.json`, and an explicit not-applicable human record; include URLs, versions, dates, conflicts, and inferences.

## 15. Definition of done

Every required framework and integration has a current, compatible, licensed disposition; learning resources are current and scoped; no material conflict remains; evidence and review are accepted; and P06-S002 unlocks.

## 16. Pause-safe boundaries

Pause after each source family or conflict decision. Record completed rows, unresolved claims, exact next source, route, model, and provider in `evidence/P06-S001/checkpoint.json`; no runtime mutation can be left partial.
