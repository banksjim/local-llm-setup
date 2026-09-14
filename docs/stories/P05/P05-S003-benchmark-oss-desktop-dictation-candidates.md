# P05-S003: Benchmark OSS desktop dictation candidates

| Property | Value |
|---|---|
| Story ID | P05-S003 |
| Phase | P05 — Desktop and Development Tool Integrations |
| Sequence | 3 |
| Status | Planned |
| Step | Testing |
| Hold reason | Dependency |
| Risk | High |
| Actor | Human + LLM |
| Dependencies | P05-S002 |
| Unlocks | P05-S004 |
| Preferred route | Interface: goagentic in the designated cloud IDE or CLI; Provider: OpenAI or Anthropic, different from the implementer for acceptance review; Model class: current quality or review model; Effort: high; Fallback: stop and switch to the current Sol or Sonnet-class route; qualified local models remain advisory during probation. |
| Research freshness | Candidate repositories, releases, licenses, and security status checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to test OpenWhispr, Handy, Whisper Local, and newly qualified candidates with the same owner corpus and applications, so that progress is inspectable and independent of chat memory.

## 2. Bounded objective

Test OpenWhispr, Handy, Whisper Local, and newly qualified candidates with the same owner corpus and applications.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P05-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Candidate repositories, releases, licenses, and security status checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not rely on training memory for changeable facts.

## 5. Preconditions and unlock conditions

P05-S002. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create and verify owner-approved audio corpus outside Git, scored application target list, isolated candidate installs, minimal-permission and feature-disable inventory, disconnected and connected traffic capture, resource telemetry, WER and correction rubric, uninstall-residue scan, and selection report. Specifically test that account/sync, meeting/calendar, assistant/agent, screen-context, remote API/MCP, and cloud transcription/cleanup features are absent or disabled. Store the suite at tests/p05/P05-S003-benchmark-oss-desktop-dictation-candidates and sanitized evidence under evidence/P05-S003/.

## 7. Out of scope and prohibited changes

Do not weaken WSL isolation, overwrite unrelated editor settings, share Windows and Ubuntu credentials, enable cloud transcription or cleanup, silently replace a hosted model, expose a local endpoint to the LAN, or install an optional integration without owner opt-in.

## 8. Privilege and human approval

Before mutation, present the complete revision-bound P05 phase preview and obtain the single phase authorization defined by the phase gate. The owner separately handles any elevation, GUI, microphone, or private-corpus action; these are participation, not additional approvals.

## 9. Risk rationale

Desktop apps receive microphone, clipboard, hotkey, and paste access and process a private owner corpus.

## 10. Execution contract

Create an activation packet; verify dependencies, freshness, and targets; preview the exact change; confirm revision-bound phase authorization where mutation is privileged; acquire the controller lease; produce tests/p05/P05-S003-benchmark-oss-desktop-dictation-candidates; run the named positive and negative checks; record sanitized evidence; release the lease. Acceptance criterion: each qualified app uses the same owner-recorded corpus, microphone, target applications, and rubric; WER, correction burden, latency, resources, offline traffic, hotkey reliability, provenance, and uninstall residue are reported.

## 11. Automated acceptance tests

Assert a nonzero candidate, corpus, target-app, permission, and network-fixture inventory. Verify each qualified app uses the same corpus, microphone, applications, and rubric; report WER, correction burden, latency, resources, offline and connected traffic, hotkey reliability, provenance, and uninstall residue. Fail a candidate on required sign-in, unexpected outbound traffic, an enabled account/sync/meeting/calendar/agent/screen/remote-API/cloud feature, excess permission, incomplete uninstall, stale source, or zero matched fixtures.

## 12. Human validation

The owner records the approved private comparison corpus outside Git, grants microphone access to each isolated candidate, dictates the same fixed and natural samples into every target application, scores correction burden and hotkey comfort, and records the preference in evidence/P05-S003/human-validation.md. The LLM cannot create the recording or subjective scores.

## 13. Idempotency and rollback

Tests use synthetic or owner-approved fixtures and leave accepted services and configuration unchanged. Rollback removes story-created fixtures and restores the pre-test snapshot recorded in evidence/P05-S003/rollback.json.

## 14. Required evidence

Commit tests/p05/P05-S003-benchmark-oss-desktop-dictation-candidates or its versioned result plus evidence/P05-S003/activation.json, evidence/P05-S003/change-inventory.json, evidence/P05-S003/test-results.json, evidence/P05-S003/rollback.json, and evidence/P05-S003/review.md; include exact versions or digests, sanitized commands or observations, timestamps, and genuine owner-authored human validation.

## 15. Definition of done

P05-S003 is Done only when each qualified app uses the same owner-recorded corpus, microphone, target applications, and rubric; WER, correction burden, latency, resources, offline traffic, hotkey reliability, provenance, and uninstall residue are reported; the story-owned output and evidence inventory exist, independent review has no unresolved material finding, rollback and idempotency evidence is accepted, and controller state unlocks the declared next story.

## 16. Pause-safe boundaries

Pause after the activation packet, after each download, install, configuration backup, or other atomic unit, after tests, and after evidence is committed. Before pausing, finish or roll back the active unit and record the exact next command plus current model and provider in evidence/P05-S003/checkpoint.json.
