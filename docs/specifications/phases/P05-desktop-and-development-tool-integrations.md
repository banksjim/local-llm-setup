# P05: Desktop and Development Tool Integrations

**Depends on:** P04  
**Required outcome:** Reliable desktop dictation and documented, reversible VS Code, Codex, Claude, ChatGPT, Cowork, autocomplete, and LM Studio workflows.  
**Status:** Planned

## Fixed architecture and execution boundary

- VS Code remains the Windows desktop shell and opens repositories inside `AI-Workbench` through the WSL remote workflow. Python, Go, Node.js, and TypeScript language tooling runs in Ubuntu; Windows-only UI extensions remain on the Windows side.
- Use the current Ollama-publisher VS Code language-model provider extension for local chat when it passes activation tests; VS Code's built-in Ollama provider is deprecated as of this review. Local inline completion is a separate optional extension path because local BYOK chat does not provide inline suggestions. Preserve ordinary IntelliSense and any existing native or Copilot completion configuration.
- Run Codex CLI and Claude Code inside `AI-Workbench`. Codex uses its built-in `ollama` provider and `--oss`; Claude Code uses Ollama's supported `ollama launch claude`/Anthropic-compatible path. Cloud and local profiles are explicit, backed up, testable, and never switched silently mid-story.
- ChatGPT, Codex desktop, Claude Desktop, and Claude Cowork receive a sourced compatibility matrix. Do not claim they can replace their hosted model with Ollama unless their current official documentation says so; MCP/tool connectivity is not the same as model-backend replacement.
- Windows-wide dictation is selected by a same-corpus benchmark, initially led by OpenWhispr and at least two current credible OSS alternatives. Local transcription and any cleanup model must remain local during the acceptance test.
- LM Studio remains an optional evaluation track. It stores its own compatible model files under `H:\ai\models\lm-studio`, binds only `127.0.0.1`, requires authentication where supported, and uses port `51239` only after an availability check. It may coexist with Ollama, but concurrent GPU residency is not assumed.
- P05 produces reusable `operations/windows/p05`, `operations/ubuntu/p05`, and `tests/p05` preview/apply/verify/rollback operations plus user-facing integration guides; it does not build the final installer.

## Current source baseline (refresh at activation)

- [VS Code language-model documentation](https://code.visualstudio.com/docs/agent-customization/language-models)
- [Continue repository status and license](https://github.com/continuedev/continue)
- [Codex configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference)
- [Claude Code configuration reference](https://code.claude.com/docs/en/configuration)
- [Ollama Claude Code integration](https://docs.ollama.com/integrations/claude-code)
- [LM Studio local server](https://lmstudio.ai/docs/developer/core/server)
- [OpenWhispr repository](https://github.com/OpenWhispr/openwhispr)

## Gate

P05-S001 research and P05-S002 learning may run after P04 acceptance without privileged authorization. Before P05-S003 installs benchmark candidates, the controller presents one revision-bound preview covering candidate provenance, microphone/clipboard/hotkey access, Windows startup changes, VS Code and WSL client settings, credential boundaries, optional-component opt-in gates, port 51239, model storage, tests, and rollback; the owner gives one P05 phase authorization. Authentication, microphone permission, optional opt-in, learning answers, and final acceptance remain genuine human actions rather than repeated approvals. Material changes to clients, extensions, endpoints, credential paths, privacy, risk, or operations invalidate the authorization.

## Story sequence

| Seq. | Story | Step | Risk |
|---:|---|---|---|
| 1 | [P05-S001: Refresh integration and dictation landscape](../../stories/P05/P05-S001-refresh-integration-and-dictation-landscape.md) | Research | Low |
| 2 | [P05-S002: Learn local client and endpoint boundaries](../../stories/P05/P05-S002-learn-local-client-and-endpoint-boundaries.md) | Learning | Low |
| 3 | [P05-S003: Benchmark OSS desktop dictation candidates](../../stories/P05/P05-S003-benchmark-oss-desktop-dictation-candidates.md) | Testing | High |
| 4 | [P05-S004: Install and configure selected desktop dictation](../../stories/P05/P05-S004-install-and-configure-selected-desktop-dictation.md) | Implementation | High |
| 5 | [P05-S005: Configure VS Code local AI chat workflow](../../stories/P05/P05-S005-configure-vs-code-local-ai-chat-workflow.md) | Implementation | High |
| 6 | [P05-S006: Create optional local autocomplete guide and prompt](../../stories/P05/P05-S006-create-optional-local-autocomplete-guide-and-prompt.md) | Implementation | Medium |
| 7 | [P05-S007: Configure Codex CLI local and cloud profiles](../../stories/P05/P05-S007-configure-codex-cli-local-and-cloud-profiles.md) | Implementation | High |
| 8 | [P05-S008: Configure Claude Code local and cloud profiles](../../stories/P05/P05-S008-configure-claude-code-local-and-cloud-profiles.md) | Implementation | High |
| 9 | [P05-S009: Document ChatGPT and Claude desktop compatibility](../../stories/P05/P05-S009-document-chatgpt-and-claude-desktop-compatibility.md) | Implementation | Low |
| 10 | [P05-S010: Create optional LM Studio evaluation guide](../../stories/P05/P05-S010-create-optional-lm-studio-evaluation-guide.md) | Implementation | Medium |
| 11 | [P05-S011: Verify cross-tool workflows](../../stories/P05/P05-S011-verify-cross-tool-workflows.md) | Testing | High |
| 12 | [P05-S012: Perform integration owner acceptance](../../stories/P05/P05-S012-perform-integration-owner-acceptance.md) | Human Validation | High |

## Completion

Every non-superseded story is Done; human evidence is genuine; review findings resolve; rollback evidence exists; and the outcome is demonstrated on the reference workstation.
