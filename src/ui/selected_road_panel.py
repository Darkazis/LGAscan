"""Selected road display helpers for the LGAScan prototype."""

from __future__ import annotations

from typing import Any

import streamlit as st


NOT_AVAILABLE = "Not available"


def _display_value(road: dict[str, Any], field_name: str) -> str:
    """Return a safe display value for selected road fields."""
    value = road.get(field_name)
    if value is None or value == "":
        return NOT_AVAILABLE
    return str(value)


def _length_value(road: dict[str, Any]) -> str:
    """Return a formatted road length value when available."""
    value = road.get("length_km")
    if value is None or value == "":
        return NOT_AVAILABLE

    try:
        return f"{float(value):.3f} km"
    except (TypeError, ValueError):
        return str(value)


def render_selected_road_summary(
    road: dict[str, Any] | None,
    summary: dict[str, Any] | None = None,
    screening_category: str = "Insufficient evidence",
) -> None:
    """Render a compact summary of the selected mock road."""
    st.markdown('<div id="road-evidence-panel"></div>', unsafe_allow_html=True)
    st.markdown("#### Road Evidence Panel")

    if road is None:
        st.warning("Select a mock road to view a summary.")
        return

    road_name = _display_value(road, "road_name")
    if road_name == NOT_AVAILABLE:
        road_name = "Unnamed road"

    st.markdown(f"**{road_name}**")
    st.markdown(f'<span class="lga-status-pill">{screening_category}</span>', unsafe_allow_html=True)

    metric_cols = st.columns(2)
    metric_cols[0].metric("Current Category", _display_value(road, "current_category"))
    metric_cols[1].metric("LGA", _display_value(road, "lga"))
    metric_cols = st.columns(2)
    metric_cols[0].metric("Length", _length_value(road))
    metric_cols[1].metric("Segments", _display_value(road, "segment_count"))

    st.markdown(f"**Road ID:** {_display_value(road, 'road_id')}")
    st.markdown(f"**Road Number:** {_display_value(road, 'road_number')}")
    st.markdown(f"**Start Point:** {_display_value(road, 'start_point')}")
    st.markdown(f"**End Point:** {_display_value(road, 'end_point')}")

    if summary:
        st.markdown("**Summary**")
        st.write(summary.get("reason", "No mock summary reason is available."))
        st.caption(
            "Future processed outputs should use the project screening "
            "categories: Review candidate, Current category supported, or "
            "Insufficient evidence."
        )

    with st.expander("View raw selected road mock data"):
        st.json(road)
