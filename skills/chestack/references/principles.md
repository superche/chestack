# Principle index

Read the full linked rule before applying it. These are reference files, not independently registered skills. User requests can name a principle through `$chestack`.

## Core

- [laziness-protocol](principles/laziness-protocol.md): Scope or abstraction grows.
- [foundational-thinking](principles/foundational-thinking.md): Choosing the implementation shape.
- [redesign-from-first-principles](principles/redesign-from-first-principles.md): A new requirement strains an existing design.
- [attack-the-premise](principles/attack-the-premise.md): Repeated fixes fail the same check.
- [subtract-before-you-add](principles/subtract-before-you-add.md): Adding a layer to an already complex system.
- [minimize-reader-load](principles/minimize-reader-load.md): A change requires tracking hidden state or indirection.
- [outcome-oriented-execution](principles/outcome-oriented-execution.md): A planned rewrite or migration.
- [experience-first](principles/experience-first.md): Product behavior conflicts with implementation convenience.
- [exhaust-the-design-space](principles/exhaust-the-design-space.md): A consequential design has no clear precedent.
- [build-the-lever](principles/build-the-lever.md): Repetitive edits, measurements, or checks.

## Architecture

- [model-the-domain](principles/model-the-domain.md): Conditions repeat or invalid states proliferate.
- [boundary-discipline](principles/boundary-discipline.md): Handling external inputs or framework integration.
- [type-system-discipline](principles/type-system-discipline.md): Designing types or signatures.
- [make-operations-idempotent](principles/make-operations-idempotent.md): Retries, crashes, or partially completed work.
- [migrate-callers-then-delete-legacy-apis](principles/migrate-callers-then-delete-legacy-apis.md): Replacing an internal API.
- [separate-before-serializing-shared-state](principles/separate-before-serializing-shared-state.md): Concurrent workers may mutate one resource.

## Verification

- [prove-it-works](principles/prove-it-works.md): Before claiming success.
- [fix-root-causes](principles/fix-root-causes.md): Debugging an observed defect.
- [sequence-verifiable-units](principles/sequence-verifiable-units.md): Multi-step work or stacked changes.
- [test-behavior-not-implementation](principles/test-behavior-not-implementation.md): Writing or retaining tests.
- [explain-the-number](principles/explain-the-number.md): Reporting or acting on a measured result.

## Delegation

- [guard-the-context-window](principles/guard-the-context-window.md): Large reads or long investigations.
- [never-block-on-the-human](principles/never-block-on-the-human.md): A reversible step is already authorized.

## Meta

- [encode-lessons-in-structure](principles/encode-lessons-in-structure.md): The same correction recurs.
