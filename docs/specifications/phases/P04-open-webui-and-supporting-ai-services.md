# P04: Open WebUI and Supporting AI Services

**Depends on:** P03  
**Required outcome:** A pinned, localhost-only Rancher Desktop stack with Open WebUI, PostgreSQL and PGVector, SearXNG, Docling, and MLflow foundations.  
**Status:** Planned

## Gate

The phase activates only after dependencies are accepted and the owner authorizes its first story. Research and design may occur earlier, but implementation cannot cross this gate.

## Story sequence

| Seq. | Story | Step | Risk |
|---:|---|---|---|
| 1 | [P04-S001: Research current service releases and integration contracts](../../stories/P04/P04-S001-research-current-service-releases-and-integration-contracts.md) | Research | Low |
| 2 | [P04-S002: Learn Rancher Desktop and the local service stack](../../stories/P04/P04-S002-learn-rancher-desktop-and-the-local-service-stack.md) | Learning | Low |
| 3 | [P04-S003: Configure Rancher Desktop for Moby without Kubernetes](../../stories/P04/P04-S003-configure-rancher-desktop-for-moby-without-kubernetes.md) | Implementation | High |
| 4 | [P04-S004: Implement pinned Compose and secret handling foundation](../../stories/P04/P04-S004-implement-pinned-compose-and-secret-handling-foundation.md) | Implementation | High |
| 5 | [P04-S005: Deploy PostgreSQL and PGVector](../../stories/P04/P04-S005-deploy-postgresql-and-pgvector.md) | Implementation | High |
| 6 | [P04-S006: Deploy SearXNG and verify private search](../../stories/P04/P04-S006-deploy-searxng-and-verify-private-search.md) | Implementation | High |
| 7 | [P04-S007: Deploy Docling Serve](../../stories/P04/P04-S007-deploy-docling-serve.md) | Implementation | High |
| 8 | [P04-S008: Deploy self-hosted MLflow foundation](../../stories/P04/P04-S008-deploy-self-hosted-mlflow-foundation.md) | Implementation | High |
| 9 | [P04-S009: Deploy and configure Open WebUI](../../stories/P04/P04-S009-deploy-and-configure-open-webui.md) | Implementation | High |
| 10 | [P04-S010: Integrate search, extraction, vector storage, and chat STT](../../stories/P04/P04-S010-integrate-search-extraction-vector-storage-and-chat-stt.md) | Implementation | High |
| 11 | [P04-S011: Perform service-stack acceptance and restore drill](../../stories/P04/P04-S011-perform-service-stack-acceptance-and-restore-drill.md) | Human Validation | Critical |

## Completion

Every non-superseded story is Done; human evidence is genuine; review findings resolve; rollback evidence exists; and the outcome is demonstrated on the reference workstation.

