#!/usr/bin/env python3
"""
Run the demo validation set for the AIPA MCP governance research overlay.

This script reads examples/aipa-governance/validation-manifest.json and
runs validate_governance_blocks.py against the listed artifacts.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
MANIFEST_PATH = REPO_ROOT / "examples" / "aipa-governance" / "validation-manifest.json"
VALIDATOR_PATH = REPO_ROOT / "validator" / "aipa-governance" / "validate_governance_blocks.py"


def load_manifest() -> dict:
    with MANIFEST_PATH.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    manifest = load_manifest()
    artifacts = manifest.get("artifacts", [])

    if not artifacts:
        print(f"FAIL: no artifacts listed in {MANIFEST_PATH}")
        return 1

    paths = [str(REPO_ROOT / artifact["path"]) for artifact in artifacts]

    command = [sys.executable, str(VALIDATOR_PATH), *paths]
    print("Running AIPA governance demo validation...")
    print(" ".join(command))
    print()

    result = subprocess.run(command, check=False)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
