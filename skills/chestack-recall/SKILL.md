---
name: chestack-recall
description: "Recover working context across authorized history and current artifacts: goals, decisions, attempted fixes, live status, and next steps. Use for catch-up requests; resuming one known checkpoint uses session-pickup."
---

# CheStack Recall

Read the [host contract](../chestack/references/hosts.md). Reconstruct context read-only; a catch-up request does not authorize resuming implementation, messaging people, or changing memory.

## Bound and recover

1. State the topic, workspace, and time window inferred from the request. For unspecified recent history, use the last seven days and say so; honor explicit wider ranges and report retrieval limits. For a supplied complete state summary, use it as the starting point instead of mining the same history again. A request to resume one known checkpoint follows [session pickup](../chestack/references/playbooks/session-pickup.md).
2. Discover authorized history capabilities from this host: chat tools, supplied transcripts, checkpoints, or accessible records. Do not assume another host's transcript layout. If history is unavailable, work from supplied artifacts and name the gap; never search unrelated private workspaces to fill it.
3. Search topic and time metadata before reading full messages. Collect goals, decisions, attempts, corrections, unresolved issues, and artifact identifiers with dated source references. Read the relevant full record when the answer depends on which commands or actions actually ran; an earlier agent summary is a lead, not proof.
4. For a named feature or bug, use a scoped [Why](../chestack-why/SKILL.md) investigation of the shared record to recover related fixes, reversions, incidents, and user reports. Frame the question as what changed and what remains unresolved. For pure personal activity recall with no named system, stay within activity records. Preserve source-coverage gaps.
5. Reconcile the history with live branches, PR heads/status, issue state, and relevant runtime/artifact evidence. Bind observations to a time and target. An old pass, pushed branch, or proposed plan does not establish today's implementation or release state. Preserve incompatible evidence rather than choosing the latest narrative.

## Return the current state

Lead with a short capsule of the work and where it stands. Give one line per relevant workstream with an observed state, its artifact/source, and any unverified part. Keep planned, implemented, checked, merged, deployed, and accepted distinct; state unavailable live checks explicitly.

Then explain recurring problems or failed/reverted attempts that matter to the next action. End with one concrete next step and the decision or capability it needs. Keep adjacent work out unless it blocks the named task. Redact private material before sharing beyond its authorized audience.

**Done:** the reader can distinguish past claims from current observations and resume from the right open issue. No completion claim relies solely on a transcript, and no automatic continuation is implied.
