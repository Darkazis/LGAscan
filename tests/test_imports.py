"""Import checks for the starter LGAScan modules."""

from __future__ import annotations

import importlib
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
SCRIPTS_DIR = PROJECT_ROOT / "scripts"

for module_dir in (SRC_DIR, SCRIPTS_DIR):
    sys.path.insert(0, str(module_dir))


def test_dashboard_modules_import() -> None:
    """Core dashboard modules should be importable."""
    for module_name in (
        "app",
        "data_loader",
        "map_view",
        "evidence_panel",
        "export_tools",
    ):
        importlib.import_module(module_name)


def test_script_modules_import() -> None:
    """Offline script modules should be importable."""
    for module_name in (
        "build_lga_scan_results",
        "validate_lga_scan_outputs",
    ):
        importlib.import_module(module_name)
