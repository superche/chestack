# Goals, issues, and work accounting

Use for project-management assessment, milestone creation or acceptance, issue tracking, and work accounting. For an assessment-only request, inspect and report gaps without changing remote state. Read the [requirements contract](requirements/contract.md) and preserve its requirement IDs, evidence states, and scope-change rules.

## Establish the source of truth

1. Inspect the actual remote host, repository/project or group, current identity, permissions, existing milestones, issues, and project conventions. Read all relevant pages of results before claiming coverage. Check sandbox and network restrictions before diagnosing account access failures.
2. For GitHub or GitLab projects, use their native milestones, issues, labels, assignees, discussions, and PR/MR links through an available connector, CLI, or API. Prefer existing records and conventions. Boards and project views organize those records; they do not replace the goal or evidence record. Verify installed capabilities and server version before choosing commands.
3. Use a milestone for a bounded goal and issues for independently trackable work, defects, risks, decisions, and follow-ups. Search before creating. Link duplicates to the canonical issue. Work without a settled goal can remain in the issue backlog; do not invent a milestone for every small change.
4. Keep the current goal, scope, acceptance conditions, owner, dependencies, and dates when agreed in the milestone description or one linked goal issue. Use a linked issue for durable review discussion. Local plans and checkpoints link to the native records. If access is unavailable, keep a clearly marked unpublished draft and reconcile it before any later write; do not maintain a competing authoritative ledger.

[GitHub milestones](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/about-milestones) group issues and PRs within a repository. [GitLab milestones](https://docs.gitlab.com/user/project/milestones/) support project and group scope. For cross-repository GitHub goals, link repository milestones from a coordinating issue or project view; do not imply a native cross-repository milestone. Check the actual GitLab instance before relying on group features.

## Gate 1: adversarial review before creation

Draft the goal and issue breakdown before creating the native milestone. Apply the [acceptance review](requirements/acceptance-review.md) and actively try to disprove that the proposal is worthwhile, bounded, and verifiable:

- Does it name an observable outcome, or only activities and outputs?
- Which user requirement is missing, and which proposed work is unnecessary?
- Can the proposed evidence look successful while the goal is unmet?
- Are dependencies, ownership, target environment, failure/recovery paths, and any promised date feasible?

Record the reviewed draft revision, reviewer/method, concrete objections, evidence, dispositions, unresolved blockers, and verdict (`pass`, `revise`, or `blocked`). Resolve material objections and review the revised proposal before creation. A mandatory adversarial review can be a distinct sequential self-review; label it as such. Use a separate reviewer only when allowed under the [delegation contract](delegation.md). If the user requires independent review, its absence leaves the gate blocked.

After a passing review and within existing write authorization, recheck for duplicates, create the milestone and required issues, link the review record, and read back the saved scope, associations, and identifiers. A write timeout has an unknown outcome: inspect live state before retrying. A local draft, tool exit, or review verdict does not prove successful creation.

## Track issues and account for work

Each issue carries the problem or outcome, milestone when applicable, owner, acceptance condition, dependencies, and relevant implementation/evidence links. Reuse the project's labels for kind, priority, and blocked state. Distinguish implementation finished from verified and accepted; a PR/MR auto-closing an issue does not establish acceptance.

Record material work in the issue description and chronological comments: date/actor, action or decision, reason, evidence/PR/MR, observed result, and next step or blocker. Preserve failed attempts and scope decisions. Keep estimates separate from actual effort; record time or cost only when requested or part of the project's convention, with units and provenance. Unknown effort remains unknown. Use native time tracking when available rather than duplicating totals in a second ledger. Exclude credentials and unrelated private transcripts.

Before authorized remote writes, verify the selected host, identity, and target; read back the result. Issue comments are external messages and follow the host's messaging authorization rules. With missing authorization, prepare the exact update locally and report it as unpublished.

For material goal, acceptance, dependency, or target changes, preserve the prior revision and repeat the creation review on the amended proposal before dependent execution. Reconcile issue membership and invalidate affected evidence using the requirements contract. Moving an unmet issue out of a milestone is a scope decision requiring the authorized decision owner, not proof of completion.

## Gate 2: adversarial review before acceptance

1. Read the current goal revision, complete issue membership including removed/deferred work, open blockers, PRs/MRs, and actual delivery evidence. Map every current acceptance condition to inspected evidence at the required target and environment.
2. Try to falsify completion: all issues closed but the user flow fails; CI passes on the wrong head; merged code is not deployed; only a mock ran; an issue was moved to inflate progress; a retry concealed a failure. Apply the acceptance review to relevant counterexamples and resolve findings with evidence.
3. Record the target and goal revision, reviewer/method, findings and dispositions, evidence per acceptance condition, residual scope, and verdict. `not-run`, `failed`, `blocked`, stale evidence, or unresolved material objections prevent acceptance. Issue counts, milestone percentages, due dates, and platform closed state are tracking signals only.
4. After a passing review, all current conditions pass, and any explicit user acceptance gate is satisfied, record the acceptance decision and close the milestone within authorized scope. Re-read the milestone and review links. If scope was explicitly reduced, report acceptance of that reduced scope and link remaining issues. Cancellation or supersession may close a milestone when authorized, but must be recorded as such rather than accepted.

**Done:** Report the native milestone/issue links, current goal revision, creation and acceptance review status, verified outcomes, blockers, and unpublished updates. This is an agent procedure; it does not install a server-side enforcement rule, bot, or scheduler.
