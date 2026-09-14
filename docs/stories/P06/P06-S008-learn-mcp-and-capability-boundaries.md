# P06-S008: Learn MCP and capability boundaries

| Property | Value |
|---|---|
| Story ID | P06-S008 |
| Phase | P06 — Agent Engineering Foundation |
| Sequence | 8 |
| Status | Planned |
| Step | Learning |
| Hold reason | Dependency |
| Risk | Low |
| Actor | Human + LLM |
| Dependencies | P06-S007 |
| Unlocks | P06-S009 |
| Preferred route | Interface: goagentic lesson in the P06 VS Code/WSL workspace; Provider: OpenAI or Anthropic with qualified Ollama practice; Model class: economical protocol/security tutor; Effort: medium; Fallback: current Sol- or Sonnet-class tutor. |
| Research freshness | Current official MCP specification and security guidance checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to teach MCP servers, clients, tools, resources, trust, schemas, credentials, and prompt-injection boundaries, so progress is inspectable and independent of chat memory.

## 2. Bounded objective

Teach MCP servers, clients, tools, resources, trust, schemas, credentials, and prompt-injection boundaries.

## 3. Learning objective

Complete the targeted concepts and demonstrate them through the acceptance exercise.

## 4. Current research requirements

Current official MCP specification and security guidance checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not use training memory for changeable facts.

## 5. Preconditions and unlock conditions

P06-S007. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create `docs/learning/p06/P06-S008-mcp-capability-boundaries.md`, a current-protocol message map, host/client/server/transport trust diagram, tool/resource/prompt comparison, manifest-authority exercise, injection scenarios, and blank rubric under `evidence/P06-S008/`.

## 7. Out of scope and prohibited changes

Do not install an MCP server, use obsolete SDK APIs, grant filesystem/network credentials, expose remote transport, confuse advertised schema with authorization, or let a model decide its own authority.

## 8. Privilege and human approval

No new authorization is required. The owner inspects and minimizes a fictional server manifest personally; the LLM cannot fill the authority decisions.

## 9. Risk rationale

The lesson is read-only, but mistaking discovery or schema validation for authorization would create a serious capability boundary failure later.

## 10. Execution contract

Use P06-S001's accepted protocol/SDK; teach host, client, server, transport, discovery, schemas, credentials, roots, and injection; have the owner reduce a broad manifest, classify four hostile inputs, and explain enforcement outside the model; checkpoint each module.

## 11. Automated acceptance tests

Assert current protocol identity, nonzero manifest capabilities, four hostile fixtures, and blank rubric. Verify least-authority selections and enforcement explanations. Fail on deprecated APIs, remote access, credential use, prefilled answers, zero fixtures, or model-only authorization.

## 12. Human validation

The owner marks each manifest capability allow/deny, identifies minimum authority, explains transport versus authorization and one injection defense, and writes `evidence/P06-S008/human-validation.md`. The LLM cannot author it.

## 13. Idempotency and rollback

Repeats create dated attempts without changing runtime or overwriting accepted evidence. Rollback removes only an unaccepted lesson revision/attempt.

## 14. Required evidence

Commit lesson, diagram, manifest and attack fixtures, blank rubric, genuine owner response, and `evidence/P06-S008/` activation, tests, rollback, checkpoint, and review.

## 15. Definition of done

The owner meets every MCP authority rubric item without substitution, current sources and tests pass, and P06-S009 unlocks.

## 16. Pause-safe boundaries

Pause between modules or before handoff; save completed scenarios and next prompt in `evidence/P06-S008/checkpoint.json`.
