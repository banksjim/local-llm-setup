# P05-S008: Configure Claude Code local and cloud profiles

| Property | Value |
|---|---|
| Story ID | P05-S008 |
| Phase | P05 — Desktop and Development Tool Integrations |
| Sequence | 8 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | Human + LLM |
| Dependencies | P05-S007 |
| Unlocks | P05-S009 |
| Preferred route | Interface: goagentic in the designated cloud IDE or CLI; Provider: qualified local Ollama worker or OpenAI or Anthropic cloud; Model class: current implementation model; Effort: medium; Fallback: current Terra or Sonnet-class cloud route, then Sol or Sonnet-class diagnosis if verification fails. |
| Research freshness | Current official Claude Code and Ollama integration docs checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to configure Claude Code inside Ubuntu for the owner's Claude plan and permitted local model routes, so that progress is inspectable and independent of chat memory.

## 2. Bounded objective

Configure Claude Code inside Ubuntu for the owner's Claude plan and permitted local model routes.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P05-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current official Claude Code and Ollama integration docs checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not rely on training memory for changeable facts.

## 5. Preconditions and unlock conditions

P05-S007. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create and verify Ubuntu Claude Code version and auth preflight, backed-up user and project settings, explicit Claude-plan and Ollama launch wrappers, synthetic repository fixture, provider identity probe, Opus prohibition check, and settings restore. Store versioned implementation or guidance at the story-owned output path already named by this contract and sanitized run evidence under evidence/P05-S008/. Reusable operation: operations/ubuntu/p05/P05-S008-configure-claude-code-local-and-cloud-profiles.

## 7. Out of scope and prohibited changes

Do not weaken WSL isolation, overwrite unrelated editor settings, share Windows and Ubuntu credentials, enable cloud transcription or cleanup, silently replace a hosted model, expose a local endpoint to the LAN, or install an optional integration without owner opt-in.

## 8. Privilege and human approval

No new approval is required while the revision-bound P05 phase authorization still matches the work. The owner must personally perform the named GUI, authentication, elevation, microphone, preference, or acceptance actions; changed scope stops for a new preview.

## 9. Risk rationale

Claude Code can mutate repositories and run tools; endpoint overrides and credentials must not leak between profiles.

## 10. Execution contract

Create an activation packet; verify dependencies, freshness, and targets; preview the exact change; confirm revision-bound phase authorization where mutation is privileged; acquire the controller lease; produce operations/ubuntu/p05/P05-S008-configure-claude-code-local-and-cloud-profiles; run the named positive and negative checks; record sanitized evidence; release the lease. Acceptance criterion: Claude Code in AI-Workbench completes one Claude-plan and one local Ollama repository fixture; local uses the supported Anthropic-compatible launch path, no Opus route exists, identity is visible, and settings restore passes.

## 11. Automated acceptance tests

Assert the expected story inventory is nonzero, then verify that Claude Code in AI-Workbench completes one Claude-plan and one local Ollama repository fixture; local uses the supported Anthropic-compatible launch path, no Opus route exists, identity is visible, and settings restore passes. Fail on missing evidence, unexpected targets, secrets, stale sources, an untested negative boundary, or a validator that matched zero fixtures.

## 12. Human validation

The owner completes Claude Code authentication through the trusted flow, confirms the subscription profile and local Ollama launch wrapper identify different providers, verifies no Opus route or token-bearing setting exists, and records both repository-fixture results in evidence/P05-S008/human-validation.md. The LLM cannot enter credentials or author the owner's provider and model observations.

## 13. Idempotency and rollback

The operation at operations/ubuntu/p05/P05-S008-configure-claude-code-local-and-cloud-profiles must implement preview, apply, verify, and story-owned rollback. A second apply is a no-op; rollback restores the recorded pre-story configuration without deleting user models, databases, documents, repositories, or unrelated settings.

## 14. Required evidence

Commit operations/ubuntu/p05/P05-S008-configure-claude-code-local-and-cloud-profiles or its versioned result plus evidence/P05-S008/activation.json, evidence/P05-S008/change-inventory.json, evidence/P05-S008/test-results.json, evidence/P05-S008/rollback.json, and evidence/P05-S008/review.md; include exact versions or digests, sanitized commands or observations, timestamps, and genuine owner-authored human validation.

## 15. Definition of done

P05-S008 is Done only when Claude Code in AI-Workbench completes one Claude-plan and one local Ollama repository fixture; local uses the supported Anthropic-compatible launch path, no Opus route exists, identity is visible, and settings restore passes; the story-owned output and evidence inventory exist, independent review has no unresolved material finding, rollback and idempotency evidence is accepted, and controller state unlocks the declared next story.

## 16. Pause-safe boundaries

Pause after the activation packet, after each download, install, configuration backup, or other atomic unit, after tests, and after evidence is committed. Before pausing, finish or roll back the active unit and record the exact next command plus current model and provider in evidence/P05-S008/checkpoint.json.
