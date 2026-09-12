# Obsolete Memory Integration Cleanup Design

## Purpose

Remove the abandoned cross-project memory integration from the Local AI Workstation Playbook so the repository describes only systems that exist or are deliberately included in this project.

## Scope

- Delete the dedicated personal-agents memory-integration design dated 2026-08-11.
- Remove references to AIOS, its reviewed inbox, candidate-memory promotion, and related future integration deliverables from the README and master workstation specification.
- Preserve useful standalone personal-agent model and usage recommendations.
- Do not introduce a replacement memory architecture.
- Do not rewrite Git history.

## Repository-Local Memory

Search hidden repository files, including `.superpowers`, for the obsolete project name and memory-contract terminology. Remove matches if any are found. Files and memory outside this repository are not in scope.

## Verification

After cleanup:

1. The obsolete design file no longer exists.
2. A case-insensitive search of current repository files, excluding `.git`, finds no references to the obsolete project name, reviewed inbox, candidate-memory workflow, or durable-promotion contract.
3. The README and master specification remain internally consistent.
4. Git history remains unchanged apart from normal additive cleanup commits.
5. This temporary cleanup design is removed so it cannot preserve the obsolete terminology in the final working tree.
