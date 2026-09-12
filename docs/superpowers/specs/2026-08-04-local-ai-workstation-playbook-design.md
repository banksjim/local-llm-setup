# Local AI Workstation Playbook — Design Specification

**Date:** 2026-08-04  
**Last reviewed:** 2026-09-11
**Status:** Approved for implementation; September 2026 recommendations incorporated
**Repository:** `local-llm-setup`  
**Product name:** Local AI Workstation Playbook

## 1. Objective

Build a complete, Git-based, open-source-first playbook for two separate local AI workstations:

1. Windows 11 desktop with an AMD Ryzen 7 9800X3D, NVIDIA RTX 4090 (24 GB VRAM), 64 GB RAM, and persistent data rooted at `H:\ai`.
2. MacBook Pro with M4 Pro, 48 GB unified memory, one internal drive, and a hard operational budget of 175 GB for the AI stack.

Each machine is an independent installation. Neither installation shares models, documents, indexes, services, or state with the other. Local services bind to loopback and are inaccessible from the LAN by default. The sole Windows exception is an inference-only gateway restricted by Windows Firewall to the WSL NAT subnet.

The primary user interface is Open WebUI. Ollama manages and serves models natively on each operating system. Rancher Desktop, using Moby/dockerd with Kubernetes disabled, runs the supporting container stack. On Windows, VS Code remains a Windows application but opens development workspaces through Remote - WSL. Codex CLI, Claude Code, the multi-agent harness, Git repositories used by agents, and agent worktrees run inside a dedicated Ubuntu WSL2 distribution.

## 2. Success Criteria

The project is complete when it provides:

- A concise root README and navigable documentation set.
- Platform-specific install, architecture, model, tuning, troubleshooting, backup, restore, update, and uninstall guides.
- A Windows PowerShell installer and PowerShell maintenance scripts.
- A platform-native macOS shell installer and shell maintenance scripts.
- Idempotent install and maintenance operations that preserve user data on repeat runs.
- Open WebUI, native Ollama, SearXNG, Docling Serve, PostgreSQL with PGVector, and a Windows-only inference gateway for the hardened WSL agent path.
- Local speech-to-text using Open WebUI's Faster-Whisper backend, plus an optional native whisper.cpp CLI guide.
- Curated model profiles optimized for each machine.
- Client integration guides for Claude Code, Claude Desktop, Codex CLI, Codex desktop, and VS Code.
- A hardened Ubuntu WSL2 agent-execution guide covering VS Code Remote - WSL, repositories, credentials, harness setup, per-agent worktrees, network access to Ollama, and rollback.
- A separate optional guide and reusable LLM prompt for fully local VS Code inline autocomplete.
- Explicit compatibility boundaries for regular ChatGPT and Claude Cowork.
- Step-by-step automated verification with a generated pass/warn/skip/fail report.
- Dated model and tool research with primary-source links and a repeatable refresh procedure.
- Codex CLI prompts for installation review, verification, maintenance, model research, performance tuning, and troubleshooting.
- Architecture and operational diagrams in Mermaid plus exported SVG when useful.

## 3. Constraints and Non-Goals

### 3.1 Constraints

- Windows persistent data defaults to `H:\ai`.
- macOS usage must warn at 150 GB projected or actual usage and block optional pulls that would exceed 175 GB unless the user explicitly overrides the guard.
- WSL2, Rancher Desktop, and Git are prerequisites and are verified but not installed.
- The Windows agent workflow requires a dedicated Ubuntu WSL2 distribution. The playbook may configure software inside it, but does not silently install, move, reset, unregister, or replace a WSL distribution.
- Homebrew is present on macOS.
- Ollama and the rest of the application stack are installed or configured by the playbook.
- Services are localhost-only except for the Windows inference gateway, which is reachable only from the WSL NAT subnet. No public tunnel, LAN-accessible listener, or remote connector is enabled by default.
- Versioned container images and explicit model tags are used. Floating `main` or `latest` tags are not used in the default deployment.
- User data is never deleted by install, repair, update, or ordinary maintenance commands.

### 3.2 Non-Goals

