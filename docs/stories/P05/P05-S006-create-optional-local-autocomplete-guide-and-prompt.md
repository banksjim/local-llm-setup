# P05-S006: Create optional local autocomplete guide and prompt

| Property | Value |
|---|---|
| Story ID | P05-S006 |
| Phase | P05 — Desktop and Development Tool Integrations |
| Sequence | 6 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Medium |
| Actor | LLM |
| Dependencies | P05-S005 |
| Unlocks | P05-S007 |
| Preferred route | Interface: goagentic in the designated cloud IDE or CLI; Provider: qualified local Ollama worker or OpenAI or Anthropic cloud; Model class: current implementation model; Effort: medium; Fallback: current Terra or Sonnet-class cloud route, then Sol or Sonnet-class diagnosis if verification fails. |
| Research freshness | Current VS Code inline-completion limitation plus current source, license, release, maintenance, privacy, and Ollama documentation for credible OSS completion extensions checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to select and document a maintained OSS local-autocomplete option separately from VS Code chat and existing completion, with an LLM-executable setup prompt, so that I can opt in without disrupting what works.

## 2. Bounded objective

Research, qualify, and document a maintained OSS local-autocomplete option plus setup and removal prompts; do not preselect Continue or any extension before the current review.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P05-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Check current VS Code documentation and each candidate's primary repository, license, releases, issue activity, privacy and telemetry behavior, Ollama support, Windows or WSL placement, and uninstall path within 7 days. Record Continue's read-only maintenance status if it remains a candidate; do not rely on training memory or old tutorials.

## 5. Preconditions and unlock conditions

P05-S005. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create docs/guides/optional/vscode-local-autocomplete.md with a current candidate matrix and selection or no-selection decision, owner opt-in gate, exact Windows versus WSL placement, LLM-executable preview/install/verify/remove prompts, four-language sample repository, latency, privacy, and suggestion tests, and IntelliSense regression checks. Store evidence under evidence/P05-S006/. Reusable operation: operations/windows/p05/P05-S006-create-optional-local-autocomplete-guide-and-prompt.

## 7. Out of scope and prohibited changes

Do not weaken WSL isolation, overwrite unrelated editor settings, share Windows and Ubuntu credentials, enable cloud transcription or cleanup, silently replace a hosted model, expose a local endpoint to the LAN, or install an optional integration without owner opt-in.

## 8. Privilege and human approval

No new approval is required while the revision-bound P05 phase authorization still matches the work. The LLM may execute only the previewed story-owned operations; any changed target, network boundary, data class, risk, or destructive action stops for a new preview.

## 9. Risk rationale

The optional extension can send source context or override completion behavior; installation is opt-in and reversible.

## 10. Execution contract

Create an activation packet; verify dependencies, freshness, and targets; preview the exact change; confirm revision-bound phase authorization where mutation is privileged; acquire the controller lease; produce operations/windows/p05/P05-S006-create-optional-local-autocomplete-guide-and-prompt; run the named positive and negative checks; record sanitized evidence; release the lease. Acceptance criterion: the guide states that VS Code local BYOK does not supply inline suggestions, compares a freshly qualified OSS extension with native or Copilot completion, provides opt-in setup and removal prompts, and proves IntelliSense is unchanged.

## 11. Automated acceptance tests

Assert the expected story inventory is nonzero, then verify that the guide states that VS Code local BYOK does not supply inline suggestions, compares a freshly qualified OSS extension with native or Copilot completion, provides opt-in setup and removal prompts, and proves IntelliSense is unchanged. Fail on missing evidence, unexpected targets, secrets, stale sources, an untested negative boundary, or a validator that matched zero fixtures.

## 12. Human validation

Not applicable — P05-S006 is accepted through deterministic checks plus an independent review; no experiential or credential-bearing action is delegated to the LLM.

## 13. Idempotency and rollback

The operation at operations/windows/p05/P05-S006-create-optional-local-autocomplete-guide-and-prompt must implement preview, apply, verify, and story-owned rollback. A second apply is a no-op; rollback restores the recorded pre-story configuration without deleting user models, databases, documents, repositories, or unrelated settings.

## 14. Required evidence

Commit operations/windows/p05/P05-S006-create-optional-local-autocomplete-guide-and-prompt or its versioned result plus evidence/P05-S006/activation.json, evidence/P05-S006/change-inventory.json, evidence/P05-S006/test-results.json, evidence/P05-S006/rollback.json, and evidence/P05-S006/review.md; include exact versions or digests, sanitized commands or observations, timestamps, and an explicit not-applicable human record.

## 15. Definition of done

P05-S006 is Done only when the guide states that VS Code local BYOK does not supply inline suggestions, compares a freshly qualified OSS extension with native or Copilot completion, provides opt-in setup and removal prompts, and proves IntelliSense is unchanged; the story-owned output and evidence inventory exist, independent review has no unresolved material finding, rollback and idempotency evidence is accepted, and controller state unlocks the declared next story.

## 16. Pause-safe boundaries

Pause after the activation packet, after each download, install, configuration backup, or other atomic unit, after tests, and after evidence is committed. Before pausing, finish or roll back the active unit and record the exact next command plus current model and provider in evidence/P05-S006/checkpoint.json.
