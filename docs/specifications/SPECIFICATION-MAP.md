# Specification Map

**Status:** Approved design being prepared for user review  
**Last reviewed:** 2026-09-15

This directory is the authoritative specification set for the Local AI Workstation Playbook. Runtime behavior is defined by the approved specifications, story documents, accepted evidence, and controller state retained in the active repository.

## Reading order

1. [Master program specification](program/LOCAL-AI-AGENTIC-WORKSTATION-PROGRAM.md)
2. [Canonical story contract](standards/STORY-CONTRACT.md)
3. [Phase specifications](phases/PHASE-MAP.md)
4. [System specifications](systems/SYSTEM-MAP.md)
5. [Sequenced story documents](../stories/STORY-BACKLOG.md)

## Authority

When documents disagree, use this order:

1. The latest owner-approved program specification.
2. The applicable system specification.
3. The applicable phase specification.
4. The activated story revision.
5. Accepted evidence and runtime checkpoints.
6. GitHub issues and GitHub Projects as synchronized presentation layers.
7. Chat history as context only.

Implementation may not begin merely because these files exist. Until the controller is trusted, the owner must explicitly authorize each story. Once trusted, only `goagentic go` authorizes the next bounded execution interval.