- Multi-user or Internet-facing hosting.
- Kubernetes deployment.
- Cross-machine model serving or data synchronization.
- Automatic installation or reconfiguration of WSL2 or Rancher Desktop.
- Replacing the underlying model in regular ChatGPT or Claude Cowork. Claude Desktop support is a separate, supported Ollama integration and does not establish equivalent support for Cowork.
- Automatically exposing a local MCP server to cloud services.
- Treating WSL2 as a complete security sandbox. The hardened profile reduces Windows exposure, but WSL integration, deliberately mounted files, credentials, network services, and user-approved host actions remain trust boundaries.
- Pulling every alternative model during the default installation.
- Benchmark claims that have not been measured on the user's hardware.

## 4. Selected Architecture

The design uses hybrid native inference with containerized supporting services.

### 4.1 Native Services

- **Ollama:** Runs natively for direct CUDA access on Windows and Metal/MLX access on macOS.
- **Optional whisper.cpp CLI:** Runs natively only when the user selects that optional profile.

### 4.2 Rancher Desktop Services

The default targets the current stable Rancher Desktop 1.x release with Moby/dockerd. Rancher Desktop 2.0 remains an alpha/technology preview as of the September review and is excluded from the supported default until it has a stable upgrade path.

- **Open WebUI:** Primary user interface, RAG orchestration, built-in Faster-Whisper STT, and client-facing API proxy.
- **SearXNG:** Live web search provider for Open WebUI.
- **Docling Serve:** CPU document extraction sidecar with one worker and bounded threads.
- **PostgreSQL with PGVector:** Stores Open WebUI application data and vector embeddings.
- **Caddy inference gateway (Windows only):** Gives the Ubuntu agent distribution an allowlisted inference route to native Ollama without exposing Ollama's model-management API or other Windows loopback services.

Redis/Valkey is not required for the single-worker default. A documented growth profile may add Valkey if Open WebUI is moved to multiple workers.

### 4.3 Network Boundaries

- Open WebUI publishes `127.0.0.1:3000`.
- Optional administrative endpoints publish only to `127.0.0.1` and are disabled unless required for diagnostics.
- PostgreSQL, Docling, and SearXNG communicate over a private Compose network. They are not reachable from the LAN.
- Open WebUI reaches native Ollama at `http://host.docker.internal:11434` under Rancher Desktop.
- Native Ollama remains bound to Windows loopback at `127.0.0.1:11434`.
- The Windows-only Caddy gateway publishes a separate configurable port, default `11435`, for the Ubuntu agent path. Windows Firewall restricts that port to the WSL NAT subnet; LAN clients are denied.
- The gateway permits only required inference and read-only discovery routes for Ollama, OpenAI-compatible, and Anthropic-compatible clients. Model pull, push, create, copy, delete, and other administrative routes are denied.
- The installer verifies that the Docker API is provided by Rancher Desktop's Moby/dockerd engine.
- Kubernetes is documented as disabled to conserve resources.

### 4.4 Windows WSL2 Agent Execution Boundary

The Windows workstation uses a split execution model:

- Native Windows Ollama owns CUDA inference and model storage under `H:\ai`.
- Rancher Desktop owns the supporting Compose services and is not exposed to agents through a Docker socket by default.
- A dedicated Ubuntu WSL2 distribution owns Codex CLI, Claude Code, the multi-agent harness, Linux development dependencies, repositories, and Git worktrees.
- VS Code runs its user interface on Windows and uses the Microsoft WSL extension so its workspace extensions, terminals, tasks, debuggers, and agent CLIs execute inside Ubuntu.
- Agent-controlled repositories live on the distribution's Linux filesystem rather than `/mnt/c`, `/mnt/h`, or a `\\wsl$`-opened Windows workspace. This avoids DrvFS performance and permission inconsistencies and reduces accidental access to Windows files.

The recommended hardened Ubuntu profile disables automatic Windows-drive mounts and Windows executable interoperability in that distribution. If enabled, the relevant `/etc/wsl.conf` settings are `[automount] enabled=false` and `[interop] enabled=false` with `appendWindowsPath=false`. This is an explicit, reversible hardening step because it prevents conveniences such as launching `code.exe`, `powershell.exe`, or Windows Git helpers from a WSL shell. VS Code is opened through its **WSL: Connect to WSL** user interface when interoperability is disabled.

