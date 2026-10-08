# Verification against the real outcome

1. Name the claim, exact target revision or artifact, environment, action, and pass predicate before choosing a check.
2. Run the narrowest check that directly observes that predicate. Use unit tests for local contracts, integration checks for boundaries, and the actual app or CLI for user-visible behavior.
3. Identify the real target: repository, branch or SHA, process, port, window, account, dataset, or deployment. A successful check against another instance does not verify this change.
4. Preserve a command, result, and relevant artifact. For UI work capture matching states and interactions. For recordings resolve the target window first and inspect representative frames before claiming acceptance.
5. Report failures and incomplete capability honestly. Passing compilation or a worker's report alone does not prove behavior.

For live CLI/TUI checks, read [Control CLI](../../chestack-control-cli/SKILL.md). For browser, desktop, or Electron checks, read [Control UI](../../chestack-control-ui/SKILL.md). Use the matching workflow before reporting runtime acceptance.

## Reusable verification

When asked to create a project-local skill or feature map, follow [Create](../../chestack-verify/references/create.md). To audit or update an existing package against source and live behavior, follow [Maintain](../../chestack-verify/references/maintain.md). Both use the [feature-map contract](../../chestack-verify/references/feature-map.md). Ordinary verification uses existing recipes without generating a new skill.

## Focused regression testing

Use a failing test first when the user requests TDD or the defect has a cheap, stable local boundary. Observe failure for the intended reason, fix the defect, then observe success. Do not create tests that merely mirror implementation details. Use [measurement](measurement.md) for numerical claims.

Finish with separate evidence states: source inspected; local test passed; real behavior observed; CI passed; reviewed; merged; deployed; accepted. Only assert the states actually checked.
