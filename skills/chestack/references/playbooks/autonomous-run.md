# autonomous-run

**Use for:** The user authorizes a bounded unattended run.

Read [host capabilities](../hosts.md) and the relevant [principles](../principles.md) before acting.

1. Define an observable done predicate, resource budget, stop conditions, and actions requiring a user gate.
2. Execute small verified units and keep a decision trail through the operations guide.
3. Use the host scheduling capability only if the user requested continuation later. Preserve quiet-until-actionable notification intent.
4. Checkpoint on capability loss or a real gate; continue independent authorized work and report partial results honestly.

**Principles:** [never-block-on-the-human](../principles/never-block-on-the-human.md), [sequence-verifiable-units](../principles/sequence-verifiable-units.md), [prove-it-works](../principles/prove-it-works.md).

**Done:** The done predicate is observed or the run ends with a usable checkpoint and a specific unmet condition.
