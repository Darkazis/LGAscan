# Architecture

LGAScan uses a staged architecture:

```text
Raw datasets -> processing scripts -> processed outputs -> Streamlit dashboard
```

## Raw Datasets

Raw source datasets live under `data/raw/`. These files are local-only and ignored by git because they may be large, licensed, or sensitive.

## Processing Scripts

Offline processing belongs in `scripts/`. These scripts should prepare small dashboard-ready CSV, GeoJSON, and JSON outputs before the Streamlit app is opened.

## Processed Outputs

Dashboard-ready files live under `data/processed/`. The app reads these files directly and should stay focused on display, filtering, ranking, and exports.

## Streamlit Dashboard

The Streamlit app lives in `src/`. It provides:

- LGA Overview
- Interactive Road Map
- Road Ranking Table
- Road Evidence Panel
- Data Gap Summary
- Export Tools

The dashboard is a screening aid for early review. It does not replace engineering judgement, policy review, or source-data verification.
