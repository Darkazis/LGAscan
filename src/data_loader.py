"""Load dashboard-ready LGAScan data files."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"


def load_lga_summary(processed_dir: Path = PROCESSED_DATA_DIR) -> dict[str, Any]:
    """Load high-level LGA summary details."""
    path = processed_dir / "lga_summary.json"
    if not path.exists():
        return {
            "lga_name": "Example LGA",
            "notes": "Add data/processed/lga_summary.json to populate this section.",
        }

    with path.open("r", encoding="utf-8") as summary_file:
        return json.load(summary_file)


def load_road_results(processed_dir: Path = PROCESSED_DATA_DIR) -> pd.DataFrame:
    """Load road-level screening results."""
    path = processed_dir / "road_results.csv"
    if not path.exists():
        return pd.DataFrame(
            columns=[
                "road_id",
                "road_name",
                "current_category",
                "screening_result",
                "evidence_score",
            ]
        )

    return pd.read_csv(path)


def load_evidence_records(processed_dir: Path = PROCESSED_DATA_DIR) -> list[dict[str, Any]]:
    """Load road evidence records for the evidence panel."""
    path = processed_dir / "evidence_records.json"
    if not path.exists():
        return []

    with path.open("r", encoding="utf-8") as evidence_file:
        records = json.load(evidence_file)

    if isinstance(records, list):
        return records
    return []


def load_data_gap_summary(processed_dir: Path = PROCESSED_DATA_DIR) -> pd.DataFrame:
    """Load prepared data gap summary rows."""
    path = processed_dir / "data_gap_summary.csv"
    if not path.exists():
        return pd.DataFrame(columns=["dataset", "gap_type", "notes"])

    return pd.read_csv(path)
