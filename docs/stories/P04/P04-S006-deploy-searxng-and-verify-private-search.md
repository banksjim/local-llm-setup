# P04-S006: Deploy SearXNG and verify private search

| Property | Value |
|---|---|
| Story ID | P04-S006 |
| Phase | P04 — Open WebUI and Supporting AI Services |
| Sequence | 6 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P04-S005 |
| Unlocks | P04-S007 |
| Preferred route | Interface: goagentic in the designated cloud IDE or CLI; Provider: qualified local Ollama worker or OpenAI or Anthropic cloud; Model class: current implementation model; Effort: medium; Fallback: current Terra or Sonnet-class cloud route, then Sol or Sonnet-class diagnosis if verification fails. |
| Research freshness | Current SearXNG and Open WebUI integration docs checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to deploy SearXNG on the private network with JSON results and documented upstream privacy behavior, so that progress is inspectable and independent of chat memory.

## 2. Bounded objective

Deploy SearXNG on the private network with JSON results and documented upstream privacy behavior.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P04-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current SearXNG and Open WebUI integration docs checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not rely on training memory for changeable facts.

## 5. Preconditions and unlock conditions

P04-S005. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create and verify SearXNG settings and secret template, private Compose service, JSON-format configuration, health and query probes, disabled-format and LAN negative tests, and outbound privacy note. Store versioned implementation or guidance at the story-owned output path already named by this contract and sanitized run evidence under evidence/P04-S006/. Reusable operation: operations/windows/p04/P04-S006-deploy-searxng-and-verify-private-search.

## 7. Out of scope and prohibited changes

Do not enable Kubernetes or Wasm, publish database ports, bind host services beyond loopback, store secrets in Git or evidence, ingest a real knowledge base, enable cloud APIs, or alter Ollama model selection.

## 8. Privilege and human approval

No new approval is required while the revision-bound P04 phase authorization still matches the work. The LLM may execute only the previewed story-owned operations; any changed target, network boundary, data class, risk, or destructive action stops for a new preview.

## 9. Risk rationale

SearXNG makes outbound requests and privacy depends on configuration, but the local service remains private and disposable.

## 10. Execution contract

Create an activation packet; verify dependencies, freshness, and targets; preview the exact change; confirm revision-bound phase authorization where mutation is privileged; acquire the controller lease; produce operations/windows/p04/P04-S006-deploy-searxng-and-verify-private-search; run the named positive and negative checks; record sanitized evidence; release the lease. Acceptance criterion: private-network JSON search succeeds from its intended client, direct LAN and unintended host access are absent, disabled formats fail, and upstream privacy limitations are documented.

## 11. Automated acceptance tests

Assert the expected story inventory is nonzero, then verify that private-network JSON search succeeds from its intended client, direct LAN and unintended host access are absent, disabled formats fail, and upstream privacy limitations are documented. Fail on missing evidence, unexpected targets, secrets, stale sources, an untested negative boundary, or a validator that matched zero fixtures.

## 12. Human validation

Not applicable — P04-S006 is accepted through deterministic checks plus an independent review; no experiential or credential-bearing action is delegated to the LLM.

## 13. Idempotency and rollback

The operation at operations/windows/p04/P04-S006-deploy-searxng-and-verify-private-search must implement preview, apply, verify, and story-owned rollback. A second apply is a no-op; rollback restores the recorded pre-story configuration without deleting user models, databases, documents, repositories, or unrelated settings.

## 14. Required evidence

Commit operations/windows/p04/P04-S006-deploy-searxng-and-verify-private-search or its versioned result plus evidence/P04-S006/activation.json, evidence/P04-S006/change-inventory.json, evidence/P04-S006/test-results.json, evidence/P04-S006/rollback.json, and evidence/P04-S006/review.md; include exact versions or digests, sanitized commands or observations, timestamps, and an explicit not-applicable human record.

## 15. Definition of done

P04-S006 is Done only when private-network JSON search succeeds from its intended client, direct LAN and unintended host access are absent, disabled formats fail, and upstream privacy limitations are documented; the story-owned output and evidence inventory exist, independent review has no unresolved material finding, rollback and idempotency evidence is accepted, and controller state unlocks the declared next story.

## 16. Pause-safe boundaries

Pause after the activation packet, after each download, install, configuration backup, or other atomic unit, after tests, and after evidence is committed. Before pausing, finish or roll back the active unit and record the exact next command plus current model and provider in evidence/P04-S006/checkpoint.json.
