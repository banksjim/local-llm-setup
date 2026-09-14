# P09-S013: Deploy the selected private memory foundation

| Property | Value |
|---|---|
| Story ID | P09-S013 |
| Phase | P09 — Durable Agent Memory |
| Sequence | 4 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | LLM |
| Dependencies | P09-S003 |
| Unlocks | P09-S004 |
| Preferred route | Interface: WSL coding agent through goagentic deployment; Provider: controller-selected cloud provider; Model class: high-reliability operations; Effort: high; Fallback: restore P08/P04 checkpoints and defer P09 without memory. |
| Research freshness | Selected framework, images, storage, authentication, encryption, upgrade, Ollama, and advisory docs checked within 7 days. |

## 1. User story
As the owner, I want a private, reproducible memory foundation before any personal memory is captured.
## 2. Bounded objective
Create workloads/agents/memory/foundation/ and operations/windows/p09/P09-S013-deploy-memory-foundation/ to deploy pinned selected components beneath `H:\ai\agents\memory` with private networking, external secrets, health, backup, update, and removal operations.
## 3. Learning objective
Not applicable — P09-S003 covers the selected foundation.
## 4. Current research requirements
Resolve immutable versions/digests, transitive services, license, telemetry, migrations, local-model endpoints, encryption/key recovery, and resource limits; reject material drift from the ADR.
## 5. Preconditions and unlock conditions
P09-S003 is Done. The revision-bound P09 authorization fixes exact changes, ports, identities, volumes, key custody/recovery, models, networks, limits, tests, and rollback checkpoint.
## 6. In scope
Framework adapter skeleton; dedicated least-privilege database/schema and projection identities; private API/admin path; authentication; secrets; encryption if selected; Ollama gateway; persistence; health; telemetry off; synthetic store; and lifecycle operations.
## 7. Out of scope and prohibited changes
No P08 integration, real conversation/private memory, public/LAN bind, cloud sync/model, vendor account, auto-retain, global namespace, Docker socket, arbitrary host mount, or shared database credential.
## 8. Privilege and human approval
The explicit revision-bound P09 phase authorization covers this deployment. Any component, data class, network, key-custody, or cloud change requires a new preview and approval.
## 9. Risk rationale
Critical: persistent private-data infrastructure, credentials, encryption recovery, and an access-control boundary are created. Revision-bound authorization, isolated rehearsal, cross-provider review, and P09-S012 owner acceptance are mandatory.
## 10. Execution contract
Rehearse in an isolated synthetic namespace; preflight storage/ports/resources; checkpoint services; deploy immutable artifacts; inject secrets; verify private binds/auth/encryption/telemetry-off; test migration/restart/backup/restore/removal/no-op; scan logs/config; and cross-provider review.
## 11. Automated acceptance tests
Prove anonymous/public/LAN/cross-service access fails; wrong key/model/dimension/migration fails closed; secrets and synthetic values do not leak; outage does not affect P08; restart/restore matches hashes; duplicate deploy is no-op. Inject occupied port, full/read-only disk, corrupt data/key/backup, bad digest, failed health, and interrupted migration; reconcile or restore.
## 12. Human validation
Not applicable — the owner operates the completed system in P09-S012.
## 13. Idempotency and rollback
Same activation is a no-op. Rollback removes only P09 services/identities/synthetic data and restores P04/P08 checkpoints; key recovery is rehearsed before any real data.
## 14. Required evidence
evidence/P09-S013/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, review.md, deployment-manifest.json, security-scan.json, key-recovery.json, failure-injection.json, and restore-results.json.
## 15. Definition of done
The foundation is private, authenticated, resource-bounded, recoverable, idempotent, telemetry-clean, independently reviewed, and contains synthetic data only.
## 16. Pause-safe boundaries
Update evidence/P09-S013/checkpoint.json before deployment and after migration, health, failure, restore, and rollback gates; never pause mid-migration or with an exposed/unknown key state.
