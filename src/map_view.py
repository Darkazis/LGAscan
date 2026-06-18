"""Map display helpers for LGAScan."""

from __future__ import annotations

import pandas as pd
import leafmap.foliumap as leafmap


def render_road_map(road_results: pd.DataFrame) -> None:
    """Render a lightweight placeholder map section."""
    import streamlit as st
    
    st.info("Look at Map page for interactive map prototype.")
