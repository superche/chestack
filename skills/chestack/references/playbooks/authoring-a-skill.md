# authoring-a-skill

**Use for:** Create or modify reusable agent guidance.

Read [host capabilities](../hosts.md) and the relevant [principles](../principles.md) before acting.

1. Identify concrete triggering prompts, required capabilities, and the output acceptance condition.
2. Use the available skill-creator guidance. Keep entry instructions small, with conditional references and executable checks for deterministic work.
3. Use the OpenAI invocation policy and host capability guide. Keep provider-specific adapters outside the core contract.
4. Validate links, metadata, and scripts. Forward-test realistic prompts without leaking expected answers when authorized agent validation is available.

**Principles:** [encode-lessons-in-structure](../principles/encode-lessons-in-structure.md), [minimize-reader-load](../principles/minimize-reader-load.md).

**Done:** The package validates and behavioral evidence or remaining evaluation gaps are recorded.
