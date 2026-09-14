# P08-S012: Deploy the shared personal-agent runtime

| Property | Value |
|---|---|
| Story ID | P08-S012 |
| Phase | P08 — Practical Personal Agents |
| Sequence | 4 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P08-S003 |
| Unlocks | P08-S004 |
| Preferred route | Interface: WSL coding agent through goagentic deployment; Provider: controller-selected cloud provider; Model class: high-reliability operations; Effort: high; Fallback: restore P07 service checkpoint and run the API as a disposable localhost-only WSL process. |
| Research freshness | Current stable LangChain/LangGraph, Open WebUI integration, Ollama API, MLflow tracing, dependency-security, and container guidance checked within 7 days. |

## 1. User story

As the owner, I want one private, reproducible runtime so personal agents can use real workflows through Open WebUI without giving the model uncontrolled computer access.

## 2. Bounded objective

Create workloads/agents/personal/runtime/ and operation operations/windows/p08/P08-S012-deploy-personal-agent-runtime/ to deploy a pinned, authenticated OpenAI-compatible agent API in WSL/Rancher and register a non-production diagnostic preset in Open WebUI.

## 3. Learning objective

Not applicable — this is the shared implementation surface for later hands-on agent use.

## 4. Current research requirements

Select and record the supported Open WebUI integration mechanism from P08-S001. Prefer a standards-based private API/model-provider path over copied server-side functions; document why the selected path preserves LangGraph orchestration and Open WebUI as the primary interface.

## 5. Preconditions and unlock conditions

P08-S003 is Done. The signed activation packet fixes image/package versions and hashes, ports, loopback/private-network bindings, WSL paths, service identity, secret references, Ollama/MLflow endpoints, resource limits, and rollback checkpoint.

## 6. In scope

OpenAI-compatible `/v1/models` and streaming chat-completions contracts; LangGraph graph factory; reuse of the accepted P06 dedicated PostgreSQL checkpointer identity; per-thread state; deterministic policy middleware; model/tool budgets; timeouts; cancellation; health/readiness; structured errors; Open WebUI chat/message correlation headers; PII redaction before MLflow; authentication; a private model-ID allowlist and diagnostic preset; start/stop/status/update/backup/remove operations; and synthetic echo/no-tool graph.

## 7. Out of scope and prohibited changes

No personal agent behavior, real private content, public/LAN bind, arbitrary tool execution, host Docker socket, Windows filesystem write, cloud model runtime, P09 memory, Open WebUI built-in Memory, or raw conversation persistence in MLflow.

## 8. Privilege and human approval

One P08 revision-bound approval covers the previewed service, network, volume, port, secret, and Open WebUI registration. Pause only if Rancher/Windows requests elevation or the resolved change exceeds that packet.

## 9. Risk rationale

High: a persistent service, credentials, container/network state, and owner-facing integration are created.

## 10. Execution contract

Preflight dependencies/ports/storage; checkpoint P04/P06/P07 services; build from lockfile; scan dependencies; deploy by immutable digest; inject secrets outside Git; bind only to the approved private Rancher network and loopback administration path; run isolated migrations; register the OpenAI-compatible connection with only diagnostic model IDs; propagate current supported Open WebUI correlation headers; verify auth, streaming, cancellation, thread isolation, redaction, restart, backup/restore, and second-run no-op; then cross-provider review.

## 11. Automated acceptance tests

Prove anonymous/public/LAN access fails; authorized Open WebUI request succeeds; thread IDs cannot cross users; seeded secrets/PII never reach logs or MLflow; unknown tool/model/preset is denied; call/time/token limits stop loops; cancellation works; checkpoint resumes exactly once; side effects do not replay; restart preserves only approved thread state; duplicate deploy is a no-op. Inject bad secret, occupied port, Ollama/MLflow outage, corrupt checkpoint, bad migration, failed health, and interrupted deployment; reconcile or restore.

## 12. Human validation

Not applicable — the diagnostic preset is technically tested here; subjective use begins with individual agents and concludes in P08-S010.

## 13. Idempotency and rollback

Same inputs produce no change. Rollback unregisters only the diagnostic preset, restores service/config/data checkpoints, and preserves no unapproved personal content.

## 14. Required evidence

evidence/P08-S012/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, review.md, deployment-manifest.json, security-scan.json, redaction-results.json, failure-injection.json, and open-webui-registration.json.

## 15. Definition of done

The runtime is private, authenticated, bounded, observable without leaking content, restartable, recoverable, idempotent, independently reviewed, and ready for P08-S004.

## 16. Pause-safe boundaries

Update evidence/P08-S012/checkpoint.json before deployment and after health, integration, failure, restart, and rollback gates. Never pause with an unreconciled migration, exposed port, or partially registered preset.
