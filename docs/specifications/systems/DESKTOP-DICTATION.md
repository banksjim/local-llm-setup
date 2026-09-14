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
| OpenWhispr | Cross-platform, global hotkey, local Whisper/Parakeet, rich feature set |
| Handy | Focused offline dictation, Whisper/Parakeet, GPU support, simple workflow |
| WhisPaste | Offline global hotkey and auto-paste, MIT license |

New credible OSS candidates discovered at activation are scored before the shortlist is frozen. No candidate wins from marketing claims alone.

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

The highest-scoring acceptable candidate becomes the default. The runner-up is documented as fallback. Installation is pinned, checksum/provenance checked where available, reversible, and configured for local processing. Cloud cleanup or rewrite features remain disabled unless separately approved.

## 5. Acceptance

The chosen application works in every target class, remains local during a network-disconnected test, meets an owner-approved accuracy/latency threshold, coexists with Ollama, survives restart, and can be removed without leaving models, startup tasks, hotkeys, or private recordings behind.

## 6. Current project sources

- [OpenWhispr repository](https://github.com/OpenWhispr/openwhispr)
- [Handy repository](https://github.com/cjpais/Handy)
- [WhisPaste repository](https://github.com/whispaste/whispaste)
- [Open WebUI speech-to-text configuration](https://docs.openwebui.com/features/chat-conversations/audio/speech-to-text/stt-config/)