Git and GitHub authentication for agent work are configured inside Ubuntu using a Linux credential store. Windows credential files, roaming GitHub CLI state, SSH agent sockets, and personal home directories are not mounted into the agent environment by default. This intentionally favors isolation over sharing one credential store across Windows and WSL.

The hardened profile retains WSL's normal NAT networking. Ubuntu discovers the Windows host address and connects to the inference-only gateway on port `11435`; it does not connect directly to Ollama on `11434`. A narrowly scoped Windows Firewall rule accepts gateway traffic from the current WSL NAT subnet and blocks LAN access. The installer revalidates the host address and firewall scope after WSL or network changes. Mirrored networking is documented only as an opt-in compatibility profile for environments such as problematic VPNs because it makes Windows loopback services reachable from WSL and therefore weakens this boundary.

This boundary is risk reduction, not containment against a hostile workload. Agents receive only the repository, tools, credentials, and network access required for their task. Destructive host actions, Windows-drive mounts, Rancher Desktop control, new secrets, and external publication remain explicit user-approved operations.

## 5. Data Flows

### 5.1 Chat and Vision

1. The browser connects to Open WebUI on loopback.
2. Open WebUI sends the request and any image input to native Ollama.
3. Ollama runs the selected local model with the chosen platform profile.
4. The response streams back through Open WebUI.

### 5.2 Web Search

1. Open WebUI sends a search request to SearXNG on the private container network.
2. SearXNG queries configured public search engines.
3. Search results return to Open WebUI with titles, URLs, and snippets.
4. The model synthesizes the results and Open WebUI presents source links.

SearXNG makes outbound Internet requests. The documentation must distinguish local model privacy from unavoidable disclosure of search terms to upstream search engines.

### 5.3 Document Ingestion and Retrieval

1. A document is uploaded or added to an Open WebUI knowledge base.
2. Open WebUI sends it to Docling Serve for structured extraction.
3. Extracted content is chunked with documented defaults.
4. Native Ollama generates embeddings with `qwen3-embedding:0.6b`.
5. Embeddings and metadata are stored in PGVector.
6. At query time, Open WebUI embeds the question, retrieves relevant chunks, and includes citations in the model context.

The same embedding model and dimensions must be used for both ingestion and querying. Changing embedding models requires an explicit reindex procedure.

### 5.4 Speech-to-Text

1. The browser records or uploads supported audio to Open WebUI.
2. Open WebUI's built-in Faster-Whisper backend runs locally with int8 quantization.
3. The transcript is returned to the chat input.

The balanced default uses `Systran/faster-whisper-large-v3` on CPU. The model is cached persistently. Native whisper.cpp is an optional standalone transcription workflow, not a required Open WebUI dependency.

### 5.5 Windows Coding and Multi-Agent Work

1. VS Code connects to the dedicated Ubuntu distribution and opens a repository stored in the Linux filesystem.
2. Codex CLI, Claude Code, or the harness creates one Git worktree per agent and applies a least-privilege tool policy.
3. The agent calls the inference-only gateway through the verified WSL NAT route; the gateway forwards allowed requests to Windows-hosted Ollama, and no model copy is stored in WSL.
4. Ollama schedules inference on the RTX 4090 and queues excess work according to the configured concurrency budget.
5. Each agent writes only to its own worktree. The harness gathers results for review before any merge, external message, deployment, or destructive operation.

The initial RTX 4090 harness profile uses `qwen3.5:9b-q4_K_M` for concurrent worker tasks and reserves `qwen3.8:27b-q4_K_M` for a single quality-critical worker, reviewer, or synthesis pass. It begins with `OLLAMA_MAX_LOADED_MODELS=1` and `OLLAMA_NUM_PARALLEL=1`. Parallelism increases only after measured VRAM, KV-cache, latency, and stability tests because Ollama parallel requests multiply effective context memory.

## 6. Model Profiles

The project supports a curated, tested model set rather than every Ollama registry model.

### 6.1 Windows Defaults

