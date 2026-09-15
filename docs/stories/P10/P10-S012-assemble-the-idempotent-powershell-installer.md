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
| Preferred route | Interface: Codex CLI on Windows and AI-Workbench through goagentic; Provider: high-reliability cloud provider; Model class: PowerShell systems integration; Effort: high; Fallback: Anthropic architecture/coding model with cross-provider review and isolated rehearsal. |
| Research freshness | Current PowerShell, Windows, WSL, Rancher Desktop, Ollama, and every invoked component interface checked within 7 days. |

## 1. User story
As the owner, I want one full PowerShell installer that predictably composes the accepted work without hiding what it will change.
## 2. Bounded objective
Create `installer/windows/Install-LocalAIWorkstation.ps1`, `LocalAIWorkstation.psm1`, `installer.schema.json`, `installer.example.yaml`, and `operation-map.yaml` by composing accepted P02–P09 and P10 operation entry points.
## 3. Learning objective
Not applicable — P10-S002 and the later install guide cover owner-facing use.
## 4. Current research requirements
Verify syntax/API, supported PowerShell runtime, external command behavior, checksums/signatures, elevation, exit codes, and `ShouldProcess` behavior. Record the cross-module `WhatIf` limitation and prove preview at the orchestration boundary.
## 5. Preconditions and unlock conditions
P10-S007 and all component operation evidence are accepted; exact dependencies/versions/digests, free-space formula, prerequisite ownership, rollback hooks, and P10 authorization are resolved.
## 6. In scope
Preflight; configuration validation; Windows 11/CPU/RAM/RTX 4090/H-drive checks; WSL2 and Rancher Desktop present/running checks without installing them; Git prerequisite check; storage plan; complete mutation plan; dry-run; dependency ordering; elevation boundaries; checkpoint/resume; structured sanitized logs; verify; rollback dispatch; and nonzero operation inventory.
## 7. Out of scope and prohibited changes
No WSL2, Rancher Desktop, or Git installation; no new component selection; no floating versions; no secret embedding/argument/logging; no duplicated component logic; no automatic destructive cleanup, driver/BIOS/OS update, backup-destination choice, or public exposure.
## 8. Privilege and human approval
Covered by P10 authorization. Static/fixture/dry-run tests do not mutate; owner handles bounded elevation or GUI-only prerequisites in live use. Changed operation map or targets requires a new preview.
## 9. Risk rationale
Critical: this orchestrates broad privileged changes across Windows, WSL, storage, networking, and private services. P10 phase authorization, isolated installer rehearsal, cross-provider review, and P10-S011 final owner acceptance are mandatory.
## 10. Execution contract
Validate schema and canonical paths; discover before plan; show all actions/privilege/data/network/storage impacts; require prerequisites; download only verified pinned artifacts; call one authoritative operation per step; checkpoint after verify; stop on drift/unknown partial result; roll back reverse-dependency units; emit a final actual-versus-planned report.
## 11. Automated acceptance tests
PowerShell parse, strict mode, PSScriptAnalyzer, schema, command help, mocked prerequisites/elevation/downloads/restarts, empty-operation rejection, storage rejection, H-drive containment, signature/digest rejection, secret scan, dry-run zero mutation, fixture apply, no-op second run, interruption at every checkpoint, resume, failed-step reverse rollback, operation-map completeness, and prohibited-operation scan pass on supported PowerShell versions.
## 12. Human validation
Owner reads a generated sample plan and isolated/nonmutating rehearsal report and can identify prerequisites, destination, storage, privilege points, and stop/rollback choice without this chat.
## 13. Idempotency and rollback
Same configuration on accepted state plans no change. Every applied unit records before-state and named rollback; rollback preserves pre-existing user data and separately installed prerequisites.
## 14. Required evidence
Commit installer artifacts/tests plus `evidence/P10-S012/activation.json`, dependency/version manifest, operation map, plan, analysis, fixture/dry-run/no-op/interruption/resume/failure/rollback results, storage and secret checks, human validation, cross-provider review, and `checkpoint.json`.
## 15. Definition of done
The installer safely plans, fixture-applies, verifies, resumes, no-ops, and reverses the exact accepted operation graph with no duplicate implementation; owner plan comprehension and all Critical controls pass; P10-S013 unlocks.
## 16. Pause-safe boundaries
Pause before elevation/download/apply and after each verified operation checkpoint or completed rollback; never pause during an atomic external mutation.
