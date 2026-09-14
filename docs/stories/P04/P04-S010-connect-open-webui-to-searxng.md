# P04-S010: Connect Open WebUI to SearXNG

| Property | Value |
|---|---|
| Story ID | P04-S010 |
| Phase | P04 — Open WebUI and Supporting AI Services |
| Sequence | 10 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P04-S009 |
| Unlocks | P04-S011 |
| Preferred route | Interface: goagentic in the designated cloud IDE or CLI; Provider: qualified local Ollama worker or OpenAI or Anthropic cloud; Model class: current implementation model; Effort: medium; Fallback: current Terra or Sonnet-class cloud route, then Sol or Sonnet-class diagnosis if verification fails. |
| Research freshness | Current Open WebUI feature documentation checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to connect Open WebUI to the private SearXNG JSON search endpoint, so that local chats can perform sourced live-web searches without exposing SearXNG publicly.

## 2. Bounded objective

Configure and verify only the Open WebUI-to-SearXNG web-search path.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P04-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current Open WebUI feature documentation checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not rely on training memory for changeable facts.

## 5. Preconditions and unlock conditions

P04-S009. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create and verify the version-compatible Open WebUI settings export, private Compose service URL for SearXNG, JSON query template, result-count and concurrency limits, one sourced-search fixture, one disabled-provider fixture, and host and LAN negative probes. Store the operation at operations/windows/p04/P04-S010-connect-open-webui-to-searxng and sanitized evidence under evidence/P04-S010/.

## 7. Out of scope and prohibited changes

Do not enable Kubernetes or Wasm, publish database ports, bind host services beyond loopback, store secrets in Git or evidence, ingest a real knowledge base, enable cloud APIs, or alter Ollama model selection.

## 8. Privilege and human approval

No new approval is required while the revision-bound P04 phase authorization still matches the work. The LLM may execute only the previewed story-owned operations; any changed target, network boundary, data class, risk, or destructive action stops for a new preview.

## 9. Risk rationale

Cross-service integration handles private content and outbound search, with multiple failure and privacy boundaries.

## 10. Execution contract

Create an activation packet; verify Open WebUI and SearXNG versions and health; preview the settings delta; confirm phase authorization; acquire the lease; apply the SearXNG-only settings; run the sourced-search and boundary fixtures; export sanitized configuration evidence; release the lease. Acceptance criterion: Open WebUI returns attributable results from the private SearXNG endpoint while direct host and LAN use remain unavailable.

## 11. Automated acceptance tests

Assert at least one positive and two negative fixtures, then verify provider identity, query encoding, JSON results, source links, concurrency and result limits, disabled-provider failure, private-network service resolution, and denial from unintended host or LAN clients. Fail on missing sources, fallback to another search provider, secrets, or zero matched fixtures.

## 12. Human validation

Not applicable — P04-S010 is accepted through deterministic checks plus an independent review; no experiential or credential-bearing action is delegated to the LLM.

## 13. Idempotency and rollback

The operation at operations/windows/p04/P04-S010-connect-open-webui-to-searxng implements preview, apply, verify, and rollback of only web-search settings. A second apply is a no-op; rollback restores the prior Open WebUI settings export without changing SearXNG data or other integrations.

## 14. Required evidence

Commit operations/windows/p04/P04-S010-connect-open-webui-to-searxng plus evidence/P04-S010/activation.json, change-inventory.json, test-results.json, rollback.json, review.md, and a sanitized Open WebUI settings export; record the SearXNG image digest and exact tested query contract.

## 15. Definition of done

P04-S010 is Done only when the SearXNG-only positive and negative checks pass, no unrelated Open WebUI integration changed, the operation and evidence inventory exist, independent review has no unresolved material finding, rollback and idempotency are proven, and P04-S011 unlocks.

## 16. Pause-safe boundaries

Pause after the activation packet, after each download, install, configuration backup, or other atomic unit, after tests, and after evidence is committed. Before pausing, finish or roll back the active unit and record the exact next command plus current model and provider in evidence/P04-S010/checkpoint.json.
