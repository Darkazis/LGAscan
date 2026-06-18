"""Criteria results page for LGAScan."""

import streamlit as st

from mockdata.sample_data import SAMPLE_SELECTED_ROAD, SAMPLE_SUPPORTING_DATA
from engine.criteria_engine import evaluate_road
from engine.summary_verdict import create_summary_verdict
from components.result_display import display_results


def main() -> None:
    st.title("Criteria Results")
    st.caption("Mock criteria evaluation output for the selected road")

    st.subheader("Selected Road")
    st.write(SAMPLE_SELECTED_ROAD["road_name"])
    st.json(SAMPLE_SELECTED_ROAD)

    criteria_results = evaluate_road(
        SAMPLE_SELECTED_ROAD,
        SAMPLE_SUPPORTING_DATA,
    )

    summary_verdict = create_summary_verdict(criteria_results)

    display_results(criteria_results, summary_verdict)


if __name__ == "__main__":
    main()