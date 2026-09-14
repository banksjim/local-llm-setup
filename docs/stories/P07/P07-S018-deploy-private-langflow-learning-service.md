# P07-S018: Deploy the private Langflow learning service

| Property | Value |
|---|---|
| Story ID | P07-S018 |
| Phase | P07 — RAG, Ingestion, and Knowledge-Base Capstone |
| Sequence | 3 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P07-S002 |
| Unlocks | P07-S003 |
| Preferred route | Interface: WSL coding agent through goagentic deployment; Provider: controller-selected cloud provider; Model class: high-reliability operations; Effort: high; Fallback: restore prior Rancher configuration and use a disposable documented local process for the lesson. |
| Research freshness | Current Langflow stable deployment, authentication, persistence, API, environment-variable, backup, and security documentation checked within 7 days. |

## 1. User story

As the owner, I want a private, reproducible Langflow learning service so the next lesson is hands-on and the later capstone has a tested administrative surface.

## 2. Bounded objective

Create workloads/rag/langflow/service/ and reusable operation operations/windows/p07/P07-S018-deploy-private-langflow to deploy a pinned Rancher Desktop service with private persistence, externalized secrets, localhost-only owner access, health checks, export/import, backup, and removal.

## 3. Learning objective

Not applicable — this automated prerequisite creates the safe surface used by P07-S003; the owner learns Langflow there before building the capstone.

## 4. Current research requirements

Resolve the stable image/package version and digest, license, database/persistence requirements, authentication controls, supported run API, environment variables, upgrade path, and disclosed vulnerabilities. Reject an image that cannot meet the private binding and secret requirements.

## 5. Preconditions and unlock conditions

P07-S002 is Done. The activation packet names image digest, ports, hostname/bindings, volume locations under the accepted H-drive Rancher data boundary, service identity, secret references, health endpoint, resource limits, and prior Rancher checkpoint.

## 6. In scope

Dedicated service definition, persistent application data, owner-only local UI, network-isolated service API, generated credential in host secret storage, health/readiness, synthetic starter flow, export/import, log redaction, upgrade checkpoint, backup, and uninstall operation.

## 7. Out of scope and prohibited changes

No public/LAN binding, shared default password, credential in repository or compose output, private knowledge source mount, arbitrary custom components, production corpus, Open WebUI integration, cloud model/API, or reuse of another service's database identity.

## 8. Privilege and human approval

The revision-bound P07 authorization covers the previewed Rancher service, private volume, port, and secret creation. No additional owner action is required unless Rancher prompts for host elevation.

## 9. Risk rationale

High: a persistent local service and credential are created and container/network configuration changes, but no real private corpus is mounted.

## 10. Execution contract

Preflight port and storage; create a checkpoint; deploy by immutable digest; generate/store the secret outside Git; bind UI to loopback and API only to the approved private network; load the synthetic flow; verify health/auth/export/import/restart; scan logs and configuration; and expose idempotent start, stop, status, backup, restore, update, and remove operations.

## 11. Automated acceptance tests

Prove unauthenticated access fails; loopback UI succeeds with injected secret; LAN/public bind is absent; private source roots are not mounted; only approved service peers reach the API; secret scans are clean; synthetic flow survives restart and export/import; duplicate deploy is a no-op. Inject occupied port, missing secret, read-only volume, bad digest, unhealthy container, corrupt export, and interrupted deployment; each restores or retains the checkpoint.

## 12. Human validation

Not applicable — the owner uses the UI in P07-S003. Technical deployment receives integration and cross-provider review.

## 13. Idempotency and rollback

Repeated deploy with the same digest/config reports no change. Rollback stops/removes only the story service and restores the prior Rancher checkpoint; backup preserves the synthetic flow but excludes secrets.

## 14. Required evidence

The directory evidence/P07-S018/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, and review.md in addition to the story-specific artifacts below.

Image digest/license, port/mount/network/identity inventory, authentication and seven failure results, secret/log scan, restart/export/import hashes, second-deploy result, backup/restore and rollback rehearsal, and reviewer findings at evidence/P07-S018/.

## 15. Definition of done

The private service is healthy, authenticated, persistent, non-public, repeatable, recoverable, and ready for the targeted lesson; P07-S003 becomes Ready.

## 16. Pause-safe boundaries

Before every pause, update evidence/P07-S018/checkpoint.json with completed unit, verified state, active model/provider, safe rollback point, and exact next operation.

Pause before deployment or after health/checkpoint evidence. An interrupted deployment must be fully reconciled or rolled back before pausing.
