# Contributing

Keep each change focused. Explain the triggering scenario, the problem, the resulting behavior, and how it was verified.

1. Use principles for reusable decisions, playbooks for execution steps, and host guidance for capability and permission boundaries.
2. Add a top-level skill only when it serves a distinct user invocation scenario.
3. Inherit the current model. Discover available capabilities instead of assuming agents, scheduling, or another host's commands exist.
4. When changing scripts, cover meaningful failure cases: preserving user files, error exits, unknown states, and read-only boundaries.
5. Run the validation commands in the [README](README.md) before submitting. For workflow evaluations, report the inputs, environment, observed results, and coverage gaps in the review.
6. Submit scoped changes in separate pull requests. Merge and release only with the repository owner's authorization.

When updating a locally copied installation, compare and preserve existing modifications first, then install into an explicitly chosen destination. The installer never automatically overwrites existing skill directories.
