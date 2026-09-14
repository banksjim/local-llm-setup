# P04: Open WebUI and Supporting AI Services

**Depends on:** P03  
**Required outcome:** A pinned, localhost-only Rancher Desktop stack with Open WebUI, PostgreSQL and PGVector, SearXNG, Docling, and MLflow foundations.  
**Status:** Planned

## Fixed architecture and execution boundary

- Use the stable Rancher Desktop release current at activation, the Moby (`dockerd`) engine, and Docker Compose. Kubernetes and WebAssembly remain disabled. Only the `AI-Workbench` WSL distribution receives the required Docker socket integration.
- Run Open WebUI as the primary user interface. Bind every host-published UI/API port explicitly to `127.0.0.1`; use a private Compose network for service-to-service traffic and do not publish PostgreSQL or PGVector.
- Pin images by immutable digest after verifying upstream release provenance. Keep nonsecret configuration in `operations/windows/p04/compose`; keep secret values in an ignored local environment file created from a committed template. Never write credentials to evidence, Git, command arguments, or screenshots.
- Keep Rancher Desktop's growing `rancher-desktop-data` WSL distribution beneath `H:\ai\containers\rancher-desktop-data`, using the activation-verified Microsoft/Rancher-supported move method and a verified export before any destructive fallback. Relocate Rancher snapshots to `H:\ai\containers\rancher-desktop-snapshots` only through Rancher's documented Windows link method. A factory reset may recreate data on the system drive, so every reset or upgrade verification must re-check the actual distribution and snapshot paths.
- Use named, labeled volumes inside the relocated Rancher data distribution plus story-owned logical backup exports under `H:\ai\backups\p04`; do not place live PostgreSQL files in a Windows bind mount. PostgreSQL holds separate application and MLflow databases/roles. MLflow uses PostgreSQL for metadata and a durable local artifact volume. Database schema upgrades require a backup and explicit version-compatible migration step.
- Deploy SearXNG with JSON enabled and query it over the private network. Deploy Docling Serve with request/page/file/time limits and CPU as the initial device so it does not compete with Ollama; GPU acceleration is a measured later change, not a default.
- Open WebUI reaches Ollama only through the P03 bounded gateway after P04-S009 adds the activation-discovered Rancher source rule; it never connects to an unrestricted Ollama listener. Open WebUI in-chat STT is distinct from Windows-wide dictation in P05. PGVector is infrastructure for later RAG work, not proof that a knowledge base exists.
- P04 produces reusable `operations/windows/p04`, `operations/ubuntu/p04`, and `tests/p04` preview/apply/verify/backup/restore/rollback operations for later composition; it does not build the final installer.

## Current source baseline (refresh at activation)

- [Rancher Desktop container-engine guidance](https://docs.rancherdesktop.io/ui/preferences/container-engine/general/)
- [Rancher Desktop Windows installation requirements](https://docs.rancherdesktop.io/getting-started/installation/)
- [Rancher Desktop persistent storage](https://docs.rancherdesktop.io/tutorials/using-persistent-storage/)
- [Rancher Desktop volume locations](https://docs.rancherdesktop.io/faq/)
- [Rancher Desktop snapshots](https://docs.rancherdesktop.io/ui/snapshots/)
- [Microsoft WSL backup and move guidance](https://learn.microsoft.com/en-us/windows/wsl/faq#how-can-i-move-my-wsl-distribution-to-a-different-drive-or-location)
- [Open WebUI SearXNG integration](https://docs.openwebui.com/features/chat-conversations/web-search/providers/searxng/)
- [Open WebUI Docling extraction](https://docs.openwebui.com/features/chat-conversations/rag/document-extraction/docling/)
- [Open WebUI environment and PGVector configuration](https://docs.openwebui.com/reference/env-configuration/)
- [SearXNG Search API](https://docs.searxng.org/dev/search_api.html)
- [Docling Serve configuration](https://github.com/docling-project/docling-serve/blob/main/docs/configuration.md)
- [MLflow tracing](https://mlflow.org/docs/latest/genai/tracing/)
- [MLflow backend stores](https://mlflow.org/docs/latest/self-hosting/architecture/backend-store/)

## Gate

P04-S001 research and P04-S002 learning may run after P03 acceptance without privileged authorization. Before P04-S003 changes Rancher Desktop, the controller presents one revision-bound preview covering runtime settings, exact current and target WSL/snapshot paths, relocation export and recovery, Compose images/digests, secrets and volumes, database migration/backup, loopback ports, the Rancher-only inference-gateway rule, service failure tests, and isolated restore; the owner gives one P04 phase authorization. GUI actions, microphone permission, learning answers, and final acceptance are human participation rather than repeated approvals. Material changes to images, targets, network exposure, data handling, risk, or restore scope invalidate the authorization.

## Story sequence

| Seq. | Story | Step | Risk |
|---:|---|---|---|
| 1 | [P04-S001: Research current service releases and integration contracts](../../stories/P04/P04-S001-research-current-service-releases-and-integration-contracts.md) | Research | Low |
| 2 | [P04-S002: Learn Rancher Desktop and the local service stack](../../stories/P04/P04-S002-learn-rancher-desktop-and-the-local-service-stack.md) | Learning | Low |
| 3 | [P04-S003: Configure Rancher Desktop for Moby without Kubernetes](../../stories/P04/P04-S003-configure-rancher-desktop-for-moby-without-kubernetes.md) | Implementation | Critical |
| 4 | [P04-S004: Implement pinned Compose and secret handling foundation](../../stories/P04/P04-S004-implement-pinned-compose-and-secret-handling-foundation.md) | Implementation | High |
| 5 | [P04-S005: Deploy PostgreSQL and PGVector](../../stories/P04/P04-S005-deploy-postgresql-and-pgvector.md) | Implementation | High |
| 6 | [P04-S006: Deploy SearXNG and verify private search](../../stories/P04/P04-S006-deploy-searxng-and-verify-private-search.md) | Implementation | High |
| 7 | [P04-S007: Deploy Docling Serve](../../stories/P04/P04-S007-deploy-docling-serve.md) | Implementation | High |
| 8 | [P04-S008: Deploy self-hosted MLflow foundation](../../stories/P04/P04-S008-deploy-self-hosted-mlflow-foundation.md) | Implementation | High |
| 9 | [P04-S009: Deploy and configure Open WebUI](../../stories/P04/P04-S009-deploy-and-configure-open-webui.md) | Implementation | High |
| 10 | [P04-S010: Connect Open WebUI to SearXNG](../../stories/P04/P04-S010-connect-open-webui-to-searxng.md) | Implementation | High |
| 11 | [P04-S011: Connect Open WebUI document extraction and vector storage](../../stories/P04/P04-S011-connect-open-webui-document-extraction-and-vector-storage.md) | Implementation | High |
| 12 | [P04-S012: Configure Open WebUI local in-chat speech to text](../../stories/P04/P04-S012-configure-open-webui-local-in-chat-speech-to-text.md) | Implementation | High |
| 13 | [P04-S013: Run automated service-stack acceptance](../../stories/P04/P04-S013-run-automated-service-stack-acceptance.md) | Testing | Critical |
| 14 | [P04-S014: Perform service-stack owner acceptance and restore drill](../../stories/P04/P04-S014-perform-service-stack-owner-acceptance-and-restore-drill.md) | Human Validation | Critical |

## Completion

Every non-superseded story is Done; human evidence is genuine; review findings resolve; rollback evidence exists; and the outcome is demonstrated on the reference workstation.
