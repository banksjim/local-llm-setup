# P10-S014: Write the core operator and usage guides

| Property | Value |
|---|---|
| Story ID | P10-S014 |
| Phase | P10 — Operations and Final Acceptance |
| Sequence | 10 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Medium |
| Actor | LLM |
| Dependencies | P10-S013 |
| Unlocks | P10-S015 |
| Preferred route | Interface: coding agent through goagentic; Provider: controller-selected value cloud provider; Model class: technical documentation; Effort: medium; Fallback: qualified local documentation model with independent cloud factual review. |
| Research freshness | Product instructions checked against accepted installed versions and official sources within each owning story’s freshness window. |

## 1. User story
As the owner, I want one navigable guide set that tells me what exists, which model/settings to use, and how to use it from my actual tools.
## 2. Bounded objective
Update root `README.md`; create `docs/architecture/WINDOWS-ARCHITECTURE.md`, `docs/guides/windows/INSTALL.md`, `QUICKSTART.md`, `MODEL-GUIDE.md`, `USAGE-RECOMMENDATIONS.md`, `OPEN-WEBUI.md`, `TOOL-INTEGRATIONS.md`, `VS-CODE.md`, `AGENTS.md`, `RAG-AND-INGESTION.md`, `MEMORY.md`, and `DICTATION.md`; create `prompts/README.md`, shared `prompts/program/resume.md`, `execute-next-story.md`, `review-story.md`, and `complete-gate.md`, plus `prompts/claude-code/implement-goagentic-command-skills.md`.
## 3. Learning objective
Not applicable — consolidate earlier targeted lessons and link their evidence; do not add redundant general training.
## 4. Current research requirements
Recheck every product-specific step against official docs and the accepted release; date citations and label locally measured recommendations. Current model/tool tables must be generated from the accepted registry, not training memory.
## 5. Preconditions and unlock conditions
P10-S013 is Done; accepted architecture, commands, ports, profiles, model registry, integrations, lessons, and evidence are stable. The activation packet fixes the required prompt inventory and intended reader tasks.
## 6. In scope
Windows/WSL/container responsibility; storage; data flow/trust Mermaid diagrams; Rancher/Ollama/Open WebUI setup/use; task-to-model and context/profile matrix for all supported Windows models; VS Code Windows-versus-WSL extensions for Python/Go/Node/TypeScript; Codex CLI, Claude Code, ChatGPT, Claude Cowork, OpenAI-compatible clients, and optional LM Studio port 51239; autocomplete optional track; dictation; agent skills/assets/scripts/MCP; MLflow; RAG/Crawl4AI/Docling/Google export; durable-memory inbox; privacy/safety; prompts and exact next links.
## 7. Out of scope and prohibited changes
No unaccepted model/tool, private content, secret, copied long-form tutorial, workstation mutation, macOS implementation, operations/recovery procedures owned by P10-S015, or implication that optional LM Studio shares Ollama model files.
## 8. Privilege and human approval
Documentation changes need no new approval. External publication beyond this existing public playbook and any private-data example requires separate scope.
## 9. Risk rationale
Medium: reversible files, but incorrect commands or model guidance can cause unsafe use or wasted storage/time.
## 10. Execution contract
Write for a nonexpert; lead with choices/outcomes; separate Windows/WSL/container commands; use exact tested wrappers; label required/optional/manual; include expected results and stop links; use concise original explanations; preserve hardware-specific caveat; cross-link rather than duplicate; never show real secrets or personal paths beyond declared architecture.
## 11. Automated acceptance tests
All 19 artifacts named in the bounded objective exist; `prompts/README.md` explains direct Codex CLI and Claude Code use, while the Claude-specific document is sufficient to implement equivalent command skills; required headings/tasks and both Windows/WSL contexts are present; local links resolve; Mermaid parses; commands parse or match accepted help; model/settings tables match registry and 4090 profiles; integration endpoints/ports match config; extension IDs validate; prompt schemas contain scope/test/evidence/pause; source dates are fresh; terminology/privacy/secret/license scans pass.
## 12. Human validation
Owner uses only the guides to choose a model/profile for three tasks, find the correct VS Code/agent/RAG/memory/dictation instructions, and locate how to begin installation. Ambiguity becomes a documentation defect.
## 13. Idempotency and rollback
Regeneration from unchanged evidence makes no semantic change. Git reversion restores guides/prompts without workstation mutation.
## 14. Required evidence
Commit guides/prompts plus `evidence/P10-S014/activation.json`, guide/prompt inventory, source/measurement map, link/Mermaid/command/model/extension/freshness/privacy checks, changed-file list, owner usability result, independent factual review, and `checkpoint.json`.
## 15. Definition of done
The named guide and prompt set is current, internally consistent, independently reviewed, and usable without chat history; owner tasks pass; P10-S015 unlocks.
## 16. Pause-safe boundaries
Pause after each complete guide/prompt and its validation; never leave moved/renamed documents with broken incoming links.
