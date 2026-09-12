# Interactive Architecture Walkthrough — Design Specification

**Date:** 2026-09-11
**Status:** Awaiting written-spec review
**Repository:** `local-llm-setup`

## Objective

Replace the stale local brainstorming preview with a reusable interactive walkthrough of the September 2026 Local AI Workstation Playbook architecture. The walkthrough teaches the owner how the components fit together and supports lightweight review feedback without becoming part of the installed AI stack.

## Location and Lifecycle

- A new visual-companion session is created beneath `.superpowers/brainstorm/`; the August session is retained as historical local state.
- The walkthrough is generated as a new HTML fragment and served through the Superpowers brainstorming preview server.
- `.superpowers/` remains ignored by Git. The durable source of truth is the approved Markdown architecture specification, not the generated preview.
- The local preview server binds to loopback, records clicks in the session `state/events` file, and stops automatically after inactivity.

## Walkthrough Content

The single-page walkthrough contains:

1. A short “How to use this page” panel.
2. A Windows host zone containing native Ollama, RTX 4090 inference, Rancher Desktop services, Open WebUI, and the inference-only Caddy gateway.
3. A dedicated Ubuntu WSL2 agent zone containing VS Code workspace extensions and terminals, Codex CLI, Claude Code, the harness, Linux Git credentials, repositories, and per-agent Git worktrees.
4. Explicit allowed and denied paths: inference through gateway port `11435` is allowed; direct Ollama administration, Windows-drive automounts, Windows executable interoperability, Rancher Desktop control, and unapproved host paths are denied by the hardened default.
5. A multi-agent sequence showing worker allocation, queued RTX 4090 inference, isolated worktrees, review, and merge.
6. A separate MacBook Pro architecture showing its independent native Ollama and container stack.
7. Model cards for Qwen3.8 27B primary/quality work, Qwen3.5 9B fast and multi-agent work, Qwen3 Embedding 0.6B, optional Qwen2.5 Coder 1.5B autocomplete, Gemma 4 alternate, and Muse Glimmer evaluation.
8. Clickable checkpoints for “Architecture understood,” “Needs explanation,” and “Ready to proceed.”

## Interaction and Usage

- The page explains that clicking a checkpoint records local feedback but does not install software or change the architecture.
- The user returns to the Codex task after clicking and describes any requested change in ordinary language.
- To reopen a stopped review, the user asks Codex: “Open the Local AI Workstation architecture walkthrough.” Codex starts a fresh local preview session and regenerates the current walkthrough from the durable specification.
- The browser URL is temporary. The Markdown specification and generated HTML remain available after the preview server stops.

## Visual Treatment

- Use a compact, readable dark-theme layout supplied by the visual-companion frame.
- Use distinct visual zones for Windows, Ubuntu WSL2, and macOS.
- Use green for allowed data paths, amber for review or resource constraints, and red for denied security-boundary paths.
- Favor architecture clarity over decorative detail. The page must remain legible at ordinary desktop width without requiring prior technical knowledge.

## Failure Handling

- If an existing session contains `state/server-stopped`, create a new session rather than modifying or pretending to revive it.
- Never reuse an existing screen filename.
- If the server cannot start, preserve the generated HTML and report the manual recovery path.
- If browser clicks are unavailable, terminal feedback remains authoritative.

## Verification

The walkthrough is complete when:

1. The preview server reports a loopback URL and serves the new page.
2. The page contains every component and boundary listed above.
3. No Qwen3.6 recommendation or mirrored-networking default remains.
4. A checkpoint click appears in the session event log.
5. The page states that it is local, ignored by Git, non-installing, and disposable.
6. The repository remains unchanged except for this tracked specification; generated `.superpowers` content remains ignored.

