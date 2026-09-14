# P05-S010: Create optional LM Studio evaluation guide

| Property | Value |
|---|---|
| Story ID | P05-S010 |
| Phase | P05 — Desktop and Development Tool Integrations |
| Sequence | 10 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Medium |
| Actor | LLM |
| Dependencies | P05-S009 |
| Unlocks | P05-S011 |
| Preferred route | Interface: goagentic in the designated cloud IDE or CLI; Provider: qualified local Ollama worker or OpenAI or Anthropic cloud; Model class: current implementation model; Effort: medium; Fallback: current Terra or Sonnet-class cloud route, then Sol or Sonnet-class diagnosis if verification fails. |
| Research freshness | Current LM Studio and Ollama documentation checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to document a separate model copy, checked localhost API port 51239, client switching, storage, test, stop, and removal workflow, so that progress is inspectable and independent of chat memory.

## 2. Bounded objective

Document a separate model copy, checked localhost API port 51239, client switching, storage, test, stop, and removal workflow.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P05-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current LM Studio and Ollama documentation checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not rely on training memory for changeable facts.

## 5. Preconditions and unlock conditions

P05-S009. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create and verify docs/guides/optional/lm-studio-evaluation.md plus operations/windows/p05/P05-S010-create-optional-lm-studio-evaluation-guide with an owner opt-in gate, version and model provenance checks, exact `H:\ai\models\lm-studio` model location, 127.0.0.1:51239 availability and bind logic, API token handling, mockable compatibility probes, VRAM test, stop, and removal. Live installation and model download occur only with owner opt-in; absence of opt-in does not block the guide. Store evidence under evidence/P05-S010/.

## 7. Out of scope and prohibited changes

Do not weaken WSL isolation, overwrite unrelated editor settings, share Windows and Ubuntu credentials, enable cloud transcription or cleanup, silently replace a hosted model, expose a local endpoint to the LAN, or install an optional integration without owner opt-in.

## 8. Privilege and human approval

Guide authoring and offline validation need no new approval. A live LM Studio installation or model download requires an explicit optional-track opt-in under evidence/P05-S010/; opt-in does not permit LAN exposure or modification of Ollama.

## 9. Risk rationale

LM Studio adds a second model store and server and can consume the full GPU; localhost binding and removal are bounded.

## 10. Execution contract

Research current LM Studio server, storage, authentication, and import contracts; write the guide and reusable opt-in operation; run static and mocked positive and negative tests unconditionally. Only with opt-in, verify a free port before binding 127.0.0.1:51239, use a separate model copy, run authenticated compatibility and VRAM probes, stop the server, and exercise story-owned removal. Record live results or an explicit not-run disposition without treating the optional lane as a failure.

## 11. Automated acceptance tests

Assert nonzero guide sections and mock fixtures. Verify current source links, separate-store warning, port-availability branch, loopback-only bind, authentication branch, Ollama nonmutation, stop and removal, and the opt-in guard. With opt-in, require live OpenAI and Anthropic-compatible probes, resource results, and removal evidence; without opt-in, require an honest not-run record and make no live claim.

## 12. Human validation

Not applicable — P05-S010 is accepted through deterministic checks plus an independent review; no experiential or credential-bearing action is delegated to the LLM.

## 13. Idempotency and rollback

Guide generation is idempotent. The optional live operation implements preview, apply, verify, stop, and removal; a second apply is a no-op. Rollback removes only the story-installed package, settings, and model copy after an exact inventory and never deletes Ollama blobs or unrelated LM Studio data.

## 14. Required evidence

Commit docs/guides/optional/lm-studio-evaluation.md and operations/windows/p05/P05-S010-create-optional-lm-studio-evaluation-guide plus evidence/P05-S010/activation.json, opt-in-or-not-run.json, change-inventory.json, test-results.json, rollback.json, and review.md; include exact versions or digests and sanitized observations without API tokens.

## 15. Definition of done

P05-S010 is Done when the standalone guide, opt-in guard, static and mocked tests, evidence inventory, and independent review pass. With opt-in, live compatibility, resource, and removal evidence must also pass; without opt-in, the record states live testing was not run and makes no live claim. P05-S011 then unlocks.

## 16. Pause-safe boundaries

Pause after the activation packet, after each download, install, configuration backup, or other atomic unit, after tests, and after evidence is committed. Before pausing, finish or roll back the active unit and record the exact next command plus current model and provider in evidence/P05-S010/checkpoint.json.