| Role | Model | Default context | Purpose |
|---|---|---:|---|
| Primary | `qwen3.8:27b-q4_K_M` | 16K | General chat, vision, reasoning, document work |
| Fast | `qwen3.5:9b-q4_K_M` | 16K | Low-latency chat and background tasks |
| Agent balanced | `qwen3.5:9b-q4_K_M` | 64K | Claude Code, Codex, harness workers, and repository work |
| Agent quality | `qwen3.8:27b-q4_K_M` | 32K; 64K after validation | Difficult coding, review, and synthesis; larger contexts may spill to RAM |
| Embedding | `qwen3-embedding:0.6b` | model default | RAG ingestion and retrieval |
| Alternative | `gemma4:26b` | 16K | Fast MoE multimodal alternative |
| Agent evaluation | `muse-glimmer:30b-q4_K_M` | 16K–32K | Optional always-on agent and failure-recovery evaluation; not pulled by default |
| Low memory | `gemma4:e4b` | 8K–16K | Multitasking and resource-constrained use |

The 16K primary context is intentionally lower than the model's advertised maximum so the RTX 4090 retains headroom for vision buffers, KV cache, and desktop graphics. The guide provides 8K, 16K, 32K, and 64K profiles and explains expected offload or system-memory spill.

### 6.2 macOS Defaults

| Role | Model | Default context | Purpose |
|---|---|---:|---|
| Primary | `qwen3.8:27b-mlx` | 16K | General multimodal, reasoning, coding, and document use with headroom |
| Fast | `qwen3.5:9b-mlx` | 16K | Low-latency chat and background tasks |
| Agent balanced | `qwen3.5:9b-mlx` | 64K | Claude Code, Codex, and repository work |
| Agent quality | `qwen3.8:27b-mlx` | 32K; 64K after validation | Difficult coding and synthesis; increased unified-memory pressure |
| Embedding | `qwen3-embedding:0.6b` | model default | RAG ingestion and retrieval |
| Performance alternate | `gemma4:26b-mlx` | 16K | Multimodal MoE alternative optimized by Ollama's MLX engine |
| Agent evaluation | `muse-glimmer:30b-mlx` | 16K–32K | Optional long-running local-agent evaluation; not pulled by default |
| Low memory | `gemma4:e4b-mlx` | 8K–16K | Maximum headroom for other applications |

Only one large model is pulled by the default macOS install. Optional pulls are checked against the 175 GB budget.

### 6.3 Optional VS Code Local Autocomplete

Local inline autocomplete is an optional, separately selected profile. It is not installed and its model is not pulled by either platform's default installation.

| Role | Model | Size | Purpose |
|---|---|---:|---|
| Autocomplete | `qwen2.5-coder:1.5b-base` | About 1 GB | Low-latency, fully local inline code suggestions in VS Code through Continue |

VS Code's native AI inline suggestions are provided by GitHub Copilot and may be sufficient when its connectivity, account, quota, and privacy characteristics are acceptable. VS Code can use Ollama models for local chat through the Ollama-maintained integration, but bring-your-own and local models do not currently replace native inline suggestions. The optional local workflow therefore uses the Continue extension with Ollama and is documented as an alternative rather than a default replacement. The older built-in Ollama BYOK provider is not used because VS Code now deprecates it in favor of the Ollama-published extension.

The optional setup must preserve existing VS Code and Continue settings, keep Ollama on loopback, and remain independently removable. Verification reports this feature as skipped unless the user explicitly selects it.

### 6.4 Usage Guides

The repository includes:

- `docs/MODEL-QUICK-REFERENCE.md` as a printable one-page task-to-model guide.
- `windows/docs/MODEL-USAGE.md` with RTX 4090 settings and expected VRAM behavior.
- `macos/docs/MODEL-USAGE.md` with M4 Pro unified-memory and storage guidance.

Each supported model documents chat, vision, OCR, RAG, coding, agent, fast-task, and difficult-reasoning use; context length; thinking mode; temperature; concurrency; keep-alive; resource pressure; and when not to use it.

### 6.5 Personal Agent Profiles

The playbook includes optional Open WebUI profiles for a Thought Partner, Life Coach, Fitness Coach, Financial Coach, and fast daily check-in assistant. These are configuration wrappers over the supported base models, not additional model downloads. The guide distinguishes reflective or educational assistance from licensed medical, mental-health, legal, or financial advice. Persistent personal memory is not part of this playbook.

## 7. Installation and Idempotency

### 7.1 Windows

`windows/scripts/Install-LocalAI.ps1` performs:

