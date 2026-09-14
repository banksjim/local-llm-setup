# P06: Agent Engineering Foundation

**Depends on:** P05  
**Required outcome:** A real, secure, locally runnable LangChain and LangGraph agent uses tools, MCP, skills, assets, scripts, durable execution, and MLflow observability.  
**Status:** Planned

## Fixed architecture and execution boundary

- Build one Python-first agent workspace beneath the dedicated `AI-Workbench` user's Linux home. Use the P02-approved Python environment and package manager, a lock file with hash-verifiable artifacts where supported, typed configuration, formatting, static analysis, unit/integration tests, and ignored local secrets. Do not develop from `/mnt/c` or `/mnt/h`.
- Treat models, agents, tools, and orchestration as separate layers. Ollama supplies qualified models through the P03 inference-only gateway; LangChain supplies model/message/tool adapters; LangGraph owns explicit state, checkpoints, interrupts, retries, and resume; MCP exposes narrowly described capabilities; skills/assets/scripts remain versioned agent resources; MLflow records sanitized traces and evaluation links.
- Pin the current compatible LangChain, LangGraph, Ollama integration, MCP Python SDK, and MLflow versions selected by P06-S001. Current upstream major versions and APIs are activation variables: the executor must not copy an older tutorial API merely because it appears in repository history.
- The first agent is deliberately read-only. Its deterministic fixture tool accepts a strict schema, can read only its fixture directory, has bounded output/time, and cannot execute a shell, follow arbitrary URLs, access secrets, or mutate the repository.
- LangGraph uses a durable local PostgreSQL-backed checkpointer selected from the accepted current integration. It receives a dedicated P04 PostgreSQL database and least-privilege role; it never reuses the Open WebUI or MLflow database/role. Every run has an explicit thread ID; side effects are isolated in idempotent nodes; replay does not silently repeat an external effect. Approval interrupts carry only JSON-safe summaries and never credentials.
- The first MCP server is local, read-only, and narrower than the equivalent direct tool. Start with standard input/output unless current accepted client support requires a different localhost-only transport. Its allowlisted root, schemas, response limits, timeouts, audit events, and denial behavior are explicit. It does not inherit the agent process's broad environment.
- MLflow uses the self-hosted P04 service. Trace collection defaults to metadata and sanitized fixture payloads; credentials, private documents, restricted memory, raw microphone input, and unapproved prompt content are redacted or excluded before emission. Loss of tracing cannot expand authority or make a failed operation appear successful.
- Evaluation combines deterministic assertions with separately labeled model-scored judgments. Thresholds, fixtures, evaluator identity, prompt, model, repetitions, and cost are versioned. A model judge never becomes the sole safety or authorization control.

## Current source baseline (refresh at activation)

- [LangChain Python quickstart](https://docs.langchain.com/oss/python/langchain/quickstart)
- [LangChain tools](https://docs.langchain.com/oss/python/langchain/tools)
- [LangChain ChatOllama integration](https://docs.langchain.com/oss/python/integrations/chat/ollama)
- [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
- [LangGraph interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)
- [Official MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Python SDK documentation](https://py.sdk.modelcontextprotocol.io/)
- [MLflow GenAI tracing](https://mlflow.org/docs/latest/genai/tracing)
- [MLflow trace evaluation](https://mlflow.org/docs/latest/genai/eval-monitor/running-evaluation/traces/)

## Gate

P06-S001 research and P06-S002 learning may run after P05 acceptance without privileged authorization. Before P06-S003 creates the workspace and later services/configuration, the controller presents one revision-bound P06 preview covering repositories and paths, dependency sources and versions, model endpoints, tool roots and denied capabilities, checkpoint storage/migrations, MCP transport, MLflow data/redaction, evaluation budgets, failure injection, and rollback; the owner gives one P06 phase authorization. Learning answers, credential entry, and owner acceptance are human participation rather than repeated approvals. A material change to authority, data class, network boundary, dependency major version, trace content, or persistent state invalidates that authorization.

## Story sequence

| Seq. | Story | Step | Risk |
|---:|---|---|---|
| 1 | [P06-S001: Refresh agent framework and protocol guidance](../../stories/P06/P06-S001-refresh-agent-framework-and-protocol-guidance.md) | Research | Low |
| 2 | [P06-S002: Learn agent fundamentals and tool safety](../../stories/P06/P06-S002-learn-agent-fundamentals-and-tool-safety.md) | Learning | Low |
| 3 | [P06-S003: Create the agent development workspace](../../stories/P06/P06-S003-create-the-agent-development-workspace.md) | Implementation | Medium |
| 4 | [P06-S004: Learn LangChain models, messages, tools, and agents](../../stories/P06/P06-S004-learn-langchain-models-messages-tools-and-agents.md) | Learning | Low |
| 5 | [P06-S005: Build the first bounded LangChain tool agent](../../stories/P06/P06-S005-build-the-first-bounded-langchain-tool-agent.md) | Implementation | Medium |
| 6 | [P06-S006: Learn LangGraph state and durable execution](../../stories/P06/P06-S006-learn-langgraph-state-and-durable-execution.md) | Learning | Low |
| 7 | [P06-S007: Convert the agent to a durable LangGraph workflow](../../stories/P06/P06-S007-convert-the-agent-to-a-durable-langgraph-workflow.md) | Implementation | High |
| 8 | [P06-S008: Learn MCP and capability boundaries](../../stories/P06/P06-S008-learn-mcp-and-capability-boundaries.md) | Learning | Low |
| 9 | [P06-S009: Build and integrate one local MCP server](../../stories/P06/P06-S009-build-and-integrate-one-local-mcp-server.md) | Implementation | High |
| 10 | [P06-S010: Add skills, assets, and scripts to the agent](../../stories/P06/P06-S010-add-skills-assets-and-scripts-to-the-agent.md) | Implementation | High |
| 11 | [P06-S011: Learn MLflow tracing and evaluation](../../stories/P06/P06-S011-learn-mlflow-tracing-and-evaluation.md) | Learning | Low |
| 12 | [P06-S012: Instrument the agent with MLflow](../../stories/P06/P06-S012-instrument-the-agent-with-mlflow.md) | Implementation | High |
| 13 | [P06-S013: Create the initial agent evaluation harness](../../stories/P06/P06-S013-create-the-initial-agent-evaluation-harness.md) | Testing | High |
| 14 | [P06-S014: Perform first-agent owner acceptance](../../stories/P06/P06-S014-perform-first-agent-owner-acceptance.md) | Human Validation | High |

## Completion

All non-superseded stories are Done; human evidence is genuine; findings resolve; rollback exists; and the outcome is demonstrated.
