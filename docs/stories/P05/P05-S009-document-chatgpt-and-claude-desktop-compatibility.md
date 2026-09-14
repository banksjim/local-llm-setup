# P05-S009: Document ChatGPT and Claude desktop compatibility

| Property | Value |
|---|---|
| Story ID | P05-S009 |
| Phase | P05 — Desktop and Development Tool Integrations |
| Sequence | 9 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Low |
| Actor | LLM |
| Dependencies | P05-S008 |
| Unlocks | P05-S010 |
| Preferred route | Interface: goagentic in the designated cloud IDE or CLI; Provider: qualified local Ollama worker or OpenAI or Anthropic cloud; Model class: current implementation model; Effort: medium; Fallback: current Terra or Sonnet-class cloud route, then Sol or Sonnet-class diagnosis if verification fails. |
| Research freshness | Current official OpenAI, Anthropic, and Ollama documentation checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to provide accurate setup or limitations for ChatGPT, Codex desktop, Claude Desktop, and Claude Cowork, so that progress is inspectable and independent of chat memory.

## 2. Bounded objective

Provide accurate setup or limitations for ChatGPT, Codex desktop, Claude Desktop, and Claude Cowork.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P05-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current official OpenAI, Anthropic, and Ollama documentation checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not rely on training memory for changeable facts.

## 5. Preconditions and unlock conditions

P05-S008. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create and verify a four-client compatibility matrix covering hosted model selection, local replacement, MCP and tool access, file access, credential boundary, exact supported setup, limitation, and official source date. Store versioned implementation or guidance at the story-owned output path already named by this contract and sanitized run evidence under evidence/P05-S009/. Reusable operation: operations/windows/p05/P05-S009-document-chatgpt-and-claude-desktop-compatibility.

## 7. Out of scope and prohibited changes

Do not weaken WSL isolation, overwrite unrelated editor settings, share Windows and Ubuntu credentials, enable cloud transcription or cleanup, silently replace a hosted model, expose a local endpoint to the LAN, or install an optional integration without owner opt-in.

## 8. Privilege and human approval

No new approval is required while the revision-bound P05 phase authorization still matches the work. The LLM may execute only the previewed story-owned operations; any changed target, network boundary, data class, risk, or destructive action stops for a new preview.

## 9. Risk rationale

This is sourced documentation only; the risk is misleading the owner into assuming unsupported local-model behavior.

## 10. Execution contract

Create an activation packet; verify dependencies, freshness, and targets; preview the exact change; confirm revision-bound phase authorization where mutation is privileged; acquire the controller lease; produce operations/windows/p05/P05-S009-document-chatgpt-and-claude-desktop-compatibility; run the named positive and negative checks; record sanitized evidence; release the lease. Acceptance criterion: the matrix separates hosted model selection, local backend replacement, MCP and tool access, and file access for ChatGPT, Codex desktop, Claude Desktop, and Cowork; every claim has a current official source.

## 11. Automated acceptance tests

Assert the expected story inventory is nonzero, then verify that the matrix separates hosted model selection, local backend replacement, MCP and tool access, and file access for ChatGPT, Codex desktop, Claude Desktop, and Cowork; every claim has a current official source. Fail on missing evidence, unexpected targets, secrets, stale sources, an untested negative boundary, or a validator that matched zero fixtures.

## 12. Human validation

Not applicable — P05-S009 is accepted through deterministic checks plus an independent review; no experiential or credential-bearing action is delegated to the LLM.

## 13. Idempotency and rollback

The operation at operations/windows/p05/P05-S009-document-chatgpt-and-claude-desktop-compatibility must implement preview, apply, verify, and story-owned rollback. A second apply is a no-op; rollback restores the recorded pre-story configuration without deleting user models, databases, documents, repositories, or unrelated settings.

## 14. Required evidence

Commit operations/windows/p05/P05-S009-document-chatgpt-and-claude-desktop-compatibility or its versioned result plus evidence/P05-S009/activation.json, evidence/P05-S009/change-inventory.json, evidence/P05-S009/test-results.json, evidence/P05-S009/rollback.json, and evidence/P05-S009/review.md; include exact versions or digests, sanitized commands or observations, timestamps, and an explicit not-applicable human record.

## 15. Definition of done

P05-S009 is Done only when the matrix separates hosted model selection, local backend replacement, MCP and tool access, and file access for ChatGPT, Codex desktop, Claude Desktop, and Cowork; every claim has a current official source; the story-owned output and evidence inventory exist, independent review has no unresolved material finding, rollback and idempotency evidence is accepted, and controller state unlocks the declared next story.

## 16. Pause-safe boundaries

Pause after the activation packet, after each download, install, configuration backup, or other atomic unit, after tests, and after evidence is committed. Before pausing, finish or roll back the active unit and record the exact next command plus current model and provider in evidence/P05-S009/checkpoint.json.
