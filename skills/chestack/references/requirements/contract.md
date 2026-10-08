# Requirements and acceptance contract

Read when intent is ambiguous, work spans phases or owners, acceptance crosses environments, or scope changes. Keep the record in the existing task, issue, or plan. A small clear task needs only an outcome and a checkable done condition; expand only the fields needed to expose risk or coordinate work.

## Establish the requirement

1. State who needs what observable outcome and why. Separate the requested result from a suggested implementation; preserve explicit user constraints.
2. Bound included behavior and non-goals. Name the files, surfaces, or responsibilities owned by this task and the dependencies outside that boundary.
3. Classify each uncertainty before acting:
   - **Fact:** inspect source, configuration, or runtime with a bounded probe. Record its result and limits. If the probe is unavailable, keep the fact unresolved and name the dependent work.
   - **Product choice:** state the options and their consequences. Ask the decision owner only when existing intent cannot resolve a material tradeoff. Continue independent authorized work while the choice is pending.
   - **Working assumption:** for a reversible detail within authorized scope, state the assumption, its impact, and what observation would invalidate it. An assumption cannot supply missing authorization or satisfy an acceptance condition.
4. Derive scenarios from the actual entry points and states. Cover the main outcome, a meaningful failure or boundary, and relevant regression paths. Include recovery, permissions, persistence, concurrency, or performance only when the requirement touches them.
5. Turn each required scenario into an observable pass/fail predicate and a feasible probe. For multi-phase or consequential work, run the [acceptance review](acceptance-review.md) before handoff and after material changes. Record missing capabilities as blockers. A plan with a named blocker can be useful; dependent execution and completion remain pending.

## Minimum handoff

Use stable IDs when several conditions, phases, or consumers need to refer to the same requirement. Reuse existing issue or feature IDs. Keep one authoritative record and link to it instead of copying it into every workflow.

| Field | Required meaning when applicable |
|---|---|
| Goal / R-ID | Requested outcome, source of intent, and current requirement revision. |
| Scope | Included behavior and explicit non-goals. |
| Acceptance / A-ID | R-ID, scenario, observable predicate, and required evidence level. |
| Target | Expected version or artifact and environment, including relevant account, flags, data, and entry point. Resolve the actual identity when running. |
| Owner / boundary | Who implements, verifies, or decides; owned surface and handoff limits. Use roles when names are unknown. |
| Dependencies | Required upstream behavior, artifact, or decision; current state and which work it gates. |
| Evidence | Probe and expected observation; after execution, actual target, result, and evidence reference. |
| Open questions | Fact, product choice, or working assumption; impact, resolver/probe, and blocked conditions. Write none when settled. |

A compact acceptance row can be:

`A-ID -> R-ID | given state / when action / then predicate | target | owner / dependencies | probe | status / evidence`

Agree on the predicate before implementing or measuring it. Define thresholds and units for numeric predicates; ground budgets in user intent, an existing service target, or a measured baseline. Keep an unresolved budget explicit rather than inventing a passing threshold after seeing the result. Use a repeatable command with its working directory or a concrete supported user action, expected observation, and completion/timeout boundary. Keep credentials and private fixture data out of the record.

## Trace requirements to acceptance

- Every in-scope requirement maps to at least one acceptance condition. Every acceptance condition maps back to intent; remove or propose unrelated work instead of silently expanding scope.
- Every acceptance condition maps to an owning phase and a probe. Several phases may contribute, but name the phase that proves the final user outcome; component checks alone cannot close that condition.
- Reuse existing verification feature, entry-point, and case IDs where available. Link A-IDs to those cases. Read the [feature-map contract](../../../chestack-verify/references/feature-map.md) only when consuming or creating a feature map; this contract does not require a new verification skill.
- Review coverage semantically: all required outcomes, material alternate paths, dependencies, and non-goals must be accounted for. Structural plan validation cannot establish this.

## Evidence and closure

Use `not-run`, `passed`, `failed`, or `blocked` for acceptance results. A planned probe starts as `not-run`; use `blocked` with the missing prerequisite when it cannot run. An observed predicate mismatch is `failed`. An expected rejection can be `passed` when the required error and absence of forbidden side effects are both observed. A timeout never proves success.

For each attempt, retain the A-ID and requirement revision, actual target revision/artifact (including relevant uncommitted changes), environment/fixture, action, observed result, time, and evidence location. Keep artifacts outside disposable state. A path or worker summary alone is not proof: inspect the relevant artifact against the predicate. Preserve earlier attempts separately; a later pass must explain the fix or changed conditions rather than erase a failure. Unexplained contradictory results leave the condition unresolved.

Follow the [verification guide](../verification.md) when collecting evidence. Label source inspection, local checks, real behavior, CI, review, merge, deployment, and user acceptance separately. Choose the required level from the actual outcome. A successful local run cannot establish rollout or deployed behavior; a user's preference decision cannot replace runtime proof.

Close only when all current in-scope acceptance conditions pass at their required evidence level and blocking questions are resolved. If the user explicitly defers or removes a condition, record that scope decision and its remaining impact instead of marking the condition passed. Report partial completion with the exact unmet condition.

## Handle changes

1. Record the new intent, source, and affected R-IDs/A-IDs. Keep IDs stable for revised conditions; mark removed conditions superseded and assign new IDs to distinct additions.
2. Compare predicates, scope, target, owners, dependencies, and probes. Update the authoritative record before dependent work continues. Resolve new product choices through the same uncertainty rules.
3. Mark affected results `not-run` or `blocked` and retain prior evidence as historical, tied to its old requirement revision and target. For a new target, compare old/new revisions, runtime configuration, exercised dependencies, fixtures, and verification code as well as the predicate. Carry evidence forward only with a recorded impact analysis explaining why the claim still holds. A matching patch or unchanged test file alone is insufficient. Re-run affected probes when relevance is uncertain, and verify target-specific delivery gates at the actual delivery head.
4. Notify dependent work through the already authorized coordination path, or include a concrete handoff in the delivery. Re-plan affected phases; continue unaffected authorized work.

This is a coordination contract, not a new permission source or automatic execution engine. Design, implementation, review, and verification consumers preserve the IDs, unresolved decisions, and evidence limits while selecting their own methods.

For a runnable example linking requirements, phases, existing verification cases, and evidence, read the [CLI acceptance example](examples/README.md).
