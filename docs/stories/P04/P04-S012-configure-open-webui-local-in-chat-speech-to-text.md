# P04-S012: Configure Open WebUI local in-chat speech to text

| Property | Value |
|---|---|
| Story ID | P04-S012 |
| Phase | P04 — Open WebUI and Supporting AI Services |
| Sequence | 12 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | Human + LLM |
| Dependencies | P04-S011 |
| Unlocks | P04-S013 |
| Preferred route | Interface: goagentic-guided session in the designated cloud IDE or CLI; Provider: owner's active OpenAI or Anthropic subscription; Model class: current implementation model; Effort: medium; Fallback: pause for microphone permission or switch to the current Terra or Sonnet-class route for diagnosis. |
| Research freshness | Current Open WebUI speech-to-text configuration and selected local engine/model documentation checked within 7 days. |

## 1. User story

As the workstation owner, I want private speech input inside Open WebUI chat, so that I can dictate a chat prompt without sending audio to a cloud transcription service.

## 2. Bounded objective

Configure and verify only Open WebUI's local in-chat speech-to-text path.

## 3. Learning objective

Not applicable — the owner receives targeted microphone and privacy guidance during this story; Windows-wide dictation is taught and selected separately in P05.

## 4. Current research requirements

Record the supported local engine, model, browser permission behavior, storage/cache path, resource requirements, exact Open WebUI settings, primary-source URLs, and any telemetry or cloud fallback.

## 5. Preconditions and unlock conditions

P04-S011 is Done; Open WebUI is healthy; the owner is available for microphone permission and spoken validation; phase authorization matches the preview.

## 6. In scope

Create operations/windows/p04/P04-S012-configure-open-webui-local-in-chat-speech-to-text with settings backup, local engine/model configuration, cache location, a synthetic prerecorded audio fixture, browser microphone checklist, outbound-traffic monitor, resource probe, and settings-only rollback. Store evidence under evidence/P04-S012/.

## 7. Out of scope and prohibited changes

Do not install Windows-wide dictation, enable cloud transcription or cleanup, retain owner recordings in Git/evidence, change chat/search/document settings, or give containers unnecessary host microphone access.

## 8. Privilege and human approval

P04 phase authorization covers the configuration. The owner must personally grant or deny browser microphone permission and speak the validation phrase; these are human actions, not a new approval.

## 9. Risk rationale

Microphone input and transcripts are private, and an unnoticed cloud fallback could disclose audio or text; resource contention can also disrupt Ollama.

## 10. Execution contract

Back up settings; validate the local engine and cache; disable cloud fallbacks; apply only STT settings; transcribe the synthetic fixture; monitor outbound traffic and resources; hand off the browser permission and spoken test; restore or retain settings from the recorded result; sanitize evidence and release the lease.

## 11. Automated acceptance tests

Assert at least one audio fixture. Verify local-engine identity, expected fixture transcript threshold, no external transcription request, bounded cache and resource use, setting persistence after restart, and unchanged search/document configuration. Fail if any transcription or cleanup request leaves the workstation, a cloud fallback remains enabled, the fixture threshold is missed, or the validator matches zero fixtures. Automation validates only presence and schema of the owner record, never its content.

## 12. Human validation

The owner grants microphone permission in the intended browser, dictates a fixed and a natural phrase, confirms acceptable latency and correction burden, and writes the result in evidence/P04-S012/human-validation.md. The LLM cannot fabricate the recording or response.

## 13. Idempotency and rollback

Second apply is unchanged and does not redownload an intact model. Rollback restores the prior STT settings and removes only story-downloaded cache content after an explicit inventory; it preserves chats, uploads, and unrelated models.

## 14. Required evidence

Commit the operation and nonprivate fixture plus activation.json, settings diff, local-engine identity, sanitized traffic and resource results, test-results.json, rollback.json, review.md, and genuine human-validation.md under evidence/P04-S012/. Never retain owner audio.

## 15. Definition of done

Synthetic and owner speech work locally at accepted quality, cloud traffic is absent, restart/idempotency/rollback checks pass, unrelated settings are unchanged, independent review resolves findings, and P04-S013 unlocks.

## 16. Pause-safe boundaries

Pause after settings backup, model download, synthetic test, owner handoff, restart test, rollback test, and evidence commit. Do not pause while the microphone is recording; discard or finish that recording first and record the exact next command, current service state, model, and provider in evidence/P04-S012/checkpoint.json.
