# P04-S009: Deploy and configure Open WebUI

| Property | Value |
|---|---|
| Story ID | P04-S009 |
| Phase | P04 — Open WebUI and Supporting AI Services |
| Sequence | 9 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | Human + LLM |
| Dependencies | P04-S008 |
| Unlocks | P04-S010 |
| Preferred route | Interface: goagentic in the designated cloud IDE or CLI; Provider: qualified local Ollama worker or OpenAI or Anthropic cloud; Model class: current implementation model; Effort: medium; Fallback: current Terra or Sonnet-class cloud route, then Sol or Sonnet-class diagnosis if verification fails. |
| Research freshness | Current Open WebUI deployment and environment docs checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to deploy Open WebUI against native Ollama and supporting services with localhost-only access, so that progress is inspectable and independent of chat memory.

## 2. Bounded objective

Deploy Open WebUI against native Ollama and supporting services with localhost-only access.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P04-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current Open WebUI deployment and environment docs checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not rely on training memory for changeable facts.

## 5. Preconditions and unlock conditions

P04-S008. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create and verify Open WebUI service, explicit 127.0.0.1 UI binding, persistent volume, secret template, approved-model allowlist, and a separate Rancher-source rule on the P03 bounded gateway using activation-discovered addressing; include text and vision fixtures plus container, WSL, host, and LAN boundary probes. Store versioned implementation or guidance at the story-owned output path already named by this contract and sanitized run evidence under evidence/P04-S009/. Reusable operation: operations/windows/p04/P04-S009-deploy-and-configure-open-webui.

## 7. Out of scope and prohibited changes

Do not enable Kubernetes or Wasm, publish database ports, bind host services beyond loopback, store secrets in Git or evidence, ingest a real knowledge base, enable cloud APIs, or alter Ollama model selection.

## 8. Privilege and human approval

No new approval is required while the revision-bound P04 phase authorization still matches the work. The owner must personally perform the named GUI, authentication, elevation, microphone, preference, or acceptance actions; changed scope stops for a new preview.

## 9. Risk rationale

Open WebUI holds chat history, credentials, uploads, and model connectivity across several services.

## 10. Execution contract

Create an activation packet; verify dependencies, freshness, and targets; preview the exact change; confirm revision-bound phase authorization; acquire the controller lease; produce operations/windows/p04/P04-S009-deploy-and-configure-open-webui; add only the discovered Rancher source to the inference/read gateway; run positive and negative checks; record sanitized evidence; release the lease. Acceptance criterion: Open WebUI is reachable only on 127.0.0.1, lists only approved Ollama models through the bounded gateway, completes text and vision prompts, persists state, and rejects gateway administration plus LAN access.

## 11. Automated acceptance tests

Assert nonzero text, vision, persistence, and boundary fixtures. Verify Open WebUI is reachable only on 127.0.0.1; the container reaches only the inference and read allowlist through the Rancher-scoped gateway; model administration, unknown routes, direct Ollama access, non-Rancher sources, and LAN probes fail; approved models work; state persists after recreate. Zero negative fixtures or an unrestricted Ollama path fails.

## 12. Human validation

The owner creates the initial local Open WebUI administrator through the loopback UI, keeps the password out of chat and evidence, confirms only approved Ollama models appear, and records one text and one vision result in evidence/P04-S009/human-validation.md. The LLM may guide but cannot enter or retain the credential.

## 13. Idempotency and rollback

The operation at operations/windows/p04/P04-S009-deploy-and-configure-open-webui must implement preview, apply, verify, and story-owned rollback. A second apply is a no-op; rollback restores the recorded pre-story configuration without deleting user models, databases, documents, repositories, or unrelated settings.

## 14. Required evidence

Commit operations/windows/p04/P04-S009-deploy-and-configure-open-webui or its versioned result plus evidence/P04-S009/activation.json, evidence/P04-S009/change-inventory.json, evidence/P04-S009/test-results.json, evidence/P04-S009/rollback.json, and evidence/P04-S009/review.md; include exact versions or digests, sanitized commands or observations, timestamps, and genuine owner-authored human validation.

## 15. Definition of done

P04-S009 is Done only when Open WebUI is reachable only on 127.0.0.1, creates a local owner, lists only approved Ollama models, completes text and vision prompts, persists state, and rejects a LAN probe; the story-owned output and evidence inventory exist, independent review has no unresolved material finding, rollback and idempotency evidence is accepted, and controller state unlocks the declared next story.

## 16. Pause-safe boundaries

Pause after the activation packet, after each download, install, configuration backup, or other atomic unit, after tests, and after evidence is committed. Before pausing, finish or roll back the active unit and record the exact next command plus current model and provider in evidence/P04-S009/checkpoint.json.
