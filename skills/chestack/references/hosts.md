# Host capability contract

Choose adapters from the tools exposed in the current session. Product names alone do not establish capabilities. Read this contract before any entry skill acts.

| Capability | Codex / ChatGPT with tools | When absent |
|---|---|---|
| Read files and execute commands | Use the provided file and terminal tools in the authorized workspace. | Work from supplied sources; label execution unverified. |
| Skills and references | Follow the installed skill's filesystem or resource-provider paths. | Use provided contents; request only the material needed for the next step. |
| Repository mutations | Respect scoped instructions, worktree ownership, and sandbox approval. | Produce a reviewable patch or plan; never claim it was applied. |
| Independent agents | Use the exposed subagent API only when current instructions allow delegation. | Perform sequential passes, explicitly not independent review. |
| Browsers / desktop control | Use available browser, computer-use, or product-specific control tools. | Run narrower checks and state that live UI acceptance remains open. |
| Private services | Use authorized connectors, MCP tools, or authenticated CLI. | Request the minimum missing access or supplied evidence. |
| Scheduled continuation | Use a native automation tool after the user requests scheduling. | Save a checkpoint and report that no future execution is scheduled. |
| GitHub | Use a connected GitHub tool or authenticated `gh`. | Prepare local changes and preserve the publishing step as pending. |
| Persistent preferences | Use repository-local guidance within the requested setup scope. | Keep preferences in the current conversation. |

## Model and delegation defaults

Inherit the user's current model. A model-specific field is optional, host-defined, and used only when the user requests that choice and the host supports it. Do not hardcode model IDs or reasoning tiers. More workers are not automatically better: scope, independent evidence, and context cost decide the shape of delegation.

Read [delegation](delegation.md) before spawning. Distinguish private subagents from user-visible chats. Creating or messaging another user-visible chat requires the user's authorization under the host's rules. This package does not create chats, schedules, or remote agents at installation time.

## Permissions and identity

Use existing authorization without repeatedly asking for it. If a required call fails, distinguish command misuse, sandbox/network restriction, missing capability, and genuine account access failure. Use the host's scoped escalation mechanism for sandbox restrictions before asking the user to fix credentials. If escalation is rejected, report that actual rejection and its reason; do not retry through another route to bypass it.

Before GitHub writes, verify the selected identity and repository owner. Keep git author configuration repository-local. Never print tokens, copy account files into outputs, or change global authentication as an incidental setup step.

## Invocation and persistence

Codex users can explicitly select `$chestack` or the specialized skills. ChatGPT users can select the installed plugin or skill through the host's available picker. Each skill uses `agents/openai.yaml` with `policy.allow_implicit_invocation: false` to avoid hijacking unrelated tasks. Once invoked, the router reads ordinary reference files by path; those reads are not automatic skill invocation.

The host decides whether skill content persists across turns. Do not assume a mode badge, reminder field, command syntax, or hook from another product exists. For durable repository behavior, have the user request a scoped `AGENTS.md` pointer to the installed skill.

Format references: [Build skills](https://developers.openai.com/plugins/build/skills), [Build plugins](https://developers.openai.com/plugins/build/plugins). Actual session capability and higher-priority instructions take precedence over these portability notes.
