# Local AI Workstation Playbook — Design Specification

**Date:** 2026-08-04  
**Status:** Approved for implementation  
**Repository:** `local-llm-setup`  
**Product name:** Local AI Workstation Playbook

## 1. Objective

Build a complete, Git-based, open-source-first playbook for two separate local AI workstations:

1. Windows 11 desktop with an AMD Ryzen 7 9800X3D, NVIDIA RTX 4090 (24 GB VRAM), 64 GB RAM, and persistent data rooted at `H:\ai`.
2. MacBook Pro with M4 Pro, 48 GB unified memory, one internal drive, and a hard operational budget of 175 GB for the AI stack.

Each machine is an independent installation. Neither installation shares models, documents, indexes, services, or state with the other. All local service ports bind to loopback and are inaccessible from the LAN by default.

The primary user interface is Open WebUI. Ollama manages and serves models natively on each operating system. Rancher Desktop, using Moby/dockerd with Kubernetes disabled, runs the supporting container stack.

## 2. Success Criteria

The project is complete when it provides:

- A concise root README and navigable documentation set.
- Platform-specific install, architecture, model, tuning, troubleshooting, backup, restore, update, and uninstall guides.
- A Windows PowerShell installer and PowerShell maintenance scripts.
- A platform-native macOS shell installer and shell maintenance scripts.
- Idempotent install and maintenance operations that preserve user data on repeat runs.
- Open WebUI, native Ollama, SearXNG, Docling Serve, and PostgreSQL with PGVector.
- Local speech-to-text using Open WebUI's Faster-Whisper backend, plus an optional native whisper.cpp CLI guide.
- Curated model profiles optimized for each machine.
- Client integration guides for Claude Code, Codex CLI, Codex desktop, and VS Code.
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
- Homebrew is present on macOS.
- Ollama and the rest of the application stack are installed or configured by the playbook.
- Services are localhost-only. No reverse proxy, public tunnel, LAN listener, or remote connector is enabled by default.
- Versioned container images and explicit model tags are used. Floating `main` or `latest` tags are not used in the default deployment.
- User data is never deleted by install, repair, update, or ordinary maintenance commands.

### 3.2 Non-Goals

- Multi-user or Internet-facing hosting.
- Kubernetes deployment.
- Cross-machine model serving or data synchronization.
- Automatic installation or reconfiguration of WSL2 or Rancher Desktop.
- Replacing the underlying model in regular ChatGPT or Claude Cowork; neither product currently supports Ollama as a local model backend.
- Automatically exposing a local MCP server to cloud services.
- Pulling every alternative model during the default installation.
- Benchmark claims that have not been measured on the user's hardware.

## 4. Selected Architecture

The design uses hybrid native inference with containerized supporting services.

### 4.1 Native Services

- **Ollama:** Runs natively for direct CUDA access on Windows and Metal/MLX access on macOS.
- **Optional whisper.cpp CLI:** Runs natively only when the user selects that optional profile.

### 4.2 Rancher Desktop Services

- **Open WebUI:** Primary user interface, RAG orchestration, built-in Faster-Whisper STT, and client-facing API proxy.
- **SearXNG:** Live web search provider for Open WebUI.
- **Docling Serve:** CPU document extraction sidecar with one worker and bounded threads.
- **PostgreSQL with PGVector:** Stores Open WebUI application data and vector embeddings.

Redis/Valkey is not required for the single-worker default. A documented growth profile may add Valkey if Open WebUI is moved to multiple workers.

### 4.3 Network Boundaries

- Open WebUI publishes `127.0.0.1:3000`.
- Optional administrative endpoints publish only to `127.0.0.1` and are disabled unless required for diagnostics.
- PostgreSQL, Docling, and SearXNG communicate over a private Compose network. They are not reachable from the LAN.
- Open WebUI reaches native Ollama at `http://host.docker.internal:11434` under Rancher Desktop.
- The installer verifies that the Docker API is provided by Rancher Desktop's Moby/dockerd engine.
- Kubernetes is documented as disabled to conserve resources.

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

