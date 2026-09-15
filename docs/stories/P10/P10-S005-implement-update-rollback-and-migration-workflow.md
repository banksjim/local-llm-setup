# P10-S005: Implement update, rollback, and migration workflow

| Property | Value |
|---|---|
| Story ID | P10-S005 |
| Phase | P10 — Operations and Final Acceptance |
| Sequence | 5 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | LLM |
| Dependencies | P10-S004 |
| Unlocks | P10-S006 |
| Preferred route | Interface: Codex CLI across Windows and AI-Workbench through goagentic; Provider: high-reliability cloud provider; Model class: migration and recovery implementation; Effort: high; Fallback: Anthropic architecture-capable model with cross-provider review and isolated rehearsal. |
| Research freshness | Official release, migration, compatibility, and rollback documentation for every affected component checked at activation and again before apply. |

## 1. User story
As the owner, I want one controlled lifecycle workflow so updates cannot silently break databases, models, integrations, or recovery.
## 2. Bounded objective
Implement `operations/windows/p10/P10-S005-lifecycle/` with `Get-UpdatePlan.ps1`, `Invoke-ComponentUpdate.ps1`, `Test-UpdatedSystem.ps1`, and `Invoke-UpdateRollback.ps1`, plus `config/releases/windows-lock.yaml` and `tests/p10/lifecycle/`.
## 3. Learning objective
Not applicable — P10-S002 teaches preview, apply, and stop boundaries.
## 4. Current research requirements
Resolve stable versions/digests, supported upgrade order, breaking changes, schema migrations, downgrade limits, signature/checksum sources, driver/runtime compatibility, and release provenance. Never select preview releases by default.
## 5. Preconditions and unlock conditions
P10-S004 is Done; P10-S001 matrix is refreshed; exact current/target identities, database backups, free-space requirement, health probes, migration steps, rollback point, and expected downtime are in the activation packet.
## 6. In scope
Ollama, pinned models/manifests, Rancher Desktop settings and stable version, container images by digest, Open WebUI, SearXNG, Docling, Langflow, PostgreSQL/PGVector, MLflow, agent/runtime dependencies, memory foundation, dictation/tool integrations, and controller compatibility. Windows, BIOS, and GPU-driver updates are reported but not automatically applied.
## 7. Out of scope and prohibited changes
No floating tags, unattended schedule, blind bulk update, preview/alpha adoption, OS/BIOS/driver mutation, update without consistent backup, or claiming that image rollback reverses migrated data.
## 8. Privilege and human approval
Covered by P10 authorization. Owner participates at elevation/restart or UI-only boundaries. A new component, unsupported migration, or changed destructive scope requires a new preview.
## 9. Risk rationale
Critical: coordinated updates can migrate or corrupt multiple private services and make downgrade impossible. P10 phase authorization, isolated migration/restore rehearsal, cross-provider review, and P10-S011 final owner acceptance are mandatory.
## 10. Execution contract
Inventory and compare; verify provenance; calculate space; create application-consistent backup; stop dependents; update one dependency-ordered unit; run its migration and probes; checkpoint; stop on first failure; choose tested forward-fix or restore—not an improvised downgrade; emit no secrets.
## 11. Automated acceptance tests
Fixtures prove no-op current state, valid signed/digested update, rejected floating/preview/unverified artifact, insufficient-space stop, dependency ordering, interrupted download, failed health probe, failed schema migration, pre-migration restore, and full rollback. Every inventory row maps to a supported lifecycle action or explicit manual/report-only result; second run no-ops.
## 12. Human validation
Owner reviews a plain-language plan showing versions, downtime, storage, backup, irreversible boundaries, and rollback before the isolated rehearsal; no technical certification is required.
## 13. Idempotency and rollback
Plans are read-only; repeated successful apply no-ops. Rollback restores the pre-update configuration/data pair and version/digest set in isolation, preserving unrelated data.
## 14. Required evidence
Commit operations/config/tests plus `evidence/P10-S005/activation.json`, `inventory-before.json`, `update-plan.json`, `provenance.json`, `backup-reference.json`, scenario results, `inventory-after.json`, `second-run.json`, `rollback.json`, `human-validation.md`, `cross-provider-review.md`, and `checkpoint.json`.
## 15. Definition of done
Every accepted component has a tested lifecycle disposition; success, failure, interruption, migration, no-op, and recovery behave as specified; the owner can read the plan; and P10-S006 unlocks.
## 16. Pause-safe boundaries
Pause before backup, service stop, artifact apply, migration, or restore, and after a verified checkpoint. Never pause mid-migration or with an unknown partial result.
