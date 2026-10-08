# feature

**Use for:** New or changed behavior.

Read [host capabilities](../hosts.md) and the relevant [principles](../principles.md) before acting.

1. Define user-visible acceptance criteria and relevant regression boundaries.
2. Choose the domain model and ownership shape. Read the design guide when alternatives materially affect callers.
3. Implement one coherent unit at a time; run the appropriate check after each.
4. Use the verification guide on the real surface, then review the diff and report what remains unverified.

**Principles:** [model-the-domain](../principles/model-the-domain.md), [experience-first](../principles/experience-first.md), [sequence-verifiable-units](../principles/sequence-verifiable-units.md), [prove-it-works](../principles/prove-it-works.md).

**Done:** The requested behavior and relevant regression checks pass on the identified revision.
