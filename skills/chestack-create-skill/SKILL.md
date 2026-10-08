---
name: chestack-create-skill
description: "Create or update a reusable skill for Codex or ChatGPT, including triggering metadata, conditional references, portable tools, and validation."
---

# CheStack Create Skill

1. Read the [host contract](../chestack/references/hosts.md). Identify concrete user prompts, expected results, required capabilities, and the authorized target directory. For edits, inspect the existing skill and preserve local conventions.
2. If the host exposes `skill-creator`, load its guidance and use its scaffold/validation helpers where available. This is an optional implementation adapter, not a required runtime dependency. Otherwise follow the package contract below directly.
3. Write concise common steps in `SKILL.md`. Place conditional material in named references with explicit trigger-and-path pointers. Add scripts only for deterministic work worth making repeatable.
4. Check that metadata matches the intended invocation, every local reference resolves, and any executable helper actually runs. Test a valid case and its meaningful failure boundary. For instruction behavior, evaluate representative prompts and report the difference between a walkthrough and executed results.
5. Deliver the usable skill, its invocation, output contract, and any unverified capability. Keep creation diaries and one-off test transcripts outside the distributed skill.

## Package contract

Use a directory named with lowercase letters, digits, and hyphens. Required `SKILL.md` frontmatter contains matching `name` and a concise `description` naming the result and triggering requests. Optional `agents/openai.yaml` supplies quoted `interface.display_name`, `interface.short_description`, and `interface.default_prompt` mentioning `$skill-name`.

Put OpenAI explicit-invocation policy in `agents/openai.yaml` as `policy.allow_implicit_invocation: false` when the user should select the workflow. Use implicit invocation only when the skill should automatically match an independent task. Do not copy another host's invocation fields.

Keep scripts and resources inside the installed bundle and validate references from their installed location. Record runtime prerequisites; never bundle credentials or assume local absolute paths. For repository discovery use the authorized `.agents/skills` directory; for plugin distribution use the package's `skills/` directory. Do not silently modify global preferences or install into another user's directory.

**Done:** The skill is saved in the agreed location, its metadata and references are valid, runnable helpers have observed results, and the user knows how to invoke it.
