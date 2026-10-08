# Chestack maintenance

Keep the core host-capability based and default to the current Codex / ChatGPT model. New vendor-specific runtimes belong in optional adapters, never in mandatory entry instructions.

Before editing, read the relevant skill and its references. Keep user-facing instructions in clear Chinese and agent procedures in concise English. Preserve exact file and tool identifiers.

After changes, run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v`. For workflow changes, evaluate realistic tasks against the edited artifact and record actual evidence in `docs/validation.md`; distinguish structural tests from model behavior. Keep the catalog, source mapping, and manifest version consistent.

The repository belongs to `superche`. Verify the active GitHub identity before remote writes. Keep git identity configuration local. Preserve the upstream attribution. Never commit credentials, local state, private transcripts, or generated installation caches.

For permission errors, first determine whether the sandbox or network restriction caused them. Use authorized scoped escalation before requesting human account changes.
