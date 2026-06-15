"""Tests for dashboard data loading helpers."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from src.data_loader import (
    load_data_gap_summary,
    load_evidence_records,
    load_lga_summary,
    load_road_results,
)


def test_loaders_return_empty_defaults_for_missing_files(tmp_path: Path) -> None:
    """Missing prototype files should return useful empty defaults."""
    summary = load_lga_summary(tmp_path)
    road_results = load_road_results(tmp_path)
    evidence_records = load_evidence_records(tmp_path)
    data_gap_summary = load_data_gap_summary(tmp_path)

    assert summary["lga_name"] == "Example LGA"
    assert road_results.empty
    assert evidence_records == []
    assert data_gap_summary.empty


def test_loaders_read_processed_files(tmp_path: Path) -> None:
    """Loaders should read small dashboard-ready files."""
    (tmp_path / "lga_summary.json").write_text(
        json.dumps({"lga_name": "Sample LGA"}),
        encoding="utf-8",
    )
    pd.DataFrame(
        [
            {
                "road_id": "R001",
                "road_name": "Sample Road",
                "current_category": "Local",
                "screening_result": "Review candidate",
                "evidence_score": 3,
            }
        ]
    ).to_csv(tmp_path / "road_results.csv", index=False)
    (tmp_path / "evidence_records.json").write_text(
        json.dumps([{"road_id": "R001", "source": "sample"}]),
        encoding="utf-8",
    )
    pd.DataFrame(
        [{"dataset": "traffic", "gap_type": "missing count", "notes": "sample"}]
    ).to_csv(tmp_path / "data_gap_summary.csv", index=False)

    assert load_lga_summary(tmp_path)["lga_name"] == "Sample LGA"
    assert len(load_road_results(tmp_path)) == 1
    assert load_evidence_records(tmp_path)[0]["road_id"] == "R001"
    assert len(load_data_gap_summary(tmp_path)) == 1