1. Preflight checks for Windows version, WSL2 and Ubuntu status, Rancher Desktop, Moby/dockerd, Git, NVIDIA driver, `H:` availability, free space, WSL networking, Windows Firewall scope, and port conflicts.
2. Creation of the approved `H:\ai` directory structure.
3. Ollama installation through a pinned, documented mechanism.
4. Environment and Compose configuration generation.
5. Container image pulls.
6. Model pulls for the selected profile.
7. Service startup.
8. Layered health and functional verification.
9. A timestamped final report.

The script supports `-WhatIf`, configurable data root, profile selection, non-destructive repair, and selective phase execution. Re-running it compares desired and actual state and changes only drifted items.

### 7.2 macOS

`macos/scripts/install-local-ai.sh` performs the equivalent workflow with Homebrew, native Ollama, Rancher Desktop verification, Apple Silicon checks, and storage-budget enforcement. It does not install Homebrew or Rancher Desktop.

### 7.3 Persistent Directory Layout

Windows defaults:

```text
H:\ai\
├── models\ollama\
├── wsl\ubuntu-agents\          # optional dedicated distro VHDX location
├── data\open-webui\
├── data\postgres\
├── data\docling\
├── documents\
├── indexes\
├── backups\
│   └── wsl\                    # explicit WSL exports; not live VHDX copies
├── logs\
└── reports\
```

macOS defaults:

```text
~/Library/Application Support/LocalAI/
├── models/ollama/
├── data/open-webui/
├── data/postgres/
├── data/docling/
├── documents/
├── indexes/
├── backups/
├── logs/
└── reports/
```

## 8. Updates, Backups, Restore, and Uninstall

- Versions are centralized in machine-readable configuration and explained in a human-readable update guide.
- Update checks report available versions but do not mutate the installation without an explicit update command.
- Updates create a preflight report and backup before pulling images or applying database migrations.
- PostgreSQL backups use a consistent dump. Open WebUI files, configuration, and model manifests are included. Ollama model blobs are inventoried but excluded from routine backups by default because they can be re-pulled.
- Restore is verified into an isolated validation target before the guide instructs replacement of active data.
- Rollback restores pinned configuration and compatible data snapshots.
- Uninstall is manual, path-explicit, and separated into application removal, retained-data removal, and model removal. No default command recursively deletes the complete data root.

## 9. Client Integrations

`docs/CLIENT-INTEGRATIONS.md` provides copy-ready, reversible setup for:

- **Claude Code:** Installed and executed inside Ubuntu for the Windows hardened path, with manual Anthropic-compatible Ollama endpoint configuration, model selection, validation, and restore. `ollama launch claude` remains a convenience for non-hardened or native setups.
- **Claude Desktop:** Ollama's supported third-party gateway toggle for local models, including validation and a documented switch back to Anthropic. This does not imply Claude Cowork compatibility.
- **Codex CLI:** Installed and executed inside Ubuntu for the Windows hardened path, using `codex --oss`, a dedicated Ollama provider/profile, model catalogs, validation, and restore. `ollama launch codex` remains a convenience outside the hardened distribution.
- **Codex desktop app:** `ollama launch codex-app`, profile persistence, backups, and restore. The guide warns that a Windows-native Codex task is outside the WSL agent boundary; protected repository work uses Codex CLI inside Ubuntu unless the app provides a verified WSL execution target.
- **VS Code:** Windows UI with Remote - WSL for protected development; workspace extensions and terminals run in Ubuntu. Ollama-backed local chat uses the Ollama-maintained VS Code integration and `ollama launch vscode` where compatible. Native GitHub Copilot inline suggestions remain available when acceptable, and `docs/integrations/VS-CODE-LOCAL-AUTOCOMPLETE.md` documents Continue with `qwen2.5-coder:1.5b-base` as the optional fully local path.

The local-autocomplete guide includes a decision summary comparing native Copilot suggestions with the optional offline/local path. It covers prerequisites, model pull, Continue configuration, platform-specific paths, validation with a small test file, troubleshooting, disablement, and complete rollback.

`prompts/vscode/setup-local-autocomplete.md` provides a reusable instruction for Codex or Claude Code to perform this optional setup. The prompt requires the LLM to detect the installed Continue configuration schema, back up existing configuration, preserve unrelated settings, request approval before installing the extension or model, avoid changing Ollama's loopback binding, verify ghost-text completion and relevant logs, report every change, and provide rollback steps. Conflicting settings cause the LLM to stop and ask for direction rather than overwrite them.

