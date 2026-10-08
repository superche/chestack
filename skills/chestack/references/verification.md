# Verification against the real outcome

1. Name the claim, exact target revision or artifact, environment, action, and pass predicate before choosing a check.
2. Run the narrowest check that directly observes that predicate. Use unit tests for local contracts, integration checks for boundaries, and the actual app or CLI for user-visible behavior.
3. Identify the real target: repository, branch or SHA, process, port, window, account, dataset, or deployment. A successful check against another instance does not verify this change.
4. Preserve a command, result, and relevant artifact. For UI work capture matching states and interactions. For recordings resolve the target window first and inspect representative frames before claiming acceptance.
5. Report failures and incomplete capability honestly. Passing compilation or a worker's report alone does not prove behavior.

## Create a verification recipe

When requested, write a repository-local recipe or skill containing prerequisites, safe fixture setup, the exact action, expected observable result, cleanup, and known environment limits. Include a feature map connecting each behavior to its probe. Keep credentials outside the recipe. Run at least one representative scenario before calling the recipe validated.

## Maintain a recipe

Compare every feature-map entry with current code and the available runtime. Exercise the documented path, update stale commands, remove obsolete cases, and add coverage only for real supported behavior. Keep unsupported cases explicit rather than inventing successful runs.

## Focused regression testing

Use a failing test first when the user requests TDD or the defect has a cheap, stable local boundary. Observe failure for the intended reason, fix the defect, then observe success. Do not create tests that merely mirror implementation details. Use [measurement](measurement.md) for numerical claims.

Finish with separate evidence states: source inspected; local test passed; real behavior observed; CI passed; reviewed; merged; deployed; accepted. Only assert the states actually checked.
