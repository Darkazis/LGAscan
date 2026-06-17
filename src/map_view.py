"""Map display helpers for LGAScan."""

from __future__ import annotations

import pandas as pd
import leafmap.foliumap as leafmap


def render_road_map(road_results: pd.DataFrame) -> None:
    """Render a lightweight placeholder map section."""
    import streamlit as st
    
    m = leafmap.Map(center=(-32.0, 147.0), zoom=6)
    
    m.to_streamlit(height=500, width=None)

    if road_results.empty:
        return

    st.write("Map rendering will use dashboard-ready GeoJSON in a later prototype step.")
