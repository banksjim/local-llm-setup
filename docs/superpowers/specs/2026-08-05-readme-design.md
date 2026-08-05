# Root README Design Specification

**Date:** 2026-08-05  
**Status:** Approved for implementation  
**Repository:** `banksjim/local-llm-setup`

## Objective

Create a concise root `README.md` that explains the Local AI Workstation Playbook, accurately inventories the repository's current contents, and makes the project's present status unmistakable.

## Audience

The README is for the repository owner, prospective users, and contributors who need to understand the intended workstation setup and determine whether usable installation assets exist yet.

## Required Structure

The README will contain:

1. The product name and a short purpose statement.
2. A prominent GitHub admonition stating: **Design complete; implementation not started; not yet installable.**
3. A concise summary of the two independent target systems:
   - Windows 11 desktop with Ryzen 7 9800X3D, RTX 4090, 64 GB RAM, and planned persistent storage under `H:\ai`.
   - MacBook Pro with M4 Pro, 48 GB unified memory, and a 175 GB storage budget.
4. The planned open-source-first stack: Open WebUI, native Ollama, Rancher Desktop, SearXNG, Docling Serve, PostgreSQL with PGVector, Faster-Whisper, and optional whisper.cpp.
5. A **Currently available** section listing and linking to the approved design specification.
6. A **Not yet available** section explicitly identifying the unimplemented installers, maintenance scripts, deployment configuration, platform guides, model guides, verification tests, diagrams, and Codex prompt library.
7. A compact planned repository-structure summary.
8. A roadmap checklist that distinguishes the completed design phase from future implementation and validation work without assigning dates.
9. A direct link to the complete design specification for authoritative detail.

## Accuracy Rules

- Do not provide installation commands while no installer exists.
- Do not claim that any service, model, script, configuration, or workflow has been implemented or tested.
- Describe all unbuilt technical choices as planned or proposed.
- Do not use release, build, test, or coverage badges that imply working software.
- Do not promise delivery dates.
- Do not add license, contributing, or changelog sections; those belong in dedicated files when created.

## Style

- Use concise GitHub Flavored Markdown.
- Lead with status and practical orientation rather than promotional language.
- Use tables or lists only where they improve scanning.
- Avoid excessive headings, badges, and emoji.
- Keep the README useful as the repository grows by linking to detailed documents rather than duplicating the full design specification.

## Acceptance Criteria

The README is complete when a new visitor can answer all of these questions without opening another file:

- What is this project intended to become?
- Which Windows and macOS machines does it target?
- What stack is planned?
- What content exists in the repository today?
- What has not been implemented yet?
- Where is the authoritative design specification?

All links must resolve within the repository, Markdown must render cleanly on GitHub, and the working tree must contain no unrelated changes.
