# GitHub identity, status, and delivery

Check `gh api user --jq .login` and the target repository before writes. Respect the owner the user requested. Keep commit identity local to that repository; GitHub's authenticated account and git author are separate settings. Never disclose credentials.

For a PR status snapshot, run the bundled `pr-status --repo OWNER/REPO --pr NUMBER`. It returns GitHub metadata and required checks, labels collection gaps, and never returns an affirmative merge-ready verdict. It is a read-only helper, not a watcher or merger.

Before declaring readiness, inspect all of:

- Exact current head SHA, base branch, open/draft state, and conflicts.
- Required checks and the forge's merge-state decision, including branch protection.
- Review decision and unresolved review threads; fetch every page when using GraphQL.
- Whether checks and review apply to the current head, plus any user or repository gate.
- Dependencies and the lowest unmerged frontier for a stack.

Treat unknown, stale, missing, or unreadable state as unresolved. An empty check list is not proof that no required gate exists. A successful command exit alone is not merge-readiness evidence.

For creation, use a scoped branch, review the full diff, run the required checks, and publish only within the request. Use `--body-file` for prose. Attach PRs with the host's artifact API when available. Keep draft status aligned with readiness and user intent.

Merge only with explicit user authorization and a fresh readiness check. Use the forge's expected-head guard, such as `gh pr merge --match-head-commit SHA`, when supported by the installed CLI, and re-read the result. A changed head invalidates the prior check. Never disable protection, override reviews, or force-push a shared branch to obtain a green result.

Future monitoring requires a user-requested native schedule or an actively running bounded session. A local checkpoint or a JSON status snapshot does not schedule another turn.