No authoritative OpenAI documentation in the September 2026 review establishes regular ChatGPT as a supported Ollama model frontend, so it remains outside the supported local-backend matrix. ChatGPT MCP apps require a remote server or Secure MCP Tunnel and therefore are not enabled in this local-machine-only design. Claude Desktop can now use Ollama through its supported gateway configuration; Claude Cowork remains outside the supported local-backend matrix unless Anthropic publishes equivalent support. These boundaries are documented with supported local alternatives.

## 10. Repository Structure

```text
local-llm-setup/
├── README.md
├── LICENSE
├── CHANGELOG.md
├── docs/
│   ├── architecture/
│   ├── install/
│   ├── operations/
│   ├── research/
│   ├── CLIENT-INTEGRATIONS.md
│   └── MODEL-QUICK-REFERENCE.md
├── windows/
│   ├── configs/
│   ├── docs/
│   ├── wsl/
│   ├── scripts/
│   └── tests/
├── macos/
│   ├── configs/
│   ├── docs/
│   ├── scripts/
│   └── tests/
├── shared/
│   ├── compose/
│   ├── fixtures/
│   └── versions/
└── prompts/
    ├── install-validation/
    ├── maintenance/
    ├── model-research/
    ├── performance/
    ├── troubleshooting/
    └── vscode/
```

## 11. Error Handling and Observability

- Scripts use strict error handling and nonzero exit codes for failed required phases.
- Every phase logs start time, elapsed time, result, relevant command output, and a recovery recommendation.
- Secrets are redacted from console output and reports.
- Errors distinguish prerequisite failures, permissions, network/DNS, disk space, port conflicts, container health, database migration, Ollama reachability, model pull, GPU/Metal offload, document extraction, embedding, retrieval, search, and speech transcription.
- Timeouts are explicit and configurable for slow pulls, ingestion, and first model load.
- A failed optional feature produces a warning or skip without falsely marking the core stack healthy.
- Repair never deletes unknown or user-created files.

## 12. Verification and Acceptance Tests

Verification is layered so a failure identifies the responsible boundary.

1. **Static checks:** PowerShell parsing and linting, ShellCheck, YAML/Compose validation, JSON parsing, Markdown link checks, and secret scanning.
2. **Preflight tests:** Platform, prerequisite, storage, port, container engine, GPU/Metal, WSL distribution, networking, filesystem-boundary, and permission checks.
3. **Service health:** PostgreSQL readiness, PGVector extension, SearXNG response, Docling API, Ollama API, and Open WebUI health.
4. **Functional fixtures:** Included small text, image, PDF, and audio inputs exercise extraction, vision, RAG, and transcription.
5. **Known-answer RAG:** A fixture is ingested, processing completion is polled, and a known fact must be retrieved with a source reference.
6. **Model verification:** Text output, vision input, tool capability metadata, configured context, and reported GPU/Metal offload.
7. **Persistence:** State is created, services restart, and state remains available.
8. **Idempotency:** Installer and maintenance commands are run again and must report no unintended changes.
9. **Backup/restore rehearsal:** A backup is created and validated in an isolated target.
10. **Final report:** Each test is marked pass, warning, skip, or fail with evidence and remediation.
11. **Agent-boundary tests:** From Ubuntu, verify inference through port `11435`, rejection of Ollama administrative routes and direct port `11434` access, Linux-filesystem repository placement, per-agent worktree separation, disabled Windows-drive automounts and interoperability when selected, absence of an exposed Rancher Desktop socket, and inability to reach unapproved Windows paths.
12. **Harness tests:** Verify queue behavior with one quality worker and multiple fast-model workers, record VRAM and latency, and prove that agent results require review before merge or publication.

Tests that require the target hardware are delivered for the user to run on each workstation. Repository-local tests validate scripts, configuration, fixtures, documentation, and dry-run behavior without pretending that the current development environment is the target machine.

## 13. Documentation Deliverables

