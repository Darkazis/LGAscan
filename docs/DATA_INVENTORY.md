# Data Inventory

This file tracks the datasets expected by the LGAScan prototype.

## Raw Data

Store raw source files in `data/raw/`. Do not commit raw datasets.

Example inventory fields:

- Dataset name
- Source organisation
- Date received
- Spatial coverage
- Key fields
- Known limitations

## Manually Encoded Data

Store small manually prepared inputs in `data/manually_encoded/`.

Example files may include lookup tables, case-study notes, or evidence weighting inputs.

## Processed Data

Store dashboard-ready files in `data/processed/`. Do not commit processed datasets.

Expected starter outputs:

- `lga_summary.json`
- `road_results.csv`
- `road_network.geojson`
- `evidence_records.json`
- `data_gap_summary.csv`
