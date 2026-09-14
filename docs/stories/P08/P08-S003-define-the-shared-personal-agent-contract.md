# P08-S003: Define the shared personal-agent contract

| Property | Value |
|---|---|
| Story ID | P08-S003 |
| Phase | P08 — Practical Personal Agents |
| Sequence | 3 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Medium |
| Actor | LLM |
| Dependencies | P08-S002 |
| Unlocks | P08-S012 |
| Preferred route | Interface: WSL coding agent through goagentic; Provider: controller-selected cloud provider; Model class: high-reliability architecture; Effort: high; Fallback: cross-provider design review before code generation. |
| Research freshness | P08-S001 must be unexpired; current LangChain/LangGraph, Open WebUI, Ollama, MLflow, and OWASP docs rechecked within 7 days. |

## 1. User story

As the owner, I want one enforceable agent contract so every personal agent inherits consistent privacy, safety, capability, and evidence rules.

## 2. Bounded objective

Create versioned schemas and policy assets under workloads/agents/personal/contracts/ plus reusable validation at operations/ubuntu/p08/P08-S003-personal-agent-contract/.

## 3. Learning objective

Not applicable — the concepts were completed in P08-S002.

## 4. Current research requirements

Confirm current middleware hooks, interrupt semantics, checkpoint replay rules, Open WebUI preset fields, native tool behavior, Ollama request controls, MLflow trace/evaluation APIs, and OWASP prompt-injection guidance before freezing the schema.

## 5. Preconditions and unlock conditions

P08-S002 is Done. Inputs include accepted provider/model profiles, owner region, P06 capability registry, P07 retrieval registry, P04 MLflow/Open WebUI endpoints, and explicit P09 memory prohibition.

## 6. In scope

Schemas for identity, purpose, input/output, provider/model disclosure, role boundaries, allowed tools/data/RAG, denied capabilities, tool/model call limits, timeouts, token budget, citations, uncertainty, escalation, thread retention/deletion, trace redaction, explicit export confirmation, test requirements, version, and provenance.

## 7. Out of scope and prohibited changes

No agent implementation, service deployment, generic shell/browser/filesystem/network capability, account connection, unreviewed MCP server, cross-thread semantic memory, silent write, prompt-only authorization, or raw private-text tracing.

## 8. Privilege and human approval

No privileged action. Policy changes affecting safety, data access, or writes require a future revision-bound activation packet.

## 9. Risk rationale

Medium: repository-only change, but this contract governs later high-risk behavior.

## 10. Execution contract

Define JSON Schema plus readable policy; use deny-by-default capability resolution; separate deterministic enforcement from model instructions; require replay-safe side effects; version all prompts/skills/tools; define regional emergency-resource lookup; and provide valid and invalid fixtures for every agent class.

## 11. Automated acceptance tests

Validate schemas and fixtures; reject unknown capabilities, wildcard resources, public endpoints, missing disclosures, absent limits, trace payloads containing seeded PII, cross-thread memory, uncited sourced claims, unconfirmed writes, and policy changes introduced by retrieved text or tool output.

## 12. Human validation

Not applicable — engineering correctness is independently reviewed. Owner-facing behavior is tested in P08-S010.

## 13. Idempotency and rollback

Generation is deterministic from versioned inputs. Rollback restores the prior schema set; incompatible revisions require migration metadata and cannot silently reinterpret stored state.

## 14. Required evidence

evidence/P08-S003/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, review.md, schema-validation.json, negative-fixtures.json, and policy-diff.json.

## 15. Definition of done

The contract is machine-validatable, deny-by-default, model-independent, covers every fixed architecture boundary, passes negative tests, and receives fresh-session architecture review.

## 16. Pause-safe boundaries

Update evidence/P08-S003/checkpoint.json after schema, fixtures, validators, and review. Pause only with the repository validation suite green and no partially migrated schema.
