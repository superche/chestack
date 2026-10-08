# Feature-map contract

A feature map records observable product behavior and repeatable ways to verify it. It is maintained guidance, not a run log or a source-code inventory.

## Index

Use `features/README.md` as the index inside a generated verification skill. State the covered application/surfaces, shared prerequisites, target-identity check, fixture/reset conventions, harness invocation, evidence directory, cleanup ownership, and known exclusions. Link every feature leaf once. Keep implementation source citations in audit evidence unless a path is needed to launch or drive the product.

## Feature leaves

Use a stable filename and H1 with a short user-visible behavior description, then these four H2 sections:

1. **Sub-features:** stable IDs and one observable behavior per ID.
2. **User entry points:** each supported route, control, shortcut, CLI command, or public API; include materially different states or access prerequisites. Assign entry-point IDs when a feature has several paths.
3. **Drive and observe:** preconditions, reset state, exact supported command or tool action, completion predicate, timeout, proof capture, and cleanup. Connect each case to feature and entry-point IDs. Document alternate paths as executable cases, not only a list of controls.
4. **Gotchas:** traps that change the interpretation of evidence, such as focus, debounce, stale builds, persistence, feature flags, or dry-run side effects.

For a host browser tool, an observed role/name plus a semantic action is acceptable; do not invent an executable wrapper command. For scripts, provide the exact working directory and invocation. Evidence must pair the action with the observed result. Confirm mutations through a second public read path or appropriate read-only persistence observation. Internal state injection may prepare fixtures but cannot prove the user action it bypasses.

## Coverage and evidence

A scratch result table can use:

| Feature / entry / case | Target revision and runtime | Status | Observed predicate | Evidence or blocker |
|---|---|---|---|---|

Statuses are `passed`, `failed`, `blocked`, and `not-run`. Distinguish source findings from runtime observations. One passing browser flow does not verify a CLI or keyboard entry. When one case covers several sub-features, list their IDs explicitly. Capture bounded stdout/stderr and exit status for CLI/API probes; for UI capture the interaction and matching visual/semantic state. Redact secrets and private fixture data before sharing.

The [worked example](feature-map-example/README.md) uses actual CheStack CLI commands in a disposable workspace. Its two leaves illustrate public file mutation and read-only validation; they are not an exhaustive verification map for CheStack and do not prescribe a browser or framework.
