"""Criteria results page for LGAScan."""

import streamlit as st

from components.result_display import display_results
from engine.criteria_engine import evaluate_road
from mockdata.sample_data import (
    SAMPLE_ROADS,
    SAMPLE_SELECTED_ROAD,
    SAMPLE_SUPPORTING_DATA,
)
from ui.road_selector import render_road_selector


def main():
    st.title("Criteria assessment")
    st.caption(
        "Review a selected road against the State and Regional "
        "recategorisation criteria."
    )

    selection_state = render_road_selector(SAMPLE_ROADS, SAMPLE_SELECTED_ROAD)
    selected_road = selection_state["selected_road"]

    if selected_road is None:
        st.info("Select a road to view criteria results.")
        return

    criteria_results = evaluate_road(
        selected_road,
        SAMPLE_SUPPORTING_DATA,
    )

    road_name = selected_road.get("road_name") or "Unnamed road"
    road_number = selected_road.get("road_number") or "Not available"
    current_category = selected_road.get("current_category") or "Not available"
    lga = selected_road.get("lga") or "Not available"
    length_km = selected_road.get("length_km")
    length_label = (
        f"{float(length_km):.1f} km"
        if isinstance(length_km, (int, float))
        else "Not available"
    )

    with st.container(border=True):
        st.subheader(road_name)

        road_details = st.columns(3)
        road_details[0].metric("Road number", road_number)
        road_details[1].metric("Current category", current_category)
        road_details[2].metric("Segment length", length_label)

        st.markdown("**LGAs**")
        st.write(lga)

    default_scope = (
        current_category
        if current_category in {"State", "Regional"}
        else "All"
    )
    display_results(
        criteria_results,
        default_scope=default_scope,
        road_id=selected_road.get("road_id", "selected-road"),
    )


if __name__ == "__main__":
    main()
