"""Validate dashboard-ready LGAScan output files."""

from __future__ import annotations

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"

EXPECTED_OUTPUTS = (
    "lga_summary.json",
    "road_results.csv",
    "road_network.geojson",
    "evidence_records.json",
    "data_gap_summary.csv",
)

RESULT_CATEGORIES = {
    "Review candidate",
    "Current category supported",
    "Insufficient evidence",
}


def validate_outputs(processed_dir: Path = PROCESSED_DATA_DIR) -> list[str]:
    """Return a list of missing expected processed output files."""
    return [
        file_name
        for file_name in EXPECTED_OUTPUTS
        if not (processed_dir / file_name).exists()
    ]


def main() -> None:
    """Print a short validation summary for local processed outputs."""
    missing_files = validate_outputs()
    if missing_files:
        print("Missing processed files:")
        for file_name in missing_files:
            print(f"- {file_name}")
        return

    print("All expected processed files are present.")


if __name__ == "__main__":
    main()
