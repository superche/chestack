# Decision log append

A user appends a decision to a named JSONL file. Invalid existing data is rejected rather than extended or replaced.

## Sub-features

- `log-append`: a valid invocation persists one structured record.
- `log-readback`: an independent read observes the submitted values.
- `log-corrupt`: corrupt existing data produces exit 2 and remains unchanged.

## User entry points

- `log-cli`: `python3 skills/chestack/scripts/chestack.py log --path PATH --decision TEXT --reason TEXT --evidence TEXT --result TEXT` from the repository root.

## Drive and observe

Preconditions: complete the [baseline](README.md); retain its environment variables. Use disposable paths with one writer. Both cases use `log-cli`. Run:

```sh
python3 - <<'CHECK'
import json, os, subprocess
from pathlib import Path
repo = Path(os.environ['CHESTACK_VERIFY_REPO'])
run = Path(os.environ['CHESTACK_VERIFY_RUN'])
for case, code in [('log-append', 0), ('log-corrupt', 2)]:
    path = run / 'state' / (case + '.jsonl')
    if code:
        path.write_text('not-json\n')
    before = path.read_bytes() if path.exists() else b''
    argv = ['python3', str(repo / 'skills/chestack/scripts/chestack.py'), 'log',
        '--path', str(path), '--decision', 'Use disposable data', '--reason', 'Isolate verification',
        '--evidence', 'Local fixture', '--result', 'Recorded']
    result = subprocess.run(argv, capture_output=True, text=True, timeout=10, cwd=repo)
    observed = path.read_text() if path.exists() else None
    (run / 'evidence' / (case + '.json')).write_text(json.dumps(dict(
        entry='log-cli', case=case, argv=argv, exit_code=result.returncode,
        stdout=result.stdout, stderr=result.stderr, file_readback=observed), indent=2))
    assert result.returncode == code
    if code:
        assert 'Invalid JSONL' in json.loads(result.stderr)['error']
        assert path.read_bytes() == before
    else:
        rows = [json.loads(line) for line in observed.splitlines()]
        assert len(rows) == 1
        assert rows[0]['decision'] == 'Use disposable data'
        assert rows[0]['reason'] == 'Isolate verification'
        assert rows[0]['evidence'] == 'Local fixture'
        assert rows[0]['result'] == 'Recorded'
        assert rows[0] == json.loads(result.stdout)
print('Passed: log-append, log-readback, log-corrupt via log-cli')
CHECK
```

The JSON artifacts retain CLI evidence and independent file readback. Follow the index cleanup after the run, including failed attempts; proof files remain outside the removed fixture directory.

## Gotchas

- An existing log must contain JSON objects and end in a newline.
- This utility is single-writer; this sample does not test concurrent append safety.
- A successful stdout response alone is insufficient persistence proof.