## 6. Model Profiles

The project supports a curated, tested model set rather than every Ollama registry model.

### 6.1 Windows Defaults

| Role | Model | Default context | Purpose |
|---|---|---:|---|
| Primary | `qwen3.6:27b` | 16K | General chat, vision, reasoning, document work |
| Fast | `qwen3.5:9b` | 16K | Low-latency chat and background tasks |
| Agent balanced | `qwen3.5:9b` | 64K | Claude Code, Codex, and repository work |
| Agent quality | `qwen3.6:27b` | 64K | Difficult coding and repository analysis; may spill to RAM |
| Embedding | `qwen3-embedding:0.6b` | model default | RAG ingestion and retrieval |
| Alternative | `gemma4:26b` | 16K | Fast MoE multimodal alternative |
| Low memory | `gemma4:e4b` | 8K–16K | Multitasking and resource-constrained use |

The 16K primary context is intentionally lower than the model's advertised maximum so the RTX 4090 retains headroom for vision buffers, KV cache, and desktop graphics. The guide provides 8K, 16K, 32K, and 64K profiles and explains expected offload or system-memory spill.

### 6.2 macOS Defaults

| Role | Model | Default context | Purpose |
|---|---|---:|---|
| Primary | `gemma4:26b-mlx` | 16K | General multimodal use with good memory headroom |
| Fast | `qwen3.5:9b-mlx` | 16K | Low-latency chat and background tasks |
| Agent balanced | `qwen3.5:9b-mlx` | 64K | Claude Code, Codex, and repository work |
| Agent quality | `qwen3.6:27b-mlx` | 64K | Difficult coding; increased unified-memory pressure |
| Embedding | `qwen3-embedding:0.6b` | model default | RAG ingestion and retrieval |
| Quality alternate | `qwen3.6:27b-mlx` | 16K | Qwen general and vision alternative |
| Low memory | `gemma4:e4b-mlx` | 8K–16K | Maximum headroom for other applications |

Only one large model is pulled by the default macOS install. Optional pulls are checked against the 175 GB budget.

### 6.3 Optional VS Code Local Autocomplete

Local inline autocomplete is an optional, separately selected profile. It is not installed and its model is not pulled by either platform's default installation.

| Role | Model | Size | Purpose |
|---|---|---:|---|
| Autocomplete | `qwen2.5-coder:1.5b-base` | About 1 GB | Low-latency, fully local inline code suggestions in VS Code through Continue |

VS Code's native AI inline suggestions are provided by GitHub Copilot and may be sufficient when its connectivity, account, quota, and privacy characteristics are acceptable. VS Code can use Ollama models for local chat, but it does not currently use bring-your-own or local models for native inline suggestions. The optional local workflow therefore uses the Continue extension with Ollama and is documented as an alternative rather than a default replacement.

The optional setup must preserve existing VS Code and Continue settings, keep Ollama on loopback, and remain independently removable. Verification reports this feature as skipped unless the user explicitly selects it.

### 6.4 Usage Guides

The repository includes:

- `docs/MODEL-QUICK-REFERENCE.md` as a printable one-page task-to-model guide.
- `windows/docs/MODEL-USAGE.md` with RTX 4090 settings and expected VRAM behavior.
- `macos/docs/MODEL-USAGE.md` with M4 Pro unified-memory and storage guidance.

Each supported model documents chat, vision, OCR, RAG, coding, agent, fast-task, and difficult-reasoning use; context length; thinking mode; temperature; concurrency; keep-alive; resource pressure; and when not to use it.

## 7. Installation and Idempotency

### 7.1 Windows

`windows/scripts/Install-LocalAI.ps1` performs:

