# Review an acceptance plan

Use before executing a multi-phase or consequential plan, when a product decision changes it, or before claiming its outcome. Read the [contract](contract.md) first. For a small clear task, apply the relevant questions in place; no separate review document is required.

## 1. Ground the claims

Read the request, current constraints, and target independently of the proposed implementation. List the required user outcomes and prohibited effects, then trace them to R-IDs and A-IDs. Flag uncovered intent, invented scope, and implementation steps presented as outcomes. Settle factual gaps with bounded probes; leave material product choices with their authorized decision owner.

**Exit:** every included outcome and explicit constraint has a predicate or an identified decision blocking it. A task list by itself does not satisfy this check.

## 2. Select coverage by failure consequence

For each materially different entry point or state, ask which plausible failure would escape the proposed checks. Add the smallest scenario that would expose it. Reuse existing feature-map cases; do not multiply workers or cases merely to meet a count.

| When relevant | Required distinction |
|---|---|
| User-visible behavior | Actual entry point, starting state, action, and final state; compilation alone cannot prove it. |
| Invalid input or unavailable dependency | Expected rejection/degraded behavior and absence of forbidden side effects. |
| Persistent or destructive changes | Independent readback, preservation of unrelated data, and recovery after interruption where required. |
| Several entry points, accounts, or environments | Name which paths the evidence covers; test materially different paths or justify why they exercise the same behavior. |
| Concurrency, retries, or shared state | Identify competing actors and the invariant; test the relevant interleaving or bound the claim to single-writer use. |
| Regression or migration | Run the same meaningful scenario on the baseline and candidate where possible. If the baseline lacks the feature, state that and prove the new outcome plus preservation of existing behavior. |
| Performance or numerical quality | Define workload, metric/unit, baseline, correctness gates, and failure budget before the run; follow the [measurement guide](../measurement.md). |
| Interaction or subjective quality | Name who judges which artifact; automated checks complement an explicit user review gate rather than fulfilling it. |

Record included dimensions and material exclusions with reasons in the existing plan. An unavailable required surface is `blocked`, not excluded. A dimension outside the actual requirement needs no ceremonial test.

**Exit:** each material failure has a named scenario, owner, and evidence requirement; exclusions do not contradict the request.

## 3. Try to falsify the proof

For each A-ID, ask whether its proposed evidence could still look successful if:

- The user action never ran, or the fixture was already in the final state.
- The action ran against the wrong build, account, instance, or deployment.
- The visible response succeeded but persistence or another required side effect failed.
- A component passed while the cross-phase user flow remained broken.
- Only the convenient entry point worked, or a mock bypassed the behavior being claimed.
- A retry hid a failure or a stale artifact was reused after the predicate or target changed.

If yes, strengthen the probe with the missing before/action/after observation, target check, independent readback, or final-flow case. For a negative condition, define the observation boundary and duration that make absence meaningful. Capture enough evidence to distinguish a tested rejection from a harness failure.

**Exit:** the proposed observation distinguishes success from the plausible failure. A screenshot filename, zero exit code, or rule-name assertion alone is insufficient when it does not observe the predicate.

## 4. Check execution and authority

Identify the verifier, exact target, fixture/setup, supported driver, timeout, evidence destination, and cleanup/recovery owner. Prove prerequisites with read-only checks where practical; keep untested feasibility labeled. Inspect the dependency graph for cycles and name the artifact or decision that releases each dependent phase. Separate implementation, verification, and approval responsibilities where the task needs that separation. A sequential self-review is valid evidence of that pass, not independent review.

Check authorization against the actual request. A plan, available tool, passing test, or workflow reference does not authorize publication, merge, deployment, or messages. Use existing authorization; ask only for a genuinely missing decision and continue unaffected work.

**Exit:** each phase is ready to execute within the current scope or blocked by a named prerequisite. No implementation or acceptance pass is implied by readiness.

## 5. Record findings and close the right outcome

Use a compact row for each finding:

`A-ID | reachable failure / consequence | missing proof or decision | resolver | dependent phase`

Fix the plan or keep the affected phase blocked. When handing off a partial plan, state its usable scope and unresolved conditions. Before implementation closure, inspect actual attempts using the contract's evidence and change rules; resolve contradictory results and scope decisions. Return passed conditions with evidence, failed/blocked/not-run conditions with next actions, and separate delivery states.

**Exit:** a reader can tell what may start, what has actually passed, and what still prevents completion. Reviewer confidence and structural-check success cannot substitute for evidence.
