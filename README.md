# LGAScan

LGAScan is a showcase-style Streamlit dashboard for LGA-wide road category review readiness screening. It helps explore road segments across a selected case-study LGA using prepared CSV, GeoJSON, and JSON outputs.

The project exists to make early review work easier to inspect and explain. Heavy GIS and source-data preparation are expected to happen before the dashboard is opened, so the app can stay fast, simple, and suitable for a short prototype.

## Architecture

LGAScan follows a simple staged flow:

```text
Raw datasets -> processing scripts -> processed outputs -> Streamlit dashboard
```

- `data/raw/` stores source datasets locally and is ignored by git.
- `data/manually_encoded/` stores small manually prepared inputs, notes, or lookup tables.
- `scripts/` contains processing and validation entry points.
- `data/processed/` stores dashboard-ready CSV, GeoJSON, and JSON files and is ignored by git.
- `src/` contains the Streamlit dashboard and display helpers.
- `outputs/` stores generated exports and is ignored by git.

The dashboard reads prepared files only. It should not run heavy GIS processing during normal use.

## Result Categories

LGAScan uses only these screening result categories:

- Review candidate
- Current category supported
- Insufficient evidence

## Install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run The Dashboard

```bash
streamlit run src/app.py
```

## Processed Files

The starter dashboard looks for files in `data/processed/`. The prototype currently expects small dashboard-ready artifacts such as:

- `lga_summary.json`
- `road_results.csv`
- `road_network.geojson`
- `evidence_records.json`
- `data_gap_summary.csv`

If these files are missing, the app shows empty placeholder sections so the dashboard can still be opened during early development.
