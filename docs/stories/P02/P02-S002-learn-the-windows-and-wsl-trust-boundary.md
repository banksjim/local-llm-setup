# P02-S002: Learn the Windows and WSL trust boundary

| Property | Value |
|---|---|
| Story ID | P02-S002 |
| Phase | P02 — Windows, WSL, Git, and VS Code Foundation |
| Sequence | 2 |
| Status | Planned |
| Step | Learning |
| Hold reason | Dependency |
| Risk | Low |
| Actor | Human + LLM |
| Dependencies | P02-S001 |
| Unlocks | P02-S003 |
| Preferred route | Interface: interactive Codex or Claude Code session; Provider: OpenAI or Anthropic; Model class: general-purpose guide; Effort: low; Fallback: switch provider if the primary interface is unavailable; no model may substitute for human evidence. |
| Research freshness | Current phase research record. |

## 1. User story

As the workstation owner, I want this story to teach only the filesystem, network, credential, process, and rollback concepts needed for this workstation, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Teach only the filesystem, network, credential, process, and rollback concepts needed for this workstation.

## 3. Learning objective

The owner can draw the Windows, Rancher Desktop, `AI-Workbench`, Git credential, and H-drive boundaries; place each planned process and data class correctly; classify safe versus prohibited mount, credential, executable, network, elevation, backup, and rollback scenarios; and explain that WSL reduces accidental host exposure but is not a hostile-code sandbox.

## 4. Current research requirements

Use the accepted P02-S001 research record and its still-current primary sources. Record the P02-S001 evidence revision and recheck any source whose declared freshness window expires before the lesson; a material change returns the story to research rather than teaching stale behavior.

## 5. Preconditions and unlock conditions

P02-S001. Applicable specifications, clean Git state, valid controller state, current research, required model route, and lease checks must pass.

## 6. In scope

A targeted lesson and scenario exercise on Windows versus Ubuntu filesystems, Linux-home repository placement, host/guest networking, credentials, Windows-drive mounts, executable interoperability, elevation, snapshots/exports, and rollback; record the owner's answers in `evidence/P02-S002/owner-learning.md`.

## 7. Out of scope and prohibited changes

General container, Linux-administration, networking, or VS Code training; installing software; creating the WSL distribution; changing security policy; and allowing an LLM-generated paraphrase to stand in for the owner's explain-back.

## 8. Privilege and human approval

Required human learning — the owner completes the scenarios and explain-back. This records learning under the P02 phase authorization; it is not a second approval, and the LLM cannot create the answers.

## 9. Risk rationale

The lesson is Low risk because it uses diagrams and synthetic scenarios and writes only learning evidence. It performs no privileged action and grants no phase authorization.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the lease; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the lease; and route to review or human validation. The owner completes a diagram exercise and identifies which operations stay in Windows versus Ubuntu.

## 11. Automated acceptance tests

The owner completes a diagram exercise and identifies which operations stay in Windows versus Ubuntu. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass. A justified not-applicable test is recorded rather than omitted.

## 12. Human validation

The owner draws or annotates the boundary diagram, classifies the supplied scenarios, and explains the limits of WSL in their own words. The LLM records but cannot author the explain-back.

## 13. Idempotency and rollback

The lesson may be repeated without machine changes. New attempts append a dated score and preserve earlier owner answers; rollback reverts only the learning-evidence commit.

## 14. Required evidence

Lesson revision and P02-S001 source set; interface/provider/model/effort; the owner's ungenerated answers; scored decisions for safe and unsafe file, credential, network, interop, elevation, and rollback scenarios; questions needing clarification; completion timestamp; and owner acknowledgement.

## 15. Definition of done

The owner correctly explains where code and AI data live, why Windows tokens are not shared into Ubuntu, what WSL does and does not isolate, how VS Code crosses the boundary, and when export or rollback is required. The evidence is genuine and P02-S003 is unblocked.

## 16. Pause-safe boundaries

Pause between lesson modules or scenarios and before owner acknowledgement. Save the owner's original answer before feedback; incomplete modules remain Waiting rather than inferred complete.
