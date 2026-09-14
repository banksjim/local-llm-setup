# Desktop Dictation Selection and Implementation Specification

**System ID:** `SYS-STT`  
**Status:** Approved evaluation design; product not selected  
**Primary phase:** P05  
**Last reviewed:** 2026-09-13

## 1. Scope

This system provides Windows-wide push-to-talk or toggle dictation into VS Code, terminals, browsers, Office applications, Codex, and Claude. It is separate from Open WebUI's in-chat audio transcription and from batch audio/video transcription.

## 2. Candidates

The activation story performs a fresh GitHub and release review. The initial shortlist is:

| Candidate | Current reason to test |
|---|---|
| OpenWhispr | Current lead to benchmark: MIT-licensed, Windows build, global hotkey, and local speech engines; its broader agent, meeting, sync, account, calendar, and optional screen-context features increase the permission surface and must remain disabled for this project |
| Handy | Established focused offline dictation candidate with Whisper/Parakeet and GPU support |
| Whisper Local | Current fully offline Windows/macOS candidate with global hotkey, transforms, and published source |

P05-S001 may replace a candidate when current provenance, maintenance, signing, privacy, or compatibility evidence is stronger. Newly advertised projects must have a readable OSS license, reproducible release provenance, active issue handling, and no unresolved security concern before benchmarking. No candidate wins from marketing claims or star count alone.

## 3. Evaluation

Use the same owner-recorded corpus and microphone for each candidate. Score:

- Word error rate and correction effort for conversational and technical language.
- Names, acronyms, punctuation, code terms, and paragraph commands.
- First-use setup, global hotkey reliability, clipboard/paste behavior, and target-app compatibility.
- Latency, GPU/CPU/RAM use, model storage, idle use, and conflict with Ollama workloads.
- Fully local operation, telemetry defaults, update mechanism, signature/release provenance, license, maintenance activity, issue health, and rollback.
- Behavior in VS Code Windows UI, WSL terminals, browser text fields, Office apps, Codex, and Claude.

The owner performs experiential scoring because comfort, correction burden, and hotkey behavior cannot be established by automation.

## 4. Selection and installation

The highest-scoring acceptable candidate becomes the default. The runner-up is documented as fallback. Installation is pinned, checksum/provenance checked where available, reversible, and configured for local processing. Configure the winner for the minimum dictation-only feature set: no account or team space, cloud transcription, sync, meeting capture, calendar access, assistant/agent calls, screen capture, remote MCP/API exposure, cloud cleanup, or rewrite feature. A candidate that cannot disable unrelated collection or network features fails rather than receiving broader permission.

## 5. Acceptance

The chosen application works in every target class, remains local during a network-disconnected test, makes no unexpected outbound request during a connected traffic-capture test, exposes only the selected microphone/hotkey/paste permissions, meets an owner-approved accuracy/latency threshold, coexists with Ollama, survives restart, and can be removed without leaving models, startup tasks, hotkeys, accounts, integrations, or private recordings behind.

## 6. Current project sources

- [OpenWhispr repository](https://github.com/OpenWhispr/openwhispr)
- [Handy repository](https://github.com/cjpais/Handy)
- [Whisper Local repository](https://github.com/drajb/whisper-local)
- [Open WebUI speech-to-text configuration](https://docs.openwebui.com/features/chat-conversations/audio/speech-to-text/stt-config/)
