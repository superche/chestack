---
name: chestack-setup
description: "Inspect available host capabilities, explain Chestack installation, and configure only requested repository-local preferences."
---

# chestack-setup

Read [host capabilities](../chestack/references/hosts.md) and inspect which tools are actually available. If shell exists, run `python3 ../chestack/scripts/chestack.py doctor` from this skill directory. Explain the six entry skills and the main [router](../chestack/SKILL.md). Inherit the current model. Write preferences into the target repository only if the user requests persistent setup. Never modify global model, auth, or sandbox settings as a setup side effect. Installation alone starts no automation. Finish with available capabilities, missing capabilities, and a runnable first-task prompt.
