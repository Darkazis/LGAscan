"""Build dashboard-ready LGAScan outputs from prepared local inputs."""

from __future__ import annotations

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
MANUAL_DATA_DIR = PROJECT_ROOT / "data" / "manually_encoded"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"

RESULT_CATEGORIES = (
    "Review candidate",
    "Current category supported",
    "Insufficient evidence",
)


def build_lga_scan_results(
    raw_dir: Path = RAW_DATA_DIR,
    manual_dir: Path = MANUAL_DATA_DIR,
    processed_dir: Path = PROCESSED_DATA_DIR,
) -> None:
    """Placeholder entry point for future offline processing."""
    processed_dir.mkdir(parents=True, exist_ok=True)
    print("LGAScan offline processing placeholder")
    print(f"Raw data directory: {raw_dir}")
    print(f"Manual data directory: {manual_dir}")
    print(f"Processed output directory: {processed_dir}")
    print("Add source-specific processing here as the prototype matures.")


if __name__ == "__main__":
    build_lga_scan_results()
