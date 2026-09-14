# P06-S012: Instrument the agent with MLflow

| Property | Value |
|---|---|
| Story ID | P06-S012 |
| Phase | P06 — Agent Engineering Foundation |
| Sequence | 12 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P06-S011 |
| Unlocks | P06-S013 |
| Preferred route | Interface: goagentic using Codex or Claude Code inside AI-Workbench; Provider: OpenAI or Anthropic with qualified Ollama for test iteration; Model class: strong coding/observability model; Effort: high; Fallback: current Sol- or Sonnet-class route with cross-provider privacy review. |
| Research freshness | Current MLflow LangChain, LangGraph, and OpenTelemetry docs checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to record model, prompts, tools, state transitions, retrieval, latency, failures, and evaluation links with redaction, so progress is inspectable and independent of chat memory.

## 2. Bounded objective

Record model, prompts, tools, state transitions, retrieval, latency, failures, and evaluation links with redaction.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P06-S011; this story introduces no separate learning objective.

## 4. Current research requirements

Current MLflow LangChain, LangGraph, and OpenTelemetry docs checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not use training memory for changeable facts.

## 5. Preconditions and unlock conditions

P06-S011. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Instrument the durable agent with current MLflow tracing at `workloads/agents/foundation/src/local_agents/observability/`: spans for run, model, tool, graph node, interrupt, error, and evaluator link; explicit provider/model/version/thread metadata; allowlist/redaction policy; sampling switch; bounded async queue; and `operations/ubuntu/p06/P06-S012-mlflow-instrumentation`.

## 7. Out of scope and prohibited changes

Do not capture credentials, raw private documents, restricted memory, microphone data, hidden reasoning, or unapproved prompts; enable cloud export; make tracing required for safe execution; or alter agent authority.

## 8. Privilege and human approval

No new approval is required under P06 authorization. Any new trace data class, remote exporter, public bind, or retention expansion invalidates the preview.

## 9. Risk rationale

Instrumentation crosses agent, graph, MCP, and MLflow boundaries; incorrect capture can disclose sensitive data or an outage can alter agent behavior.

## 10. Execution contract

Export current settings; define span and redaction contracts; instrument one layer at a time; emit synthetic success/failure/interrupt traces; inject canary secrets in every field class; stop MLflow and saturate the queue; verify safe agent behavior and bounded loss reporting; restart, repeat, disable, restore, and review.

## 11. Automated acceptance tests

Assert each required span and canary fixture. Verify trace hierarchy, IDs, model/provider/tool decisions, latency/error status, evaluator link, and redaction before emission; search storage/logs for every canary; prove outage, timeout, and full queue neither expands authority nor changes answer status. Fail on any secret, missing required span, remote export, zero fixtures, or safety dependence on tracing.

## 12. Human validation

Not applicable — synthetic canaries and deterministic trace inspection prove privacy and outage behavior without owner content.

## 13. Idempotency and rollback

Instrumentation registration is repeat-safe. Rollback disables the hook, restores prior settings, and removes only tagged synthetic traces after inventory; agent code, unrelated MLflow records, and databases remain.

## 14. Required evidence

Commit instrumentation/operation plus `evidence/P06-S012/` activation, span schema, redaction policy, canary inventory, trace IDs, outage/queue results, storage scan, idempotency, rollback, checkpoint, and cross-provider review.

## 15. Definition of done

All required spans and decisions are inspectable, all sensitive canaries are absent, outages fail safely, rollback is isolated, review resolves, and P06-S013 unlocks.

## 16. Pause-safe boundaries

Pause after a complete instrumentation layer, trace fixture, outage test, or restore. Drain or discard only tagged queued fixtures and record trace/settings state in `evidence/P06-S012/checkpoint.json`.
