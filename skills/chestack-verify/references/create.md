# Create a project verification skill

Deliver a repository-local skill that another agent can execute without this conversation. Use `.agents/skills/verify-<app>/` when the project has no established host-compatible location. Respect existing conventions and the requested destination. Inspect existing verification skills before creating a duplicate.

## Discover the executable contract

Read repository instructions, run scripts, routes, command help, tests, and existing harnesses. Establish:

- User surfaces: browser, desktop, CLI/TUI, service/API, or library; include alternative entry points to the same behavior.
- Launch and readiness: actual build/start command, working directory, dependencies, fixtures, authentication, expected ready signal, and bounded timeout.
- Driving: reuse existing automation first. Choose available browser controls, PTY, HTTP client, or public library API according to the actual surface.
- Identity: checkout/revision and runtime identity such as executable path, process, port, window, account, or dataset. Explain how to detect a stale build or another instance.
- Isolation: owned process/session handles, separate profiles, ports and disposable data. For an authorized attached instance, define permitted actions and fixture restoration; preserve the user's process.
- Evidence: observable predicates, capture method, destination outside disposable runtime state, and redaction of sensitive output.

Probe the documented launch path before encoding it. Diagnose failures using repository evidence. Fix verification scaffolding within scope; report product/build defects or missing access instead of silently expanding into product repair. If execution is unavailable, save a clearly labeled draft with exact missing prerequisites rather than inventing working commands.

## Write the package

Use [Create Skill](../../chestack-create-skill/SKILL.md) for packaging and metadata. The generated skill names the application and verification surface in its description, links its feature index, and provides these operating contracts:

| Contract | Required content |
|---|---|
| Launch | Exact working directory, startup/build commands, safe fixtures, readiness predicate and timeout. For short-lived commands, use a fresh invocation or PTY per case. |
| Doctor | Read-only target and readiness checks. Recheck each fresh session and after unexpected behavior; a healthy process alone does not prove healthy UI state. |
| Drive | Real user entry points and stable handles observed in this project; ordered actions with observable assertions. |
| Evidence | Action plus resulting state, side-effect confirmation, case ID, target revision, output paths, and capture instructions. |
| Cleanup | Finally-style teardown on success, failure, timeout, or cancellation; remove only owned resources and restore touched fixtures. Retain and check evidence after teardown. |
| Helpers | Document every bundled helper's invocation and prerequisites; make directly invoked scripts executable. Reuse repository tools rather than wrapping them without a concrete need. |

Use [Control CLI](../../chestack-control-cli/SKILL.md) or [Control UI](../../chestack-control-ui/SKILL.md) when that surface must be driven. Generated guidance must name the tools actually available in the target project, with an explicit capability gap when absent. A test-only setter is not proof of a public entry path. Observe what a dry-run or mock bypasses before interpreting its result.

## Seed the feature map

Read the [feature-map contract](feature-map.md) and [worked example](feature-map-example/README.md). Select a bounded initial set of important supported behaviors from real source entry points; list known exclusions. Create an index and one leaf per feature. Map each alternate entry point to its own action and predicate, including meaningful failure, cancellation, persistence, or recovery behavior where supported. Avoid scaffolding placeholders in the delivered map.

## Execute the generated instructions

Run launch → doctor → one representative mapped feature → evidence capture → cleanup using the new instructions, not an undocumented shortcut. Include the feature's relevant failure or recovery boundary when safely available. After every failed attempt, clean owned residue before retrying. After teardown, verify captured artifacts still exist and are readable.

Correct recipe or harness errors and re-run affected paths. A successful sample validates only those cases; identify the remaining map entries as untested. If no feature can execute, deliver a draft and its blocker, never a validated skill.

**Done:** package and relative references resolve from the installed location; at least one feature has observed proof and successful cleanup for a validated delivery; the handoff names the skill invocation, evidence location, checked cases, and remaining gaps. Keep transient run reports outside the distributed skill. Point to maintain mode for future drift; create schedules only when requested.
