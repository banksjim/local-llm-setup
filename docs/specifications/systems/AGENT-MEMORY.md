# Durable Agent Memory System Specification

**System ID:** `SYS-MEM`  
**Status:** Approved design direction; framework deliberately unselected  
**Primary phase:** P09  
**Last reviewed:** 2026-09-13

## 1. Purpose

Give practical agents durable, inspectable memory without allowing model-generated guesses to become permanent truth. The system uses a shared memory core with agent-specific namespaces and a reviewed candidate inbox.

## 2. Memory classes

| Class | Purpose | Promotion |
|---|---|---|
| Session context | Temporary continuity within one run or thread | Expires by policy |
| Candidate memory | Agent-proposed preference, fact, goal, event, or relationship | Owner review required |
| Durable shared memory | Owner-approved facts/preferences usable by permitted agents | Reviewed promotion |
| Agent-private memory | Approved domain-specific memory visible only to one agent class | Reviewed promotion |
| Restricted memory | Sensitive records with narrower access, retention, and export rules | Explicit owner approval |

Agents may append candidate memories automatically. Only the owner or an explicitly authorized deterministic rule may promote, correct, merge, or delete durable memories.

## 3. Framework selection

P09 begins with a fresh evaluation of actively maintained OSS GitHub projects. The evaluation includes, but is not limited to, current versions of Mem0, Letta, Zep/community offerings, LangGraph memory/checkpoint components, and newly credible alternatives.

Score license, genuinely self-hosted functionality, storage portability, local-model support, LangChain/LangGraph integration, API stability, provenance, namespaces, candidate-review support, deletion/export, encryption/authentication, observability, testability, maintenance health, migration risk, and resource use. SaaS-only capabilities do not count as OSS functionality.

An ADR records the selected framework or a justified composable design. A targeted learning story for the selected technology blocks implementation.

## 4. Data model and provenance

Every memory records stable ID, class, namespace, subject, normalized content, source agent, source interaction/evidence, created/observed times, confidence as an assertion attribute rather than truth, review state, reviewer, promotion rationale, supersession links, retention, sensitivity, and access policy.

Durable memory is versioned. Corrections supersede prior assertions; they do not silently rewrite history. Retrieval returns provenance and current status. Restricted content is excluded from logs, model traces, and unrelated agents.

## 5. Reviewed inbox

The owner sees candidate memories in one queue with source context, proposed class, possible duplicates/conflicts, sensitivity warning, and actions to approve, edit, merge, reject, defer, or mark restricted. Bulk promotion is disabled initially. An agent cannot review its own candidates.

## 6. Integration and evaluation

One P08 agent is integrated first. Tests cover capture accuracy, duplicate and contradiction handling, namespace isolation, restricted-memory denial, correct retrieval, poisoning resistance, owner correction, export, deletion, backup/restore, framework upgrade, and behavior when the memory service is unavailable.

MLflow traces memory decisions without recording restricted raw values. The system must fail closed on authorization uncertainty and continue safely without durable memory when the service is unavailable.

## 7. Acceptance

The selected system is self-hosted, uses local storage and local models where applicable, passes the targeted learning gate, preserves provenance, requires reviewed promotion, isolates namespaces, supports export/deletion and tested restore, and measurably improves the selected agent without unacceptable false-memory behavior.
