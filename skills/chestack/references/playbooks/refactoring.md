# refactoring

**Use for:** Structure changes while behavior stays stable.

Read [host capabilities](../hosts.md) and the relevant [principles](../principles.md) before acting.

1. Inventory callers and pin representative current behavior.
2. Name the structure that reduces branching, invalid states, or reader load. Compare alternatives if the change crosses module boundaries.
3. Remove obsolete paths, migrate callers in small units, and delete replaced APIs once their consumers move.
4. Rerun the behavior pin and inspect the whole diff for accidental user-visible changes.

**Principles:** [subtract-before-you-add](../principles/subtract-before-you-add.md), [model-the-domain](../principles/model-the-domain.md), [migrate-callers-then-delete-legacy-apis](../principles/migrate-callers-then-delete-legacy-apis.md), [minimize-reader-load](../principles/minimize-reader-load.md).

**Done:** Behavior is preserved and the report identifies the concrete complexity removed.
