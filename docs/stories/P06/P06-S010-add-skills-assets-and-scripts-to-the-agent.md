# P06-S010: Add skills, assets, and scripts to the agent

| Property | Value |
|---|---|
| Story ID | P06-S010 |
| Phase | P06 — Agent Engineering Foundation |
| Sequence | 10 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P06-S009 |
| Unlocks | P06-S011 |
| Preferred route | Interface: goagentic using Codex or Claude Code inside AI-Workbench; Provider: qualified Ollama model for bounded authoring with OpenAI or Anthropic review; Model class: strong coding/instruction model; Effort: high; Fallback: current Terra- or Sonnet-class route with cross-provider review. |
| Research freshness | Current selected skill formats and supply-chain guidance checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to package reusable instructions, deterministic scripts, and versioned assets behind explicit interfaces, so progress is inspectable and independent of chat memory.

## 2. Bounded objective

Package reusable instructions, deterministic scripts, and versioned assets behind explicit interfaces.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P06-S008; this story introduces no separate learning objective.

## 4. Current research requirements

Current selected skill formats and supply-chain guidance checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not use training memory for changeable facts.

## 5. Preconditions and unlock conditions

P06-S009. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Add one `fixture-summary` skill under `workloads/agents/foundation/skills/` with a scoped instruction file, versioned rubric asset, deterministic parser script, declared input/output schema, checksums, capability manifest, and dispatcher registration. Add verification under `tests/p06/P06-S010-agent-resources/`.

## 7. Out of scope and prohibited changes

Do not install user-global Codex/Claude skills, embed hidden instructions, execute arbitrary scripts, allow path/network escape, store secrets or private assets, duplicate MCP authority, or let instruction text override system/controller policy.

## 8. Privilege and human approval

No new approval is required under the unchanged P06 authorization. New runtime capabilities, global installation, external assets, or credentials invalidate the preview.

## 9. Risk rationale

Skills combine model-readable instructions with executable scripts and assets; hidden authority or path confusion could bypass the otherwise bounded agent.

## 10. Execution contract

Define the resource contract; add checksummed assets and deterministic script; register only the named dispatcher entry; parse instructions for prohibited overrides; run direct and agent-mediated invocation; inject missing/corrupt asset, traversal, oversized input, shell token, and prompt-injection cases; repeat discovery; remove/reapply; review.

## 11. Automated acceptance tests

Assert exactly one new skill and nonzero fixtures. Verify discovery, declared schemas, deterministic output, checksum enforcement, read-only fixture paths, bounded time/size, and identical direct/agent results; reject hidden directives, asset tampering, traversal, shell/network requests, and unknown resources. Zero matches or implicit authority fail.

## 12. Human validation

Not applicable — all content uses synthetic fixtures and deterministic checks; independent review covers instruction safety without an owner decision.

## 13. Idempotency and rollback

Registration is key-based and repeat-safe. Rollback removes only the exact skill entry/files after checksum verification and restores the prior dispatcher; shared agents, MCP configuration, and unrelated skills remain.

## 14. Required evidence

Commit skill/assets/scripts/tests plus `evidence/P06-S010/` activation, manifest, checksums, authority scan, positive/negative results, idempotency, rollback, checkpoint, and cross-provider review.

## 15. Definition of done

The agent discovers and invokes only the declared resource contract, all tamper/escape/authority cases fail, rollback is isolated, review resolves, and P06-S011 unlocks.

## 16. Pause-safe boundaries

Pause after contract, asset, script, registration, test suite, or rollback; finish atomic manifest replacement and record hashes/next command in `evidence/P06-S010/checkpoint.json`.
