# P02-S001: Refresh Windows and WSL foundation guidance

| Property | Value |
|---|---|
| Story ID | P02-S001 |
| Phase | P02 — Windows, WSL, Git, and VS Code Foundation |
| Sequence | 1 |
| Status | Planned |
| Step | Research |
| Hold reason | Phase Not Activated |
| Risk | Low |
| Actor | LLM |
| Dependencies | P01-S014 |
| Unlocks | P02-S002 |
| Preferred route | Interface: Codex desktop or CLI with web access; Provider: OpenAI; Model class: economical research; Effort: low; Fallback: Claude Code with an Anthropic general-purpose model at low effort, escalating only unresolved architecture conflicts. |
| Research freshness | Microsoft, Rancher Desktop, GitHub, and VS Code sources checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to record current supported Windows, WSL, Rancher Desktop prerequisites, networking, filesystem, and VS Code integration guidance, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Record current supported Windows, WSL, Rancher Desktop prerequisites, networking, filesystem, and VS Code integration guidance.

## 3. Learning objective

Not applicable — this research story prepares the evidence used by the following learning gate and does not teach an owner-operated procedure.

## 4. Current research requirements

Microsoft, Rancher Desktop, GitHub, and VS Code sources checked within 7 days. Record access date, version, direct links, material claims, conflicts, and inferences. Do not rely on model training memory for changeable facts.

## 5. Preconditions and unlock conditions

P01-S014. Applicable specifications, clean Git state, valid controller state, current research, required model route, and lease checks must pass.

## 6. In scope

Create `evidence/P02-S001/foundation-research.md` plus a decision matrix covering supported Windows 11 and WSL prerequisites, the current Ubuntu release choice, WSL distribution storage/relocation methods, Rancher Desktop compatibility, GPU/network behavior, automount/interoperability controls, VS Code Remote WSL requirements, and known conflicts with the fixed P02 boundaries.

## 7. Out of scope and prohibited changes

Installing or changing Windows, WSL, Ubuntu, Rancher Desktop, drivers, VS Code, Git, networking, or security settings; relying on community guidance where current primary documentation exists; and silently changing `AI-Workbench`, `H:\ai`, credential separation, or the no-automount boundary.

## 8. Privilege and human approval

Not applicable — research and read-only inventory require no privileged action. Any live check requesting elevation, configuration, or authentication stops and is assigned to its later story.

## 9. Risk rationale

The story is Low risk because it performs current-documentation research and read-only capability checks and writes only Git evidence. Any live check requiring elevation, installation, authentication renewal, or configuration stops and becomes an owner-visible requirement for a later story.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the lease; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the lease; and route to review or human validation. All recommendations cite current first-party sources and identify changes from the design baseline.

## 11. Automated acceptance tests

All recommendations cite current first-party sources and identify changes from the design baseline. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass. A justified not-applicable test is recorded rather than omitted.

## 12. Human validation

Not applicable — the story is read-only research. Independent review verifies source currency and compatibility; any design conflict requiring owner choice blocks P02-S002 and creates a decision action.

## 13. Idempotency and rollback

Rerunning refreshes the dated matrix without changing the machine. Rollback reverts only `evidence/P02-S001/`; changed recommendations remain inspectable in Git history.

## 14. Required evidence

Story revision; interface/provider/model class/effort; OS and installed-tool read-only inventory; official source URLs, versions, and access dates; claim-to-source matrix; conflicts and inferences; recommended supported Ubuntu and WSL storage method; compatibility verdict for every fixed boundary; rerun comparison; and independent review.

## 15. Definition of done

Every named prerequisite and boundary has a current primary source or is explicitly marked unknown; the chosen Ubuntu and relocation method are supported together; VS Code and hardening requirements contain no unresolved contradiction; no machine state changed; and P02-S002 is unblocked.

## 16. Pause-safe boundaries

Pause between vendor or source families, after each compatibility decision, and before committing the matrix. Preserve unresolved conflicts as blockers; do not synthesize a platform choice while source evidence is incomplete.
