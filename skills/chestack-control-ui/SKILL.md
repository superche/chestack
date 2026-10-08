---
name: chestack-control-ui
description: "Drive and verify a browser, desktop, or Electron interface. Use for real UI reproduction, interaction acceptance, screenshots, accessibility checks, visual comparisons, or UI profiling. Source-only UI explanation does not require live control."
---

# CheStack Control UI

Read the [host contract](../chestack/references/hosts.md). Use the repository's existing UI harness or the browser/computer-control tools exposed in this session. Follow each tool's own setup and policy. If none can reach the target, provide a runnable verification recipe and mark live UI acceptance unverified.

## Bind the right surface

Identify the app, source revision, URL or process, window/tab identity, account/fixture, viewport, and acceptance condition. Reuse a running target only after establishing that it is the requested instance. Start a development server only when required, with an owned process and discovered port.

For browser or Electron tests, prefer an existing harness such as repository-installed Playwright or host browser control. Attach over CDP only when the app supports it and that access is authorized; bind a newly created debug endpoint to loopback. Select a page by a positive app marker plus URL/title, never tab order alone. For native desktop UI, use the exposed computer-control surface and verified application/window identity.

## Interaction loop

1. Read a fresh accessibility/DOM snapshot or screenshot.
2. Choose a target grounded in that observation, preferring accessible role/name or stable app selectors. Use coordinates only from a fresh screenshot when semantic targeting is unavailable.
3. Perform one meaningful interaction: click, type, keypress, scroll, drag, navigate, or resize.
4. Wait for an observable state change with a timeout. Re-read the surface after navigation or structural changes; reacquire stale targets.
5. Verify the user-visible result and the relevant persisted or network result when the claim requires it. Cover applicable loading, empty, error, recovery, focus, and success states.
6. Save focused before/after evidence and note console/network errors that affect acceptance. Keep credentials and unrelated private content out of artifacts.

Use higher-level APIs before raw CDP. For performance or memory claims collect a matching trace/profile and apply the [measurement checklist](../chestack/references/measurement.md). Do not add project dependencies solely for an ad-hoc probe without authorization.

## Evidence and cleanup

For visual parity compare the same state, data, and viewport. For a requested recording, verify the target window before capture and inspect first, middle, and last frames. A screenshot of a mockup is not evidence of a live interaction.

Close only pages, profiles, servers, and debug processes created by the run. Disconnect from user-owned instances without terminating them. If a tool's close behavior is ambiguous, keep the attached instance intact and report the remaining connection.

Return the target identity, tested flows, observed pass/fail results, relevant captures, and remaining acceptance gaps.
