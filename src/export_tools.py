"""Export helpers for LGAScan."""

from __future__ import annotations

import pandas as pd


def render_export_tools(
    road_results: pd.DataFrame,
    data_gap_summary: pd.DataFrame,
) -> None:
    """Render starter export controls for processed dashboard tables."""
    import streamlit as st

    if road_results.empty and data_gap_summary.empty:
        st.info("No processed tables are available for export yet.")
        return

    if not road_results.empty:
        st.download_button(
            label="Download road ranking CSV",
            data=road_results.to_csv(index=False),
            file_name="lga_scan_road_ranking.csv",
            mime="text/csv",
        )

    if not data_gap_summary.empty:
        st.download_button(
            label="Download data gap summary CSV",
            data=data_gap_summary.to_csv(index=False),
            file_name="lga_scan_data_gaps.csv",
            mime="text/csv",
        )
