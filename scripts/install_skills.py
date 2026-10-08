#!/usr/bin/env python3
"""Copy the complete skill bundle into an explicit local discovery directory."""

import argparse
import json
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def install(destination):
    destination = Path(destination).expanduser().resolve()
    source = ROOT / "skills"
    if destination.is_relative_to(source.resolve()):
        raise ValueError("Destination must be outside the source skills directory")
    names = json.loads((ROOT / "catalog.json").read_text())["skills"]
    # Check all conflicts before writing, preserving partial existing installations.
    conflicts = [str(destination / name) for name in names
                 if (destination / name).exists() or (destination / name).is_symlink()]
    if conflicts:
        raise ValueError("Existing skills preserved; choose another destination: " + ", ".join(conflicts))
    destination.mkdir(parents=True, exist_ok=True)
    installed = []
    with tempfile.TemporaryDirectory(prefix=".chestack-stage-", dir=destination) as stage:
        for name in names:
            shutil.copytree(source / name, Path(stage) / name,
                            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        try:
            for name in names:
                # mkdir fails on a late collision rather than replacing someone else's data.
                target = destination / name
                target.mkdir()
                installed.append(target)
                shutil.copytree(Path(stage) / name, target, dirs_exist_ok=True)
        except Exception:
            for target in installed:
                shutil.rmtree(target)
            raise
    return [str(path) for path in installed]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dest", type=Path, required=True,
                        help="Explicit .agents/skills directory; no global default")
    args = parser.parse_args()
    try:
        print(json.dumps({"installed": install(args.dest)}, indent=2))
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
