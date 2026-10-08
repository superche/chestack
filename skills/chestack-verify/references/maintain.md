# Maintain a verification skill

Audit an existing project verification package against current source and runtime. Editing is limited to that package's instructions, feature map, fixtures, and owned helpers. Product fixes belong to a separately authorized task. For a read-only audit, report proposed corrections without editing.

## Locate and establish scope

Find the repository's verification skill and read its entry, feature index, helpers, and local instructions. If several candidates plausibly match, resolve from the requested application/surface or ask which target. If none exists, report that finding and route a requested creation to [Create](create.md); do not invent an audit target.

Record the target revision, environment, and coverage scope in scratch notes. A full maintenance pass covers every mapped feature and every listed entry point. If the user bounds the audit to a subset, name that subset and avoid a whole-map clean claim.

## Reconcile map and source

1. Compare the index with feature files: detect unlisted leaves, duplicate IDs, broken links, and obsolete entries. Read the [map contract](feature-map.md).
2. Trace each feature to concrete user-facing source entry points, supported flags/routes/controls, state transitions, and existing tests. Capture source locations and a concise live recipe. Inspect recent changes for new surfaces absent from the map; require a concrete supported path before adding coverage.
3. When delegation is permitted and useful, use read-only source reviewers with disjoint feature scopes. They return source citations, suspected drift, and proposed probes; they do not edit or drive shared runtime state. Otherwise perform the same source pass sequentially and describe it accurately.
4. Reconcile source findings into a coverage matrix keyed by feature and entry-point/case ID. Minimize repeated setup without treating one entry point as proof of another. Separate current source behavior from the intended product contract; source alone cannot settle a suspected regression.

## Exercise the map

The coordinator owns live driving. Follow the package's launch model: a checked long-lived instance for server/UI flows, or fresh isolated invocations/PTY sessions for short-lived commands. Reset fixtures between cases.

- Run doctor before first drive, for fresh sessions, and after unexpected behavior. If process health passes but interaction state is wedged, reset to a known state or relaunch an owned instance before proceeding.
- Exercise each required entry point, observing the action, result, and relevant side effect. Track `passed`, `failed`, `blocked`, or `not-run` per case with artifact paths. A missing entitlement, OS, account, or service yields a blocked case with the route attempted and concrete prerequisite; it is not a passing alternate path.
- If doctor or driving fails due to proven recipe/harness drift, repair within scope, restart only invalidated state, and retry once. A repeated failure remains blocked or failed; do not loop indefinitely.
- Clean owned residue after failed attempts, timeouts, and cancellation. Preserve user-owned attached instances; undo only authorized fixture mutations. Retain evidence outside scratch runtime state and confirm it survives cleanup.
- Re-drive every affected path after a harness or command correction. Complete final teardown after all re-proofs, including failed ones.

Source review alone cannot establish live coverage, even when no drift is found.

## Classify before editing

| Finding | Treatment |
|---|---|
| Instructions differ from a confirmed supported contract | Fix documentation and re-exercise the corrected path. |
| Supported behavior works but the harness cannot reach or observe it | Fix the owned helper/recipe, document its invocation, and prove the fix live. |
| Behavior violates the expected contract | Report a product regression with reproduction evidence. Preserve the expected predicate; do not rewrite the map to bless broken behavior. |
| Intent is ambiguous | Preserve the claim, record the conflicting evidence, and request the missing decision. |
| Missing environment, permission, or tool | Record the attempted route and unmet prerequisite; continue independent reachable cases. |

Remove a feature only with evidence that its supported contract was intentionally retired. A failing selector or absent runtime control is insufficient evidence of retirement.

## Deliver a bounded result

- **clean:** all cases in the declared scope have source and live coverage, no failures or gaps, and no corrections needed. A partial-scope audit is labeled partial; it cannot certify the whole map.
- **updated:** corrections are complete, affected paths were re-proven, and required scope coverage finished without unresolved failures or gaps.
- **incomplete:** any required case failed, was blocked, or was not run; or a correction remains unproven. Report verified subsets and any local changes separately.

Report feature/entry-point coverage, confirmed corrections, product defects, remaining prerequisites, evidence location, and cleanup outcome. Keep run diaries in scratch artifacts, not in the maintained map. Create at most one scoped PR when publication is part of the authorized task and the corrections are proven; a clean audit needs no branch or PR. An incomplete audit does not trigger automatic publication, merge, or scheduling.
