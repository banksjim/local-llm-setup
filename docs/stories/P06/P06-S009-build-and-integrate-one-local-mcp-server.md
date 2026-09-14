# P06-S009: Build and integrate one local MCP server

| Property | Value |
|---|---|
| Story ID | P06-S009 |
| Phase | P06 — Agent Engineering Foundation |
| Sequence | 9 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P06-S008 |
| Unlocks | P06-S010 |
| Preferred route | Interface: goagentic using Codex or Claude Code in AI-Workbench; Provider: OpenAI or Anthropic with qualified Ollama test execution; Model class: strong protocol-aware coding model; Effort: high; Fallback: current Sol- or Sonnet-class route with cross-provider security review. |
| Research freshness | Current MCP SDK and client documentation checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to implement a narrow read-only MCP capability with schemas, tests, logs, and denial controls, so progress is inspectable and independent of chat memory.

## 2. Bounded objective

Implement a narrow read-only MCP capability with schemas, tests, logs, and denial controls.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P06-S008; this story introduces no separate learning objective.

## 4. Current research requirements

Current MCP SDK and client documentation checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not use training memory for changeable facts.

## 5. Preconditions and unlock conditions

P06-S008. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Implement `workloads/agents/foundation/src/local_agents/mcp_fixture_catalog/` using the P06-S001-selected official MCP Python SDK and one read-only `search_fixture_catalog` capability over a fixed synthetic catalog root. Add stdio launch/config adapters for the accepted agent, Codex, and Claude clients plus `operations/ubuntu/p06/P06-S009-mcp-fixture-server`.

## 7. Out of scope and prohibited changes

Do not expose HTTP/LAN transport, inherit broad environment secrets, accept arbitrary roots or glob escape, add writes/shell/web access, publish prompts that expand authority, or claim compatibility for an untested client.

## 8. Privilege and human approval

No new approval is required under the P06 preview. Any transport other than stdio, extra capability, credential, or nonfixture root is a material authority change requiring a new preview.

## 9. Risk rationale

An MCP server becomes callable by multiple agent hosts; a schema or process-environment mistake could broaden filesystem or secret access despite read-only intent.

## 10. Execution contract

Pin SDK/protocol; implement strict schemas, root resolution, output/time limits, sanitized audit events, minimal child environment, and stdio lifecycle; generate client configs without secrets; test each installed client and the agent; inject traversal, malformed, oversized, cancellation, unknown-capability, environment, and process-death failures; remove/reapply; review cross-provider.

## 11. Automated acceptance tests

Assert capability and client fixture inventories. Verify each available accepted client discovers exactly the declared capability and returns the same bounded result; reject traversal, unknown calls, invalid schema, excessive output, secret/env reads, and writes; terminate cleanly on cancellation/death. Fail if zero clients run, an unavailable client is claimed, or any transport listens.

## 12. Human validation

Not applicable — synthetic fixtures and client/protocol probes are deterministic; no credential or subjective owner judgment is required.

## 13. Idempotency and rollback

Second apply leaves code/config unchanged. Rollback removes only story-added client entries and server files after exact inventory, restores prior client configs, and preserves unrelated MCP servers and the shared workspace.

## 14. Required evidence

Commit server, adapters, and operation plus `evidence/P06-S009/` activation, SDK/protocol IDs, authority/env inventory, per-client results, attacks, lifecycle, idempotency, rollback, checkpoint, and cross-provider review.

## 15. Definition of done

Every available required host invokes the one bounded capability, all authority/transport negatives fail closed, config rollback is proven, review resolves, and P06-S010 unlocks.

## 16. Pause-safe boundaries

Pause after server unit tests, each complete client adapter, attack suite, or rollback. Stop the stdio process and finish atomic config replacement before saving `evidence/P06-S009/checkpoint.json`.
