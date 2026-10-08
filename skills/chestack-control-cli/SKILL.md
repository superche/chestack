---
name: chestack-control-cli
description: "Drive, inspect, and profile an interactive CLI or TUI with a repeatable local harness, including prompts, keyboard flows, hangs, and terminal layout."
---

# CheStack Control CLI

Read the [host contract](../chestack/references/hosts.md). A terminal session or executable test harness is required for live CLI acceptance. Without one, provide the runnable probe and mark execution unverified.

## Establish the target

Identify the exact executable, arguments, working directory, revision, fixture, and observable success condition. Inspect the repository's existing integration tests, PTY helpers, expect scripts, and demo tools. Reuse a suitable harness before adding a dependency.

For plain batch commands, capture stdout, stderr, and exit status. For terminal-sensitive behavior, use an exposed host PTY, an existing PTY library, or an available tmux/Expect harness. Pipes do not verify TUI rendering, keyboard focus, or terminal dimensions. On platforms without a POSIX PTY, use the host's terminal capability or an existing platform adapter.

## Drive and observe

Put session ownership and cleanup in an unconditional finalization path (for example, `try/finally` in a scripted harness). Prompt timeouts, failed assertions, and interrupts must reach cleanup as well as successful runs.

1. Start an isolated owned session with a disposable fixture and explicit terminal dimensions. Record its process/session identity. Give every wait and run a timeout.
2. Read the current output or terminal screen. Wait for a concrete prompt or state; fail with captured diagnostics if it never arrives.
3. Send one action, then observe its result before the next action. Exercise applicable Enter, arrows, Escape, interrupt, resize, and recovery paths. Send control characters only when the expected state supports them.
4. Assert the actual result, not merely prompt disappearance: exit code, output value, written file, state change, or restored prompt. Compare before/after behavior for a defect.
5. Retain the minimal transcript and required artifacts, excluding credentials. For hangs, collect the current screen and process/stack evidence before interruption.
6. In cleanup, stop and reap only the processes or sessions created by this run. Preserve attached user-owned terminals and evidence requested by the user. Clean disposable fixtures when safe.

## Profiling and recordings

Use a supported local runtime inspector only when needed. Bind debug endpoints to loopback, discover their actual address, and close endpoints created by the probe. Apply the [measurement checklist](../chestack/references/measurement.md) to startup, CPU, and memory comparisons. A terminal recording should show the identified target session, representative interaction, and final result.

Return target identity, tested interaction, observed outcome, transcript/artifact locations, and untested paths. A launch log alone is not CLI acceptance.
