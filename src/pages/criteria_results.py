"""Criteria results page for LGAScan."""

import streamlit as st

from mockdata.sample_data import SAMPLE_SELECTED_ROAD, SAMPLE_SUPPORTING_DATA, SAMPLE_ROADS
from ui.road_selector import render_road_selector
from ui.selected_road_panel import render_selected_road_summary

from engine.criteria_engine import evaluate_road
from engine.summary_verdict import create_summary_verdict
from components.result_display import display_results


def main():
    st.title("Criteria Results")

    selected_road = render_road_selector(SAMPLE_ROADS)

    if selected_road is None:
        st.info("Select a road to view criteria results.")
        return

    criteria_results = evaluate_road(
        selected_road,
        SAMPLE_SUPPORTING_DATA,
    )

    summary_verdict = create_summary_verdict(criteria_results)

    display_results(
        criteria_results,
        summary_verdict,
    )


if __name__ == "__main__":
    main()