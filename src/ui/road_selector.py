"""Road selection controls for the LGAScan prototype."""

from __future__ import annotations

from typing import Any

import streamlit as st


ALL_OPTION = "All"
NOT_AVAILABLE = "Not available"


RoadSelectionState = dict[str, Any]


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


def _split_lga_values(road: dict[str, Any]) -> list[str]:
    """Return individual LGA names from a road's LGA field."""
    lga_value = _field_value(road, "lga")
    if lga_value == NOT_AVAILABLE:
        return [NOT_AVAILABLE]
    return [lga.strip() for lga in lga_value.split(",") if lga.strip()]


def _lga_filter_options(roads: list[dict[str, Any]]) -> list[str]:
    """Return sidebar LGA options with multi-LGA roads split into councils."""
    values = sorted(
        {
            lga
            for road in roads
            for lga in _split_lga_values(road)
        }
    )
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


def _apply_lga_filter(
    roads: list[dict[str, Any]],
    selected_lga: str,
) -> list[dict[str, Any]]:
    """Filter roads by membership in an individual LGA."""
    if selected_lga == ALL_OPTION:
        return roads
    return [
        road
        for road in roads
        if selected_lga in _split_lga_values(road)
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
) -> RoadSelectionState:
    """Render sidebar road controls and return road selection state."""
    st.sidebar.header("Road Selection")

    if not roads:
        st.sidebar.warning("No mock roads are available.")
        return {
            "selected_road": None,
            "filtered_roads": [],
            "lga_scoped_roads": [],
            "selected_lga": ALL_OPTION,
            "selected_category": ALL_OPTION,
            "road_selection_changed": False,
        }

    filtered_roads = roads
    lga_scoped_roads = roads
    selected_lga = ALL_OPTION
    selected_category = ALL_OPTION

    if _has_field(roads, "lga"):
        selected_lga = st.sidebar.selectbox(
            "Filter by LGA",
            options=_lga_filter_options(roads),
        )
        filtered_roads = _apply_lga_filter(filtered_roads, selected_lga)
        lga_scoped_roads = filtered_roads

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

    filter_signature = (selected_lga, selected_category)
    previous_filter_signature = st.session_state.get("previous_filter_signature")
    filters_changed = (
        previous_filter_signature is not None
        and previous_filter_signature != filter_signature
    )
    st.session_state["previous_filter_signature"] = filter_signature

    st.sidebar.caption(
        f"{len(filtered_roads)} of {len(roads)} mock roads match the filters."
    )

    if not filtered_roads:
        st.sidebar.warning("No mock roads match the selected filters.")
        return {
            "selected_road": None,
            "filtered_roads": filtered_roads,
            "lga_scoped_roads": lga_scoped_roads,
            "selected_lga": selected_lga,
            "selected_category": selected_category,
            "road_selection_changed": False,
        }

    road_options = _road_options(filtered_roads)
    labels = [label for label, _road in road_options]
    roads_by_label = {label: road for label, road in road_options}
    default_index = 0
    if default_road in filtered_roads:
        default_index = filtered_roads.index(default_road)
    default_label = labels[default_index]

    if st.session_state.get("selected_road_label") not in labels:
        st.session_state["selected_road_label"] = default_label
        st.session_state["previous_road_selector_label"] = default_label

    selected_option = st.sidebar.selectbox(
        "Select a mock road",
        options=labels,
        key="selected_road_label",
    )
    selected_road = roads_by_label[selected_option]
    previous_option = st.session_state.get("previous_road_selector_label")
    road_selection_changed = (
        previous_option is not None and previous_option != selected_option
    )
    if filters_changed:
        road_selection_changed = False
    st.session_state["previous_road_selector_label"] = selected_option

    st.sidebar.caption("Selection is driven by src/mockdata/sample_data.py.")
    return {
        "selected_road": selected_road,
        "filtered_roads": filtered_roads,
        "lga_scoped_roads": lga_scoped_roads,
        "selected_lga": selected_lga,
        "selected_category": selected_category,
        "road_selection_changed": road_selection_changed,
    }
