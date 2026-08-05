# Local AI Workstation Playbook

An open-source-first plan for building two independent, private local AI workstations: a Windows 11 desktop optimized for an RTX 4090 and a MacBook Pro optimized for Apple silicon and a fixed storage budget.

> [!IMPORTANT]
> **Design complete; implementation not started; not yet installable.**
>
> This repository currently contains approved design specifications. Installers, deployment configuration, operational guides, and verification tooling have not been implemented or tested yet.

## Project goals

The completed playbook is intended to provide:

- Open WebUI as the primary interface.
- Ollama for native model management and inference.
- Local vision, document ingestion, retrieval-augmented generation, speech-to-text, and live web search.
- Rancher Desktop for containerized supporting services without requiring Docker Desktop.
- Independent Windows and macOS installations with localhost-only defaults.
- Idempotent installers, maintenance scripts, verification reports, troubleshooting guidance, and Codex prompt templates.

## Reference hardware

This playbook is designed around the repository owner's personal devices:

| Platform | Reference system | Planned constraints |
|---|---|---|
| Windows 11 | AMD Ryzen 7 9800X3D, NVIDIA RTX 4090 with 24 GB VRAM, 64 GB RAM | Persistent AI data rooted at `H:\ai`; inference and context settings optimized for the RTX 4090 |
| macOS | MacBook Pro with M4 Pro and 48 GB unified memory | Independent installation with a 175 GB storage budget and enough headroom for normal work |

These are reference configurations, not universal hardware requirements. Other users should expect to adjust model sizes, context limits, concurrency, storage paths, and service resource allocations for their available GPU, memory, CPU, and disk capacity. Broader hardware profiles have not yet been tested.

## Planned architecture

The approved design uses native inference with containerized supporting services:

| Component | Planned role |
|---|---|
| Open WebUI | Primary chat, vision, RAG, and speech interface |
| Ollama | Native model management and inference on CUDA or Apple silicon |
| Rancher Desktop | Moby/dockerd runtime for supporting containers, with Kubernetes disabled |
| SearXNG | Live web search integrated with Open WebUI |
| Docling Serve | Structured document extraction |
| PostgreSQL with PGVector | Application data and vector storage |
| Faster-Whisper | Local speech-to-text through Open WebUI |
| whisper.cpp | Optional native transcription workflow |

Each machine is planned as a separate, localhost-only installation. Models, documents, indexes, services, and state will not be shared between the Windows and macOS systems.

## Currently available

- [Local AI Workstation Playbook design specification](docs/superpowers/specs/2026-08-04-local-ai-workstation-playbook-design.md) — approved architecture, constraints, model profiles, data flows, repository structure, operations, and acceptance criteria.
- [Root README design specification](docs/superpowers/specs/2026-08-05-readme-design.md) — approved scope and accuracy requirements for this README.

The design specification is the authoritative source for planned behavior. Technical recommendations will be researched again before implementation because local AI models and tools change quickly.

## Not yet available

The following planned deliverables do not exist yet:

- Windows PowerShell installer and maintenance scripts.
- macOS shell installer and maintenance scripts.
- Rancher Desktop Compose configuration and pinned component versions.
- Windows and macOS installation guides.
- Architecture, model usage, performance tuning, storage, security, troubleshooting, update, backup, restore, and uninstall guides.
- Client integration guidance for Claude Code, Codex, ChatGPT, Claude Cowork, and VS Code.
- Automated static, preflight, service, functional, persistence, idempotency, and backup/restore verification.
- Test fixtures, diagrams, example reports, and Codex CLI prompts.

There are intentionally no installation commands in this README while those assets remain unimplemented.

## Planned repository structure

```text
local-llm-setup/
├── README.md
├── docs/
│   ├── architecture/
│   ├── install/
│   ├── operations/
│   ├── research/
│   └── superpowers/specs/
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
```

Most of these directories will be created during implementation and are shown here only to describe the approved organization.

## Roadmap

- [x] Establish workstation requirements and operating constraints.
- [x] Research the initial architecture, tool choices, and model profiles.
- [x] Approve and publish the project design specification.
- [x] Document the repository's current status and intended contents.
- [ ] Refresh model and tool research immediately before implementation.
- [ ] Implement the shared container stack and pinned version catalog.
- [ ] Implement the Windows installer, scripts, tests, and documentation.
- [ ] Implement the macOS installer, scripts, tests, and documentation.
- [ ] Add client integration guides and usage recommendations.
- [ ] Validate the complete playbook on both reference machines.

See the [full design specification](docs/superpowers/specs/2026-08-04-local-ai-workstation-playbook-design.md) for the detailed scope and acceptance criteria.
