# Local AI Workstation Playbook

An open-source-first, Git-based program for building a private local AI and agent-development workstation. The active plan is tailored to the repository owner's Windows 11 desktop: Ryzen 7 9800X3D, RTX 4090 with 24 GB VRAM, 64 GB RAM, and persistent AI storage under `H:\ai`.

> [!IMPORTANT]
> **The specification and story backlog exist; implementation has not started.**
>
> This repository is not currently an installer. Do not treat planned commands, versions, or acceptance criteria as completed or verified workstation behavior.

## What is planned

- Open WebUI as the main local AI interface.
- Native Ollama model management and RTX 4090 inference.
- Rancher Desktop with Moby/dockerd for supporting containers; Kubernetes disabled.
- SearXNG search, Docling extraction, PostgreSQL with PGVector, and self-hosted MLflow.
- Windows-wide local desktop dictation selected by an actual comparison of current OSS applications.
- VS Code on Windows connected to a dedicated, hardened Ubuntu WSL2 agent and development environment.
- Python, Go, Node.js, and TypeScript development.
- Codex CLI, Claude Code, and accurately documented desktop-client integrations.
- LangChain, LangGraph, MCP, skills, assets, scripts, tracing, and evaluations for real agents.
- Multi-format private RAG ingestion using Docling, Crawl4AI, Google Workspace exports, YAML-frontmatter Markdown, and local vision enrichment.
- A substantial personal knowledge-base capstone.
- Thought-partner, life-planning, fitness, financial-education, and daily-check-in agents.
- An OSS durable-memory system with a reviewed candidate inbox.
- Idempotent installers and complete verification, tuning, troubleshooting, update, backup, restore, and removal guidance.

## Start here

1. Read the [master program specification](docs/specifications/program/LOCAL-AI-AGENTIC-WORKSTATION-PROGRAM.md).
2. Review the [phase map](docs/specifications/phases/README.md).
3. See the [132 sequenced stories](docs/stories/README.md).
4. Read the [canonical story contract](docs/specifications/standards/STORY-CONTRACT.md).

The specifications are designed so a future `goagentic` controller can reconstruct the project after a reboot or long pause and give exactly one safe next action. That controller does not exist yet; it is built and accepted in Phase P01. The first P01 story creates the personal GitHub Project and imports the approved backlog, so progress becomes visible before controller or workstation implementation begins.

## Program phases

| Phase | Scope |
|---|---|
| P01 | Project controller and quality foundation |
| P02 | Windows, WSL, Git, VS Code, and development toolchains |
| P03 | Ollama, RTX 4090 model selection, benchmarking, and qualification |
| P04 | Open WebUI and supporting AI services |
| P05 | Desktop dictation and development-tool integrations |
| P06 | LangChain, LangGraph, MCP, skills, and MLflow agent foundation |
| P07 | RAG, ingestion, and personal knowledge-base capstone |
| P08 | Practical personal agents |
| P09 | Durable reviewed agent memory |
| P10 | Security, operations, performance, recovery, and final acceptance |

Targeted human learning stories precede every major concept. Human authentication, privileged changes, experiential testing, and acceptance are separate, visible stories.

## Hardware and portability

These recommendations are specifications for the owner's personal hardware, not universal requirements. Other users must reassess model size, context, concurrency, storage, GPU offload, service resources, and thermal headroom.

The independent M4 Pro MacBook Pro installation is deliberately deferred to a later program. Its previously stated 175 GB budget remains a future constraint, but there are no active macOS implementation stories in this Windows program. That future program will remain independently executable while allowing documented Windows learning to receive prior-learning credit after a current-version and macOS-delta check; Mac-specific learning cannot be skipped.

## Private knowledge-base boundary

This playbook repository is public and contains only specifications and, later, synthetic fixtures. Real source documents and Docling JSON will live outside Git. Final generated Markdown and meaningful visual assets will live in separate local knowledge-base repositories that may only use private personal or business-organization remotes after explicit approval.

## Current status

- Requirements and major architecture decisions: complete for review.
- Master, system, phase, and story specifications: drafted.
- Formal adversarial review: [remediation in progress](docs/reviews/2026-09-13-formal-specification-review.md); P01-P05 have passed their bounded batch reviews and P06 has completed its first Batch 3 correction cycle, while P07-P10 and the final Batch 3/full-program review remain blocking.
- GitHub Project creation and controller implementation: not started.
- Workstation installation and testing: not started.
- macOS program: deferred.

Technical recommendations are refreshed from current documentation when each story activates. The project does not assume that a model, tool, extension, version, or tutorial remains current simply because it appears in this repository.

## About the removed `superpowers` folder

The active repository no longer uses `.superpowers` or `docs/superpowers`. Those were temporary planning and browser-walkthrough artifacts, not a runtime capability or requirement. Their useful decisions were incorporated into the ordinary Markdown specifications, tables, and Mermaid diagrams under `docs/`; their prior versions remain available only through Git history.
