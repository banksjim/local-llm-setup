# P07-S014: Build the Langflow personal RAG capstone

| Property | Value |
|---|---|
| Story ID | P07-S014 |
| Phase | P07 — RAG, Ingestion, and Knowledge-Base Capstone |
| Sequence | 14 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | Human + LLM |
| Dependencies | P07-S013 |
| Unlocks | P07-S015 |
| Preferred route | Human through a goagentic-guided checklist with the controller-selected assistant; no unattended substitution. |
| Research freshness | Current Langflow component and export docs checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to build one substantial private knowledge-base flow with citations, local models, and MLflow traces, so progress is inspectable and independent of chat memory.

## 2. Bounded objective

Deploy the pinned Langflow component and build one substantial private knowledge-base flow with citations, local models, and MLflow traces. Expose the accepted flow to Open WebUI through the currently supported localhost-only integration selected at activation.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P07-S003; this story introduces no separate learning objective.

## 4. Current research requirements

Current Langflow component and export docs checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not use training memory for changeable facts.

## 5. Preconditions and unlock conditions

P07-S013. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

The objective, declared files or services, tests, documentation, evidence, and minimum safe supporting changes.

## 7. Out of scope and prohibited changes

Unrelated phase work, unapproved redesign, public exposure, secret disclosure, destructive cleanup, and unnamed actions.

## 8. Privilege and human approval

Required — the human performs or validates the work; an LLM cannot create completion evidence.

## 9. Risk rationale

Work affects services, private data, credentials, networking, or several components; integration evidence and rollback are mandatory. New facts may raise risk; an LLM cannot lower it.

## 10. Execution contract

Preview, validate, lease, execute reversible units, stop on drift, test, record sanitized evidence, release, and review. The exported flow is versioned and reproducible, passes the agreed query set, and returns equivalent cited results when invoked from Open WebUI.

## 11. Automated acceptance tests

The deployment and exported flow are pinned, versioned, reproducible, and pass the agreed query set. A supported localhost-only Open WebUI call returns answers and citations without exposing Langflow to the LAN. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks pass; exclusions are justified.

## 12. Human validation

Owner completes the story checklist and records it through the controller.

## 13. Idempotency and rollback

Second execution reports no unintended change; rollback restores story-owned changes and preserves user data.

## 14. Required evidence

Story revision; actor and model; dated sources; changes; sanitized output; tests; approvals; idempotency; rollback; review; and human records.

## 15. Definition of done

Objective and tests pass; evidence and review are accepted; genuine human evidence exists when required; state agrees; next story unlocks.

## 16. Pause-safe boundaries

Pause before mutation and after each reversible unit, tests, and durable evidence. Finish or roll back atomic replacement before pausing.
