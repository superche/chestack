# CheStack

Engineering workflows for **Codex / ChatGPT**. Turn a goal into scoped work, then verify the result against code, terminal output, live interfaces, and GitHub state. CheStack inherits the current session's model and uses the tools available in the host.

## Install

Your GitHub identity must have access to this private repository.

```sh
codex plugin marketplace add superche/chestack --ref main
codex plugin add chestack@superche-chestack
```

In the desktop app, you can also install from the added marketplace. Start a new session or refresh the skill list after installation.

For hosts that discover local skills, copy the complete bundle into a project's skill directory:

```sh
gh repo clone superche/chestack
cd chestack
python3 scripts/install_skills.py --dest /absolute/path/to/project/.agents/skills
```

For a personal installation, use `~/.agents/skills` as the destination. The installer preserves existing directories and stops the entire installation on a name collision. Choose either plugin installation or local copying to avoid duplicate entries.

## Use

Start with `$chestack` to route a task to the appropriate workflow, or select a specialized skill directly:

```text
$chestack Find the root cause of this bug, fix it, and verify the behavior.
$chestack-deslop Remove redundant code introduced on this branch while preserving behavior.
$chestack-control-cli Verify input, cancellation, and exit behavior for this interactive command.
$chestack-control-ui Verify this page's submission, error, and recovery flows.
$chestack-verify Create a project-local verification skill with a feature map.
$chestack-verify Audit the existing verification skill against source and live behavior.
$chestack-create-skill Turn this procedure into a reusable skill.
$chestack-babysit Resolve this PR's review and CI blockers until it is ready to merge.
```

In Codex, select skills with `$skill-name`. In ChatGPT environments that support plugins and skills, use the available skill picker.

| Skill | Result |
|---|---|
| `chestack` | Investigation, planning, implementation, debugging, refactoring, and delivery routed from the requested outcome |
| `chestack-setup` | Host capability assessment and workflow configuration |
| `chestack-explain` | Source-backed explanations of behavior, architecture, and design decisions |
| `chestack-review` | Actionable findings with locations, impact, and verification steps |
| `chestack-verify` | Behavior verification, project-local verification skills, and feature-map maintenance |
| `chestack-reflect` | Recurring lessons encoded as structural constraints or verifiable rules |
| `chestack-deslop` | Simpler, consistent code with behavior preserved |
| `chestack-control-cli` | CLI/TUI interaction, output, exit, and performance verification |
| `chestack-control-ui` | Interaction and visual verification for browsers, desktop apps, and Electron |
| `chestack-create-skill` | Installable skills with complete references and validated metadata |
| `chestack-babysit` | PR blocker resolution and a current merge-readiness assessment |

The host may automatically select `chestack-setup`, `chestack-deslop`, `chestack-control-cli`, and `chestack-control-ui` when their descriptions match the task. All four also support explicit invocation. The main entry and remaining skills require explicit selection; an active workflow can read their instructions by reference.

CheStack reads **24 principles** and **23 playbooks** on demand. You can name a principle in a request, for example: `$chestack Apply prove-it-works and show the observed result.` See the [architecture and complete module map](docs/architecture.md) and [workflow routes](skills/chestack/references/routes.md).

## Capabilities and boundaries

- The current host supplies the model, terminal, browser, connectors, agents, and scheduling tools. Missing capabilities are reported as execution or verification gaps.
- CLI/TUI checks use observable terminal sessions. UI checks use available browser controls, desktop controls, or repository test tools.
- Skill authoring uses `skill-creator` when available, with a standalone package and validation contract as a fallback.
- PR follow-up uses CheStack's own workflow through `gh` or a GitHub connector. Merging and future scheduling require the corresponding authorization.
- Installation starts no background services, listeners, or automations.
- Reports distinguish local checks, CI, review, merge, deployment, and live acceptance.

## Development

Python 3.10+ is required for the bundled utilities and tests; both use only the standard library.

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 skills/chestack/scripts/chestack.py doctor
```

The utility commands are `doctor`, `plan-check`, `log`, and `pr-status`. A PR snapshot does not replace a complete merge-readiness assessment.

See [Contributing](CONTRIBUTING.md), [License](LICENSE), and [Third-party notices](NOTICE.md).
