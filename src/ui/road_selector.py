"""Road selection controls for the LGAScan prototype."""

from __future__ import annotations

from typing import Any

import streamlit as st


ALL_OPTION = "All"
NOT_AVAILABLE = "Not available"


def _field_value(road: dict[str, Any], field_name: str) -> str:
    """Return a safe display value for a road field."""
    value = road.get(field_name)
    if value is None or value == "":
        return NOT_AVAILABLE
    return str(value)


def _has_field(roads: list[dict[str, Any]], field_name: str) -> bool:
    """Return whether at least one road record contains a field."""
    return any(field_name in road for road in roads)


def _filter_options(roads: list[dict[str, Any]], field_name: str) -> list[str]:
    """Return sidebar filter options for a road field."""
    values = sorted({_field_value(road, field_name) for road in roads})
    return [ALL_OPTION] + values


def _apply_filter(
    roads: list[dict[str, Any]],
    field_name: str,
    selected_value: str,
) -> list[dict[str, Any]]:
    """Filter roads by a selected field value."""
    if selected_value == ALL_OPTION:
        return roads
    return [
        road
        for road in roads
        if _field_value(road, field_name) == selected_value
    ]


def format_road_option(road: dict[str, Any]) -> str:
    """Return a readable label for a road selection option."""
    road_name = _field_value(road, "road_name")
    if road_name == NOT_AVAILABLE:
        road_name = "Unnamed road"

    road_number = _field_value(road, "road_number")
    lga = _field_value(road, "lga")
    current_category = _field_value(road, "current_category")
    road_id = _field_value(road, "road_id")

    return (
        f"{road_name} ({road_number}) - {lga} - "
        f"{current_category} - {road_id}"
    )


def _road_options(roads: list[dict[str, Any]]) -> list[tuple[str, dict[str, Any]]]:
    """Return unique labels paired with their road dictionaries."""
    label_counts: dict[str, int] = {}
    options = []

    for road in roads:
        base_label = format_road_option(road)
        label_counts[base_label] = label_counts.get(base_label, 0) + 1
        label = base_label

        if label_counts[base_label] > 1:
            label = f"{base_label} #{label_counts[base_label]}"

        options.append((label, road))

    return options


def render_road_selector(
    roads: list[dict[str, Any]],
    default_road: dict[str, Any] | None = None,
) -> dict[str, Any] | None:
    """Render sidebar road controls and return the selected road."""
    st.sidebar.header("Road Selection")

    if not roads:
        st.sidebar.warning("No mock roads are available.")
        return None

    filtered_roads = roads

    if _has_field(roads, "lga"):
        selected_lga = st.sidebar.selectbox(
            "Filter by LGA",
            options=_filter_options(roads, "lga"),
        )
        filtered_roads = _apply_filter(filtered_roads, "lga", selected_lga)

    if _has_field(roads, "current_category"):
        selected_category = st.sidebar.selectbox(
            "Filter by current category",
            options=_filter_options(filtered_roads, "current_category"),
        )
        filtered_roads = _apply_filter(
            filtered_roads,
            "current_category",
            selected_category,
        )

    st.sidebar.caption(
        f"{len(filtered_roads)} of {len(roads)} mock roads match the filters."
    )

    if not filtered_roads:
        st.sidebar.warning("No mock roads match the selected filters.")
        return None

    road_options = _road_options(filtered_roads)
    default_index = 0
    if default_road in filtered_roads:
        default_index = filtered_roads.index(default_road)

    selected_option = st.sidebar.selectbox(
        "Select a mock road",
        options=road_options,
        index=default_index,
        format_func=lambda option: option[0],
    )

    st.sidebar.caption("Selection is driven by src/mockdata/sample_data.py.")
    return selected_option[1]
