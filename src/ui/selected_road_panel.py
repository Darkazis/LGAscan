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
) -> None:
    """Render a compact summary of the selected mock road."""
    st.header("Selected Road Summary")

    if road is None:
        st.warning("Select a mock road to view a summary.")
        return

    road_name = _display_value(road, "road_name")
    if road_name == NOT_AVAILABLE:
        road_name = "Unnamed road"

    st.subheader(road_name)

    metric_cols = st.columns(4)
    metric_cols[0].metric("Current Category", _display_value(road, "current_category"))
    metric_cols[1].metric("LGA", _display_value(road, "lga"))
    metric_cols[2].metric("Length", _length_value(road))
    metric_cols[3].metric("Road Number", _display_value(road, "road_number"))

    detail_cols = st.columns(2)
    with detail_cols[0]:
        st.markdown(f"**Road ID:** {_display_value(road, 'road_id')}")
        st.markdown(f"**Start Point:** {_display_value(road, 'start_point')}")

    with detail_cols[1]:
        st.markdown(f"**Road Number:** {_display_value(road, 'road_number')}")
        st.markdown(f"**End Point:** {_display_value(road, 'end_point')}")

    if summary:
        st.markdown("#### Mock Screening Summary")
        st.write(summary.get("reason", "No mock summary reason is available."))
        st.caption(
            "Future processed outputs should use the project screening "
            "categories: Review candidate, Current category supported, or "
            "Insufficient evidence."
        )

    with st.expander("View raw selected road mock data"):
        st.json(road)
