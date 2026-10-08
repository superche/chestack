# Run a requirements-to-evidence example

Use this example to learn or check the planning contract with real CheStack CLI commands. It reuses the maintained verification recipes instead of introducing a second driver. Requires a checkout, Python 3.10+, Git, and an authorized local shell. It creates disposable local files only.

## Read and review the plan

Read [the plan](cli-plan.md), then apply the [acceptance review](../acceptance-review.md). Notice the negative cases: expected CLI rejection is a passing acceptance result only when the specified error and unchanged data are both observed. A1 through A5 start as `not-run`.

From the repository root, check the plan's format:

```sh
python3 skills/chestack/scripts/chestack.py plan-check skills/chestack/references/requirements/examples/cli-plan.md
```

Expected: exit 0 and `valid_structure: true`. This is a structure check on the example plan, not execution of its phases.

## Execute the existing recipes

1. Read [Control CLI](../../../../chestack-control-cli/SKILL.md). Use batch stdout/stderr/exit capture; this example makes no terminal-rendering claim.
2. Follow the [feature-map baseline](../../../../chestack-verify/references/feature-map-example/README.md) from the repository root. Confirm the recorded checkout/revision and help output. Also record `git status --short` and the relevant diff if the working tree is dirty; a commit SHA alone does not identify modified source.
3. Run the [plan-check recipe](../../../../chestack-verify/references/feature-map-example/plan-check.md) in that same shell. Inspect its results before starting Phase 2. A harness exception, timeout, or unexpected exit blocks dependent work until understood.
4. If Phase 1 passed, run the [decision-log recipe](../../../../chestack-verify/references/feature-map-example/log.md) with the same environment. Inspect stdout and independent JSONL readback.
5. In a shell finalization path or immediately after any failed attempt, run the baseline's cleanup. Remove only owned state; confirm evidence remains readable. Preserve the failed attempt before any retry.

## Map observations to acceptance

Record actual target, attempt time, action, status, and artifact with each row. Retain each recipe invocation and its stdout/stderr and exit status, including assertion failures; individual CLI artifacts do not capture a later harness assertion. The recipe artifacts hold arguments, output, exit code, and log readback; supplement them with the target record and the recipe's successful byte-preservation assertions. Inspect the artifacts, not only the final printed success message.

| Acceptance | Required observation |
|---|---|
| A1 | plan-valid.json records exit 0 and a positive structural verdict. |
| A2 | plan-incomplete.json records exit 1 and the specified missing-acceptance error. |
| A3 | Both input-preservation assertions complete successfully for those exact files and calls. |
| A4 | log-append.json records exit 0; independent readback contains exactly one matching record with all four submitted values. |
| A5 | log-corrupt.json records exit 2 and Invalid JSONL; byte-preservation assertion succeeds. |

Close this exercise only when all five conditions pass and the evidence survives cleanup. Those results establish this bounded CLI behavior; they do not establish arbitrary plan quality, independent review, or release readiness.

## Challenge the plan before trusting it

Make each change below in a separate disposable copy of cli-plan.md. Run plan-check on that copy, then review the resulting claim using the acceptance review. Keep the original example unchanged. These are semantic review exercises; the checker is not expected to reject them.

| Mutation or supplied evidence | Expected semantic finding |
|---|---|
| Replace Phase 1 Acceptance with `Looks good.` | Predicate is not observable and disagrees with the A-ID mapping; restore explicit conditions. |
| Drop A5 and treat the happy path as proof of R-LOG. | Malformed-data preservation remains in scope but has no evidence; keep the condition unresolved. |
| Mark A4 passed using stdout only. | Persistence remains unproven; inspect independent file readback. |
| Supply a passing run from a different checkout. | Actual target does not match the claim; identify and drive the intended target. |
| Supply a failed attempt followed by an unexplained pass. | Contradictory evidence remains unresolved; explain the difference or reproduce it. |
| Add concurrent append safety to R-LOG after the run. | Single-writer evidence does not cover the new requirement; add a new condition and scenario before claiming it. |
| Request deployed-service acceptance without access to that service. | Local CLI evidence cannot satisfy it; record the missing capability and block that condition. |

A reviewer must reach these findings from the request and observations, not merely echo the labels. These examples are teaching fixtures with visible expected outcomes, not held-out model evaluation tasks. For workflow evaluation, prepare different realistic inputs and grading criteria before running trials, following the [evaluation playbook](../../playbooks/eval.md).
