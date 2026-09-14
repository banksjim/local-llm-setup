# P05-S005: Configure VS Code local AI chat workflow

| Property | Value |
|---|---|
| Story ID | P05-S005 |
| Phase | P05 — Desktop and Development Tool Integrations |
| Sequence | 5 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P05-S004 |
| Unlocks | P05-S006 |
| Preferred route | Interface: goagentic in the designated cloud IDE or CLI; Provider: qualified local Ollama worker or OpenAI or Anthropic cloud; Model class: current implementation model; Effort: medium; Fallback: current Terra or Sonnet-class cloud route, then Sol or Sonnet-class diagnosis if verification fails. |
| Research freshness | Current official VS Code language-model documentation, Ollama-publisher provider extension listing or source, and selected VS Code version checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to configure the official Ollama-publisher VS Code local-chat path without disrupting language tooling or existing completion, so that progress is inspectable and independent of chat memory.

## 2. Bounded objective

Configure and verify the current Ollama-publisher language-model provider for VS Code chat without using the deprecated built-in Ollama provider.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P05-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Check the current VS Code language-model page, exact Ollama provider extension identity and publisher, VS Code version, and Ollama endpoint contract within 7 days. Record the built-in provider's current status and stop if the official replacement cannot be verified.

## 5. Preconditions and unlock conditions

P05-S004. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create and verify VS Code Windows and AI-Workbench settings backups, the Ollama-publisher provider extension with extension-ID and publisher validation, removal of any deprecated built-in Ollama provider entry, approved local model entry, local chat fixture, Python, Go, Node, and TypeScript extension health checks, and settings restore. Store evidence under evidence/P05-S005/. Reusable operation: operations/windows/p05/P05-S005-configure-vs-code-local-ai-chat-workflow.

## 7. Out of scope and prohibited changes

Do not weaken WSL isolation, overwrite unrelated editor settings, share Windows and Ubuntu credentials, enable cloud transcription or cleanup, silently replace a hosted model, expose a local endpoint to the LAN, or install an optional integration without owner opt-in.

## 8. Privilege and human approval

No new approval is required while the revision-bound P05 phase authorization still matches the work. The LLM may execute only the previewed story-owned operations; any changed target, network boundary, data class, risk, or destructive action stops for a new preview.

## 9. Risk rationale

VS Code configuration and model access span Windows UI and WSL, but changes are backed up and scoped.

## 10. Execution contract

Create an activation packet; verify dependencies, freshness, and targets; preview the exact change; confirm revision-bound phase authorization where mutation is privileged; acquire the controller lease; produce operations/windows/p05/P05-S005-configure-vs-code-local-ai-chat-workflow; run the named positive and negative checks; record sanitized evidence; release the lease. Acceptance criterion: VS Code in AI-Workbench adds the approved Ollama model through Manage Language Models, completes local chat without a Copilot plan, keeps Python, Go, Node, and TypeScript tooling intact, and preserves existing inline completion settings.

## 11. Automated acceptance tests

Assert nonzero chat and language-tool fixtures. Verify the provider's exact extension ID and Ollama publisher, absence of deprecated built-in configuration, approved model identity, local chat without a Copilot plan, no cloud request during the offline fixture, Python, Go, Node, and TypeScript tooling health, preserved inline completion settings, and settings restore. Wrong publisher, zero fixtures, or unrelated extension changes fail.

## 12. Human validation

Not applicable — P05-S005 is accepted through deterministic checks plus an independent review; no experiential or credential-bearing action is delegated to the LLM.

## 13. Idempotency and rollback

The operation at operations/windows/p05/P05-S005-configure-vs-code-local-ai-chat-workflow must implement preview, apply, verify, and story-owned rollback. A second apply is a no-op; rollback restores the recorded pre-story configuration without deleting user models, databases, documents, repositories, or unrelated settings.

## 14. Required evidence

Commit operations/windows/p05/P05-S005-configure-vs-code-local-ai-chat-workflow or its versioned result plus evidence/P05-S005/activation.json, evidence/P05-S005/change-inventory.json, evidence/P05-S005/test-results.json, evidence/P05-S005/rollback.json, and evidence/P05-S005/review.md; include exact versions or digests, sanitized commands or observations, timestamps, and an explicit not-applicable human record.

## 15. Definition of done

P05-S005 is Done only when VS Code in AI-Workbench adds the approved Ollama model through Manage Language Models, completes local chat without a Copilot plan, keeps Python, Go, Node, and TypeScript tooling intact, and preserves existing inline completion settings; the story-owned output and evidence inventory exist, independent review has no unresolved material finding, rollback and idempotency evidence is accepted, and controller state unlocks the declared next story.

## 16. Pause-safe boundaries

Pause after the activation packet, after each download, install, configuration backup, or other atomic unit, after tests, and after evidence is committed. Before pausing, finish or roll back the active unit and record the exact next command plus current model and provider in evidence/P05-S005/checkpoint.json.
