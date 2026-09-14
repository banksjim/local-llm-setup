# P05-S004: Install and configure selected desktop dictation

| Property | Value |
|---|---|
| Story ID | P05-S004 |
| Phase | P05 — Desktop and Development Tool Integrations |
| Sequence | 4 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | Human + LLM |
| Dependencies | P05-S003 |
| Unlocks | P05-S005 |
| Preferred route | Interface: goagentic in the designated cloud IDE or CLI; Provider: qualified local Ollama worker or OpenAI or Anthropic cloud; Model class: current implementation model; Effort: medium; Fallback: current Terra or Sonnet-class cloud route, then Sol or Sonnet-class diagnosis if verification fails. |
| Research freshness | Selected project's current official documentation checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to install the winner for fully local Windows-wide dictation with reversible hotkey, startup, and model settings, so that progress is inspectable and independent of chat memory.

## 2. Bounded objective

Install the winner for fully local Windows-wide dictation with reversible hotkey, startup, and model settings.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P05-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Selected project's current official documentation checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not rely on training memory for changeable facts.

## 5. Preconditions and unlock conditions

P05-S003. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create and verify selected package provenance, Windows user-level install or portable location, local engine/model settings, minimal microphone/hotkey/paste permissions, explicit disablement of unrelated account/sync/meeting/calendar/agent/screen/remote-API/cloud features, global hotkey and startup configuration, target-app tests, disconnected and connected traffic probes, settings backup, and complete removal operation. Store versioned implementation or guidance at the story-owned output path and sanitized evidence under evidence/P05-S004/. Reusable operation: operations/windows/p05/P05-S004-install-and-configure-selected-desktop-dictation.

## 7. Out of scope and prohibited changes

Do not weaken WSL isolation, overwrite unrelated editor settings, share Windows and Ubuntu credentials, enable cloud transcription or cleanup, silently replace a hosted model, expose a local endpoint to the LAN, or install an optional integration without owner opt-in.

## 8. Privilege and human approval

No new approval is required while the revision-bound P05 phase authorization still matches the work. The owner must personally perform the named GUI, authentication, elevation, microphone, preference, or acceptance actions; changed scope stops for a new preview.

## 9. Risk rationale

Installing an always-available microphone and clipboard app changes Windows startup, permissions, hotkeys, and private model data.

## 10. Execution contract

Create an activation packet; verify dependencies, freshness, and targets; preview the exact change; confirm revision-bound phase authorization where mutation is privileged; acquire the controller lease; produce operations/windows/p05/P05-S004-install-and-configure-selected-desktop-dictation; run the named positive and negative checks; record sanitized evidence; release the lease. Acceptance criterion: the selected app dictates into VS Code, WSL terminal, browser, Office, Codex, and Claude; network-disconnected use passes; startup and hotkey do not collide; restart and clean removal and reapply drills pass.

## 11. Automated acceptance tests

Assert nonzero application, permission, network, and removal fixtures. Verify dictation into VS Code, WSL terminal, browser, Office, Codex, and Claude; disconnected use; no unexpected connected traffic; only approved permissions; every unrelated feature disabled; no startup/hotkey collision; restart; clean removal; and reapply. Any required account/cloud feature, screen or meeting capture, remote listener, residue, stale source, or zero matched fixture fails.

## 12. Human validation

The owner handles the selected application's installer and microphone prompts, chooses the global hotkey after conflict review, dictates into VS Code, a WSL terminal, a browser, Office, Codex, and Claude, and records accuracy, latency, startup, and offline observations in evidence/P05-S004/human-validation.md. The LLM cannot create the spoken samples, preference, or subjective observations.

## 13. Idempotency and rollback

The operation at operations/windows/p05/P05-S004-install-and-configure-selected-desktop-dictation must implement preview, apply, verify, and story-owned rollback. A second apply is a no-op; rollback restores the recorded pre-story configuration without deleting user models, databases, documents, repositories, or unrelated settings.

## 14. Required evidence

Commit operations/windows/p05/P05-S004-install-and-configure-selected-desktop-dictation or its versioned result plus evidence/P05-S004/activation.json, evidence/P05-S004/change-inventory.json, evidence/P05-S004/test-results.json, evidence/P05-S004/rollback.json, and evidence/P05-S004/review.md; include exact versions or digests, sanitized commands or observations, timestamps, and genuine owner-authored human validation.

## 15. Definition of done

P05-S004 is Done only when the selected app dictates into VS Code, WSL terminal, browser, Office, Codex, and Claude; network-disconnected use passes; startup and hotkey do not collide; restart and clean removal and reapply drills pass; the story-owned output and evidence inventory exist, independent review has no unresolved material finding, rollback and idempotency evidence is accepted, and controller state unlocks the declared next story.

## 16. Pause-safe boundaries

Pause after the activation packet, after each download, install, configuration backup, or other atomic unit, after tests, and after evidence is committed. Before pausing, finish or roll back the active unit and record the exact next command plus current model and provider in evidence/P05-S004/checkpoint.json.
