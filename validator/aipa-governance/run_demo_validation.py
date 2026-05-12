#!/usr/bin/env python3
"""
Run the demo validation set for the AIPA MCP governance research overlay.

This script reads examples/aipa-governance/validation-manifest.json and runs
validate_governance_blocks.py against every listed artifact and scenario folder.

The validator checks structural correctness. The manifest records expected
governance outcomes such as PASS, FAIL, and UNSUPPORTED. A structurally valid
FAIL or UNSUPPORTED scenario should not break CI when that outcome is expected.
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


def collect_paths(manifest: dict) -> list[str]:
    paths: list[str] = []

    for artifact in manifest.get("artifacts", []):
        paths.append(str(REPO_ROOT / artifact["path"]))

    for scenario in manifest.get("scenario_folders", []):
        paths.append(str(REPO_ROOT / scenario["path"]))

    return paths


def print_expected_outcomes(manifest: dict) -> None:
    print("Expected governance outcomes from manifest:")

    for artifact in manifest.get("artifacts", []):
        print(
            f"  - {artifact['path']}: "
            f"structural={artifact.get('expected_structural_status', 'PASS')} "
            f"governance={artifact.get('expected_governance_outcome', 'PASS')}"
        )

    for scenario in manifest.get("scenario_folders", []):
        print(
            f"  - {scenario['path']}: "
            f"structural={scenario.get('expected_structural_status', 'PASS')} "
            f"governance={scenario.get('expected_governance_outcome', 'PASS')}"
        )

    print()


def main() -> int:
    manifest = load_manifest()
    paths = collect_paths(manifest)

    if not paths:
        print(f"FAIL: no artifacts or scenarios listed in {MANIFEST_PATH}")
        return 1

    print_expected_outcomes(manifest)

    command = [sys.executable, str(VALIDATOR_PATH), *paths]
    print("Running AIPA governance structural validation...")
    print(" ".join(command))
    print()

    result = subprocess.run(command, check=False)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
