"""Criteria results page for LGAScan."""

import streamlit as st

from components.result_display import display_results
from engine.criteria_engine import evaluate_road
from engine.summary_verdict import create_summary_verdict
from mockdata.sample_data import (
    SAMPLE_ROADS,
    SAMPLE_SELECTED_ROAD,
    SAMPLE_SUPPORTING_DATA,
)
from ui.road_selector import render_road_selector


def filter_criteria_results(criteria_results, criteria_scope):
    """Return results matching the selected criteria scope."""
    prefixes = {
        "State": "S-",
        "Regional": "R-",
    }
    prefix = prefixes.get(criteria_scope)

    if prefix is None:
        return criteria_results

    return [
        result
        for result in criteria_results
        if result["criteria_id"].startswith(prefix)
    ]


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
        f"{float(length_km):.2f} km"
        if isinstance(length_km, (int, float))
        else "Not available"
    )

    with st.container(border=True):
        st.caption("SELECTED ROAD")
        st.subheader(road_name)

        road_details = st.columns(4)
        road_details[0].metric("Road number", road_number)
        road_details[1].metric("Current category", current_category)
        road_details[2].metric("LGA", lga)
        road_details[3].metric("Segment length", length_label)

    st.markdown("### Assessment scope")
    st.caption("Choose which criteria set to apply to the selected road.")
    criteria_scope = st.segmented_control(
        "Criteria set",
        options=["All", "State", "Regional"],
        default="All",
        selection_mode="single",
        label_visibility="collapsed",
        help=(
            "State includes S- criteria, Regional includes R- criteria, and "
            "All includes every registered criterion."
        ),
    ) or "All"

    selected_results = filter_criteria_results(criteria_results, criteria_scope)
    summary_verdict = create_summary_verdict(selected_results)

    st.divider()
    display_results(
        selected_results,
        summary_verdict,
    )


if __name__ == "__main__":
    main()
