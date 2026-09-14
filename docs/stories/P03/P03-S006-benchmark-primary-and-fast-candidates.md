# P03-S006: Benchmark primary and fast candidates

| Property | Value |
|---|---|
| Story ID | P03-S006 |
| Phase | P03 — Local Inference and Model Foundation |
| Sequence | 6 |
| Status | Planned |
| Step | Testing |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P03-S005 |
| Unlocks | P03-S007 |
| Preferred route | Interface: goagentic in the designated cloud IDE or CLI; Provider: OpenAI or Anthropic, different from the implementer for acceptance review; Model class: current quality or review model; Effort: high; Fallback: stop and switch to the current Sol or Sonnet-class route; qualified local models remain advisory during probation. |
| Research freshness | Benchmark methodology and current model cards checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to measure quality, latency, throughput, VRAM, RAM spill, cold start, context, vision, tools, and concurrency on the RTX 4090, so that progress is inspectable and independent of chat memory.

## 2. Bounded objective

Measure quality, latency, throughput, VRAM, RAM spill, cold start, context, vision, tools, and concurrency on the RTX 4090.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P03-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Benchmark methodology and current model cards checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not rely on training memory for changeable facts.

## 5. Preconditions and unlock conditions

P03-S005. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create and verify frozen text, code, tool, vision, and concurrency prompt corpus; Ollama benchmark runner; NVIDIA and system telemetry capture; and normalized result report under H:\ai\benchmarks. Store versioned implementation or guidance at the story-owned output path already named by this contract and sanitized run evidence under evidence/P03-S006/.

## 7. Out of scope and prohibited changes

Do not install containers or desktop clients, expose Ollama to the LAN, delete existing models, change BIOS or GPU drivers, accept floating model tags, or route unqualified controller work to a local model.

## 8. Privilege and human approval

No new approval is required while the revision-bound P03 phase authorization still matches the work. The LLM may execute only the previewed story-owned operations; any changed target, network boundary, data class, risk, or destructive action stops for a new preview.

## 9. Risk rationale

Sustained GPU and RAM load can destabilize desktop workloads, and a flawed corpus could select the wrong default.

## 10. Execution contract

Create an activation packet; verify dependencies, freshness, and targets; preview the exact change; confirm revision-bound phase authorization where mutation is privileged; acquire the controller lease; produce tests/p03/P03-S006-benchmark-primary-and-fast-candidates; run the named positive and negative checks; record sanitized evidence; release the lease. Acceptance criterion: the fixed prompt corpus records cold and warm latency, tokens per second, peak VRAM and RAM, spill, quality, tool and vision result, and concurrency at 16K plus approved larger contexts.

## 11. Automated acceptance tests

Assert the expected story inventory is nonzero, then verify that the fixed prompt corpus records cold and warm latency, tokens per second, peak VRAM and RAM, spill, quality, tool and vision result, and concurrency at 16K plus approved larger contexts. Fail on missing evidence, unexpected targets, secrets, stale sources, an untested negative boundary, or a validator that matched zero fixtures.

## 12. Human validation

Not applicable — P03-S006 is accepted through deterministic checks plus an independent review; no experiential or credential-bearing action is delegated to the LLM.

## 13. Idempotency and rollback

Tests use synthetic or owner-approved fixtures and leave accepted services and configuration unchanged. Rollback removes story-created fixtures and restores the pre-test snapshot recorded in evidence/P03-S006/rollback.json.

## 14. Required evidence

Commit tests/p03/P03-S006-benchmark-primary-and-fast-candidates or its versioned result plus evidence/P03-S006/activation.json, evidence/P03-S006/change-inventory.json, evidence/P03-S006/test-results.json, evidence/P03-S006/rollback.json, and evidence/P03-S006/review.md; include exact versions or digests, sanitized commands or observations, timestamps, and an explicit not-applicable human record.

## 15. Definition of done

P03-S006 is Done only when the fixed prompt corpus records cold and warm latency, tokens per second, peak VRAM and RAM, spill, quality, tool and vision result, and concurrency at 16K plus approved larger contexts; the story-owned output and evidence inventory exist, independent review has no unresolved material finding, rollback and idempotency evidence is accepted, and controller state unlocks the declared next story.

## 16. Pause-safe boundaries

Pause after the activation packet, after each download, install, configuration backup, or other atomic unit, after tests, and after evidence is committed. Before pausing, finish or roll back the active unit and record the exact next command plus current model and provider in evidence/P03-S006/checkpoint.json.
