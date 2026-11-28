#!/usr/bin/env python3
"""Check local homework prerequisites without model calls or evaluation jobs."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
FOLDERS = {"hw1": "hw1-agent-harness", "hw2": "hw2-agent-evaluation"}


def configured_keys(path: Path) -> set[str]:
    """Return configured variable names without exposing credential values."""
    names: set[str] = set()
    if path.is_file():
        for line in path.read_text().splitlines():
            name, separator, value = line.partition("=")
            value = value.strip().strip("\"'")
            if separator and value and not name.lstrip().startswith("#"):
                names.add(name.strip())
    return names


def check(hw: str) -> bool:
    root = ROOT / FOLDERS[hw]
    failures: list[str] = []
    print(f"\n{hw.upper()}: {root}")

    def report(ok: bool, message: str) -> None:
        print(f"  [{'OK' if ok else 'MISSING'}] {message}")
        if not ok:
            failures.append(message)

    report(shutil.which("uv") is not None, "uv is available")
    python = root / ".venv" / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python")
    if python.is_file():
        packages = ["openai", "pytest", "numpy"] if hw == "hw1" else ["harbor", "matplotlib"]
        code = (
            "import importlib.metadata as m, json, sys; "
            f"print(json.dumps({{p: m.version(p) for p in {packages!r}}})); "
            "assert sys.version_info[:2] == (3, 12), 'Expected Python 3.12'"
        )
        try:
            result = subprocess.run([str(python), "-c", code], cwd=root, capture_output=True, text=True, timeout=20)
            report(result.returncode == 0, "Python 3.12 and required package versions are available")
            if result.returncode == 0:
                print(f"       {result.stdout.strip()}")
        except (OSError, subprocess.TimeoutExpired):
            report(False, "Python environment check could not finish")
    else:
        report(False, "Create .venv with: uv sync --locked --python 3.12")

    keys = configured_keys(root / ".env")
    accepted = {"OPENROUTER_API_KEY"} if hw == "hw1" else {"OPENROUTER_API_KEY", "GEMINI_API_KEY"}
    report(bool(keys & accepted), "Local API key is configured (presence only; no provider call)")

    if hw == "hw1":
        source = json.loads((root / "data/source.json").read_text())
        emails = root / "data/emails/emails.jsonl"
        count = 0
        if emails.is_file():
            with emails.open("rb") as handle:
                count = sum(1 for _ in handle)
        report(count == source["emails"], f"Email data contains {count:,} of {source['emails']:,} expected records")
    else:
        if shutil.which("docker"):
            try:
                result = subprocess.run(
                    ["docker", "info", "--format", "{{.ServerVersion}} {{.Architecture}}"],
                    capture_output=True, text=True, timeout=15,
                )
                report(result.returncode == 0, "Docker server is reachable; start Docker Desktop if unavailable")
                if result.returncode == 0:
                    print(f"       Docker {result.stdout.strip()}")
            except (OSError, subprocess.TimeoutExpired):
                report(False, "Docker status check could not finish")
        else:
            report(False, "Docker CLI is installed")

    if not failures:
        print("  Local prerequisites passed. Homework implementations and live evaluations are not checked.")
    return not failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("homework", choices=["hw1", "hw2", "all"], nargs="?", default="all")
    args = parser.parse_args()
    selected = list(FOLDERS) if args.homework == "all" else [args.homework]
    results = [check(hw) for hw in selected]
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
