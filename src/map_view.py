"""Map display helpers for LGAScan."""

from __future__ import annotations

import pandas as pd


def render_road_map(road_results: pd.DataFrame) -> None:
    """Render a lightweight placeholder map section."""
    import streamlit as st

    if road_results.empty:
        st.info("No processed road geometry found yet.")
        return

    st.write("Map rendering will use dashboard-ready GeoJSON in a later prototype step.")