1. Preflight checks for Windows version, WSL2, Rancher Desktop, Moby/dockerd, Git, NVIDIA driver, `H:` availability, free space, and port conflicts.
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
├── data\open-webui\
├── data\postgres\
├── data\docling\
├── documents\
├── indexes\
├── backups\
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

- **Claude Code:** `ollama launch claude`, manual `ANTHROPIC_BASE_URL` configuration, model selection, validation, and restore.
- **Codex CLI:** `codex --oss`, `ollama launch codex`, dedicated TOML profiles, model catalogs, validation, and restore.
- **Codex desktop app:** `ollama launch codex-app`, profile persistence, backups, and restore.
- **VS Code:** Native GitHub Copilot inline suggestions when acceptable; Ollama-backed local chat at `http://127.0.0.1:11434`; optional Claude Code and Codex IDE workflows; and a separate `docs/integrations/VS-CODE-LOCAL-AUTOCOMPLETE.md` guide for Continue with `qwen2.5-coder:1.5b-base`.

The local-autocomplete guide includes a decision summary comparing native Copilot suggestions with the optional offline/local path. It covers prerequisites, model pull, Continue configuration, platform-specific paths, validation with a small test file, troubleshooting, disablement, and complete rollback.

`prompts/vscode/setup-local-autocomplete.md` provides a reusable instruction for Codex or Claude Code to perform this optional setup. The prompt requires the LLM to detect the installed Continue configuration schema, back up existing configuration, preserve unrelated settings, request approval before installing the extension or model, avoid changing Ollama's loopback binding, verify ghost-text completion and relevant logs, report every change, and provide rollback steps. Conflicting settings cause the LLM to stop and ask for direction rather than overwrite them.

Regular ChatGPT cannot use Ollama as its model backend. ChatGPT MCP apps require a remote server or Secure MCP Tunnel and therefore are not enabled in this localhost-only design. Claude Cowork also cannot use Ollama as its model backend, and its custom connectors originate from Anthropic's cloud; local MCP servers are unavailable in Cowork. These boundaries are documented with supported local alternatives.

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
2. **Preflight tests:** Platform, prerequisite, storage, port, container engine, GPU/Metal, and permission checks.
3. **Service health:** PostgreSQL readiness, PGVector extension, SearXNG response, Docling API, Ollama API, and Open WebUI health.
4. **Functional fixtures:** Included small text, image, PDF, and audio inputs exercise extraction, vision, RAG, and transcription.
5. **Known-answer RAG:** A fixture is ingested, processing completion is polled, and a known fact must be retrieved with a source reference.
6. **Model verification:** Text output, vision input, tool capability metadata, configured context, and reported GPU/Metal offload.
7. **Persistence:** State is created, services restart, and state remains available.
8. **Idempotency:** Installer and maintenance commands are run again and must report no unintended changes.
9. **Backup/restore rehearsal:** A backup is created and validated in an isolated target.
10. **Final report:** Each test is marked pass, warning, skip, or fail with evidence and remediation.

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
- Optional local VS Code autocomplete guide and reusable setup prompt.
- Security and privacy guide.
- Storage planning and cleanup guide.
- Verification guide and example report.
- Dated current-model/tool research report and refresh method.
- Codex prompt library.

## 14. Research Baseline

The initial research baseline is dated 2026-08-04 and relies on current primary documentation from Ollama, Open WebUI, Rancher Desktop, Docker, Docling, whisper.cpp, OpenAI, Anthropic, and VS Code/Ollama integration documentation. Recommendations must distinguish vendor benchmarks from measurements produced on the user's machines.

The baseline supersedes Qwen2.5-VL-32B with newer workstation-sized multimodal choices, led by Qwen3.6 27B and Gemma 4 26B. The update guide includes a repeatable evaluation template so model defaults can change without restructuring the stack.

## 15. Licensing

Repository-authored scripts and documentation use the MIT License. Third-party software, container images, models, and downloaded artifacts retain their own licenses and terms. The model guide records relevant license links and flags models whose terms differ from permissive open-source licenses.
