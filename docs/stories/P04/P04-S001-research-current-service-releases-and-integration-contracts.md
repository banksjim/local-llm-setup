# P04-S001: Research current service releases and integration contracts

| Property | Value |
|---|---|
| Story ID | P04-S001 |
| Phase | P04 — Open WebUI and Supporting AI Services |
| Sequence | 1 |
| Status | Planned |
| Step | Research |
| Hold reason | Phase Not Activated |
| Risk | Low |
| Actor | LLM |
| Dependencies | P03-S011 |
| Unlocks | P04-S002 |
| Preferred route | Interface: goagentic through a web-enabled cloud IDE or CLI; Provider: OpenAI or Anthropic with primary-source web access; Model class: current economical research model; Effort: medium; Fallback: current Sol or Sonnet-class synthesis route when sources conflict. |
| Research freshness | Official documentation, releases, and security advisories checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to refresh Open WebUI, Rancher Desktop, Compose, PostgreSQL and PGVector, SearXNG, Docling Serve, and MLflow guidance, so that progress is inspectable and independent of chat memory.

## 2. Bounded objective

Refresh Open WebUI, Rancher Desktop, Compose, PostgreSQL and PGVector, SearXNG, Docling Serve, and MLflow guidance.

## 3. Learning objective

Not applicable — this research story prepares the evidence used by the following learning gate and does not teach an owner-operated procedure.

## 4. Current research requirements

Official documentation, releases, and security advisories checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not rely on training memory for changeable facts.

## 5. Preconditions and unlock conditions

P03-S011. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create and verify the service release matrix for Rancher Desktop, Compose, Open WebUI, PostgreSQL, PGVector, SearXNG, Docling Serve, and MLflow plus image digest and migration register; no image is pulled. Store versioned implementation or guidance at the story-owned output path already named by this contract and sanitized run evidence under evidence/P04-S001/.

## 7. Out of scope and prohibited changes

Do not enable Kubernetes or Wasm, publish database ports, bind host services beyond loopback, store secrets in Git or evidence, ingest a real knowledge base, enable cloud APIs, or alter Ollama model selection.

## 8. Privilege and human approval

No privileged authorization is required because P04-S001 performs source research and versioned documentation only; discovery of a required mutation creates or reroutes to a separately previewed story.

## 9. Risk rationale

Research changes only planning evidence, while stale compatibility data blocks implementation.

## 10. Execution contract

Create an activation packet; verify dependencies, freshness, and targets; preview the exact change; confirm revision-bound phase authorization where mutation is privileged; acquire the controller lease; produce docs/research/p04/P04-S001-research-current-service-releases-and-integration-contracts-matrix.md; run the named positive and negative checks; record sanitized evidence; release the lease. Acceptance criterion: the matrix records current stable version, image digest, license, breaking changes, ports, health contract, backup and migration guidance, and direct primary source for each service.

## 11. Automated acceptance tests

Assert the expected story inventory is nonzero, then verify that the matrix records current stable version, image digest, license, breaking changes, ports, health contract, backup and migration guidance, and direct primary source for each service. Fail on missing evidence, unexpected targets, secrets, stale sources, an untested negative boundary, or a validator that matched zero fixtures.

## 12. Human validation

Not applicable — P04-S001 is accepted through deterministic checks plus an independent review; no experiential or credential-bearing action is delegated to the LLM.

## 13. Idempotency and rollback

A repeat run refreshes docs/research/p04/P04-S001-research-current-service-releases-and-integration-contracts-matrix.md without duplicate records. Rollback restores its pre-story Git version and removes only unaccepted evidence/P04-S001/ evidence.

## 14. Required evidence

Commit docs/research/p04/P04-S001-research-current-service-releases-and-integration-contracts-matrix.md or its versioned result plus evidence/P04-S001/activation.json, evidence/P04-S001/change-inventory.json, evidence/P04-S001/test-results.json, evidence/P04-S001/rollback.json, and evidence/P04-S001/review.md; include exact versions or digests, sanitized commands or observations, timestamps, and an explicit not-applicable human record.

## 15. Definition of done

P04-S001 is Done only when the matrix records current stable version, image digest, license, breaking changes, ports, health contract, backup and migration guidance, and direct primary source for each service; the story-owned output and evidence inventory exist, independent review has no unresolved material finding, rollback and idempotency evidence is accepted, and controller state unlocks the declared next story.

## 16. Pause-safe boundaries

Pause after the activation packet, after each download, install, configuration backup, or other atomic unit, after tests, and after evidence is committed. Before pausing, finish or roll back the active unit and record the exact next command plus current model and provider in evidence/P04-S001/checkpoint.json.
