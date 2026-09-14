# P03-S001: Research current Ollama and local model landscape

| Property | Value |
|---|---|
| Story ID | P03-S001 |
| Phase | P03 — Local Inference and Model Foundation |
| Sequence | 1 |
| Status | Planned |
| Step | Research |
| Hold reason | Phase Not Activated |
| Risk | Low |
| Actor | LLM |
| Dependencies | P02-S012 |
| Unlocks | P03-S002 |
| Preferred route | Interface: goagentic through a web-enabled cloud IDE or CLI; Provider: OpenAI or Anthropic with primary-source web access; Model class: current economical research model; Effort: medium; Fallback: current Sol or Sonnet-class synthesis route when sources conflict. |
| Research freshness | Official Ollama and model-publisher sources plus reproducible community benchmarks checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to re-evaluate Ollama releases, licenses, model tags, quantizations, embeddings, vision and tool support, and 24 GB VRAM candidates, so that progress is inspectable and independent of chat memory.

## 2. Bounded objective

Re-evaluate Ollama releases, licenses, model tags, quantizations, embeddings, vision and tool support, and 24 GB VRAM candidates.

## 3. Learning objective

Not applicable — this research story prepares the evidence used by the following learning gate and does not teach an owner-operated procedure.

## 4. Current research requirements

Official Ollama and model-publisher sources plus reproducible community benchmarks checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not rely on training memory for changeable facts.

## 5. Preconditions and unlock conditions

P02-S012. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create and verify the dated candidate matrix, raw source snapshot, license and digest table, and unresolved-conflict register; Ollama and model storage remain read-only. Store versioned implementation or guidance at the story-owned output path already named by this contract and sanitized run evidence under evidence/P03-S001/.

## 7. Out of scope and prohibited changes

Do not install containers or desktop clients, expose Ollama to the LAN, delete existing models, change BIOS or GPU drivers, accept floating model tags, or route unqualified controller work to a local model.

## 8. Privilege and human approval

No privileged authorization is required because P03-S001 performs source research and versioned documentation only; discovery of a required mutation creates or reroutes to a separately previewed story.

## 9. Risk rationale

Research may change model recommendations but mutates only versioned evidence; stale or conflicting claims block readiness.

## 10. Execution contract

Create an activation packet; verify dependencies, freshness, and targets; preview the exact change; confirm revision-bound phase authorization where mutation is privileged; acquire the controller lease; produce docs/research/p03/P03-S001-research-current-ollama-and-local-model-landscape-matrix.md; run the named positive and negative checks; record sanitized evidence; release the lease. Acceptance criterion: the matrix contains release date, immutable tag or digest, download size, license, modalities, tool support, context claim, 24 GB fit estimate, and source URL for every candidate; at least one non-Qwen challenger is evaluated.

## 11. Automated acceptance tests

Assert the expected story inventory is nonzero, then verify that the matrix contains release date, immutable tag or digest, download size, license, modalities, tool support, context claim, 24 GB fit estimate, and source URL for every candidate; at least one non-Qwen challenger is evaluated. Fail on missing evidence, unexpected targets, secrets, stale sources, an untested negative boundary, or a validator that matched zero fixtures.

## 12. Human validation

Not applicable — P03-S001 is accepted through deterministic checks plus an independent review; no experiential or credential-bearing action is delegated to the LLM.

## 13. Idempotency and rollback

A repeat run refreshes docs/research/p03/P03-S001-research-current-ollama-and-local-model-landscape-matrix.md without duplicate records. Rollback restores its pre-story Git version and removes only unaccepted evidence/P03-S001/ evidence.

## 14. Required evidence

Commit docs/research/p03/P03-S001-research-current-ollama-and-local-model-landscape-matrix.md or its versioned result plus evidence/P03-S001/activation.json, evidence/P03-S001/change-inventory.json, evidence/P03-S001/test-results.json, evidence/P03-S001/rollback.json, and evidence/P03-S001/review.md; include exact versions or digests, sanitized commands or observations, timestamps, and an explicit not-applicable human record.

## 15. Definition of done

P03-S001 is Done only when the matrix contains release date, immutable tag or digest, download size, license, modalities, tool support, context claim, 24 GB fit estimate, and source URL for every candidate; at least one non-Qwen challenger is evaluated; the story-owned output and evidence inventory exist, independent review has no unresolved material finding, rollback and idempotency evidence is accepted, and controller state unlocks the declared next story.

## 16. Pause-safe boundaries

Pause after the activation packet, after each download, install, configuration backup, or other atomic unit, after tests, and after evidence is committed. Before pausing, finish or roll back the active unit and record the exact next command plus current model and provider in evidence/P03-S001/checkpoint.json.
