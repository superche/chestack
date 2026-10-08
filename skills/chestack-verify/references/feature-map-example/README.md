# CheStack CLI example map

This worked map exercises two actual public commands from this repository. It illustrates the feature-map format; it does not cover all CheStack utilities. Run it from a CheStack checkout with Python 3.10+ and Git. No account, network, GUI, or additional Python package is needed.

## Baseline and identity

From the repository root, run these commands in one shell and retain its variables for both feature recipes:

```sh
export CHESTACK_VERIFY_REPO="$PWD"
export CHESTACK_VERIFY_RUN="$(mktemp -d "${TMPDIR:-/tmp}/chestack-verify.XXXXXX")"
mkdir "$CHESTACK_VERIFY_RUN/state" "$CHESTACK_VERIFY_RUN/evidence"
git rev-parse HEAD > "$CHESTACK_VERIFY_RUN/evidence/revision.txt"
python3 --version > "$CHESTACK_VERIFY_RUN/evidence/python.txt"
python3 skills/chestack/scripts/chestack.py --help > "$CHESTACK_VERIFY_RUN/evidence/cli-help.txt"
```

Before driving, confirm `CHESTACK_VERIFY_REPO` is the intended checkout and the recorded revision is the target. Confirm help lists `plan-check` and `log`. The CLI's own `doctor` checks executable availability only; it does not establish repository identity or authentication. These commands are short-lived, so no shared server or background process needs to be launched.

## Driving and evidence

Each feature recipe below runs in a separate Python invocation from that same shell. It uses the public CLI via `subprocess`, with a 10-second timeout per invocation. Artifacts record arguments, stdout, stderr, and exit status. The launch record identifies the target revision; persistent-state assertions use an independent file read. On timeout, the direct child is killed and waited for by `subprocess.run`; no process-name cleanup is used.

## Features

- [Plan structure validation](plan-check.md): valid and incomplete plan input, exit behavior, and read-only preservation.
- [Decision log append](log.md): append behavior, independent JSONL readback, and rejection of corrupt existing data without mutation.

## Cleanup

After both recipes, or after any failed attempt, remove only the owned `state` directory. Run this from the same shell even if an assertion failed:

```sh
python3 - <<'CLEANUP'
import os, shutil
from pathlib import Path
run = Path(os.environ['CHESTACK_VERIFY_RUN'])
shutil.rmtree(run / 'state', ignore_errors=True)
evidence = run / 'evidence'
assert evidence.is_dir()
for artifact in evidence.iterdir():
    assert artifact.is_file()
    artifact.read_bytes()
print('Retained evidence:', evidence)
CLEANUP
```

The scratch run directory is intentionally retained for evidence. Before retrying, start a new baseline with a new run directory. A failure or timeout remains a failed/incomplete case; cleanup is not a passing result. Run records belong in scratch artifacts, not in this example directory.