- Root README.
- Windows and macOS install guides.
- Architecture overview and detailed component/data-flow diagrams.
- Model guide and platform-specific usage playbooks.
- Performance tuning for RTX 4090, 9800X3D, M4 Pro, Docker/WSL storage, context, batching, concurrency, and thermal/resource headroom.
- Troubleshooting decision trees and common recovery commands.
- Update, rollback, backup, restore, and migration guides.
- Client integration guide.
- Windows WSL2 agent-execution and hardening guide, including VS Code Remote - WSL, Codex CLI, Claude Code, harness operation, per-agent worktrees, credentials, the inference-only gateway, Windows Firewall scoping, backup/export, rollback, and residual-risk explanation.
- Multi-agent harness architecture and capacity guide for the RTX 4090.
- Optional local VS Code autocomplete guide and reusable setup prompt.
- Personal Agents Guide with platform-specific model recommendations, Open WebUI profiles, operating routines, evaluation scenarios, and professional-safety boundaries.
- Reusable personal-agent prompts.
- Security and privacy guide.
- Storage planning and cleanup guide.
- Verification guide and example report.
- Dated current-model/tool research report and refresh method.
- Codex prompt library.

## 14. Research Baseline

The initial research baseline is dated 2026-08-04. A fresh review on 2026-09-11 used current primary documentation from Ollama, Open WebUI, Rancher Desktop, Docker, Docling, whisper.cpp, OpenAI, Anthropic, Microsoft WSL, and VS Code. Recommendations distinguish vendor claims from measurements produced on the user's machines.

The September baseline supersedes Qwen2.5-VL-32B and the August Qwen3.6 default with the workstation-sized, multimodal `qwen3.8:27b` family. Ollama lists the Q4 Windows artifact and MLX artifact at approximately 18 GB with text, image, tools, thinking, and a 256K advertised context; the playbook deliberately starts far below that maximum. `qwen3.5:9b` remains the fast and multi-agent worker default. Gemma 4 26B remains an alternate, while Muse Glimmer 30B is an opt-in evaluation model rather than a default until it passes the repository's hardware tests.

High-confidence September decisions are supported directly by the following primary sources:

- [Ollama Qwen3.8 model tags](https://ollama.com/library/qwen3.8/tags)
- [Ollama Qwen3 embedding model tags](https://ollama.com/library/qwen3-embedding)
- [Ollama Muse Glimmer model tags](https://ollama.com/library/muse-glimmer/tags)
- [Ollama MLX performance update](https://ollama.com/blog/mlx-performance)
- [Ollama Claude Desktop integration](https://ollama.com/blog/claude-desktop)
- [Ollama VS Code integration](https://docs.ollama.com/integrations/vscode)
- [VS Code language-model configuration](https://code.visualstudio.com/docs/agent-customization/language-models)
- [Continue local autocomplete guidance](https://github.com/continuedev/continue/blob/main/docs/customize/deep-dives/autocomplete.mdx)
- [Open WebUI SearXNG integration](https://docs.openwebui.com/features/chat-conversations/web-search/providers/searxng/)
- [Open WebUI Docling integration](https://github.com/open-webui/docs/blob/main/docs/features/chat-conversations/rag/document-extraction/docling.md)
- [Docling Serve releases](https://github.com/docling-project/docling-serve/releases)
- [Open WebUI local speech-to-text configuration](https://docs.openwebui.com/features/chat-conversations/audio/speech-to-text/env-variables/)
- [Rancher Desktop 2.0 status](https://docs.rancherdesktop.io/blog/welcome-to-rancher-desktop-2/)
- [Microsoft WSL networking](https://learn.microsoft.com/windows/wsl/networking)
- [Microsoft WSL configuration](https://learn.microsoft.com/windows/wsl/wsl-config)
- [VS Code development in WSL](https://code.visualstudio.com/docs/remote/wsl)
- [Ollama concurrency guidance](https://docs.ollama.com/faq#how-does-ollama-handle-concurrent-requests)

Model quality and throughput rankings remain provisional until the supplied benchmark suite runs on the RTX 4090 and M4 Pro. In particular, Muse Glimmer's agent positioning and Ollama's MLX performance numbers are vendor-provided claims, not measurements from these machines. The update guide includes a repeatable evaluation template so future model defaults can change without restructuring the stack.

## 15. Licensing

Repository-authored scripts and documentation use the MIT License. Third-party software, container images, models, and downloaded artifacts retain their own licenses and terms. The model guide records relevant license links and flags models whose terms differ from permissive open-source licenses.
