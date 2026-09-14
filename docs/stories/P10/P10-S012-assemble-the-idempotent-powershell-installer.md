# P10-S012: Assemble the idempotent PowerShell installer

| Property | Value |
|---|---|
| Story ID | P10-S012 |
| Phase | P10 — Operations and Final Acceptance |
| Sequence | 8 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | LLM |
| Dependencies | P10-S007 |
| Unlocks | P10-S013 |
| Preferred route | Controller-selected architecture route with cross-provider review; qualified local model may assist but cannot be sole reviewer. |
| Research freshness | Current PowerShell, Windows, Ollama, Rancher Desktop, WSL, and installed-component documentation checked within 7 days. |

## 1. User story

As the workstation owner, I want one full PowerShell installer assembled from accepted component operations, so that a clean or repaired workstation can reach the approved state predictably.

## 2. Bounded objective

Assemble the Windows installer entry point and reusable modules from already accepted phase operations, with preflight, plan, dry-run, apply, verification, resume-safe checkpoints, exact logging, and rollback hooks.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P10-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Refresh the official documentation for every command or API invoked by the installer within 7 days. Record versions, dates, links, privilege requirements, deprecations, and conflicts; do not infer current behavior from model memory.

## 5. Preconditions and unlock conditions

P10-S007 and all component installation evidence are accepted; exact versions and digests are recorded; rollback operations exist; Git is clean; the controller lease and Critical-risk authorization checks pass.

## 6. In scope

Installer orchestration, reusable PowerShell modules, configuration inputs, prerequisite detection, storage guards, privilege boundaries, dry-run, structured logs, checkpoints, verification, rollback invocation, and synthetic test fixtures.

## 7. Out of scope and prohibited changes

New component selection, maintenance commands, user documentation beyond command help, hidden downloads, floating versions, secret embedding, auto-installing WSL2 or Rancher Desktop, and destructive cleanup.

## 8. Privilege and human approval

Required — Critical-risk review and the applicable privileged-phase approval are required before any live installer rehearsal. Static, fixture, and dry-run tests may proceed without host mutation.

## 9. Risk rationale

The installer coordinates system configuration across Windows, WSL, storage, networking, and local services. A defect can affect the whole workstation, so isolated rehearsal, precise rollback, owner control, and cross-provider review are mandatory.

## 10. Execution contract

Generate a complete plan before mutation; reject unmet prerequisites and unsafe paths; invoke only accepted component operations; checkpoint every reversible unit; stop on drift; never continue after an unknown partial result; and emit sanitized machine-readable evidence.

## 11. Automated acceptance tests

PowerShell parsing and analysis, unit tests, mocked privilege boundaries, fixture install, safe dry-run, no-op second run, interrupted-run resume, failed-step rollback, storage-limit rejection, secret scan, pinned-version scan, and exact operation inventory all pass.

## 12. Human validation

The owner reviews the generated installation plan and one isolated or non-mutating rehearsal report; live destructive rehearsal remains governed by the final acceptance stories.

## 13. Idempotency and rollback

A second run on the accepted fixture state proposes no unintended change. Each applied unit has a named rollback action, and rollback preserves pre-existing user data and separately installed prerequisites.

## 14. Required evidence

Source revisions; dependency and version manifest; generated plan; analysis and test results; dry-run and second-run outputs; interruption and rollback results; operation and privilege inventory; secret scan; review verdicts; and owner validation.

## 15. Definition of done

The installer can plan, apply in fixtures, verify, safely resume, no-op, and roll back exactly the accepted workstation operations; all Critical controls pass; and P10-S013 is unblocked.

## 16. Pause-safe boundaries

Pause before privilege elevation and after each component checkpoint, verification block, evidence commit, and rollback completion. Finish or revert an atomic operation before pausing.
