"""Main Streamlit entry point for the LGAScan prototype."""

from mockdata.sample_data import (
    SAMPLE_CRITERIA_RESULTS,
    SAMPLE_ROADS,
    SAMPLE_SELECTED_ROAD,
    get_sample_criteria_results_by_road_id,
    get_sample_summary_result_by_road_id,
)
from ui.app_shell import configure_page, render_dashboard_header, render_placeholder_section
from ui.road_selector import render_road_selector
from ui.selected_road_panel import render_selected_road_summary


def main() -> None:
    """Render the LGAScan prototype dashboard."""
    import streamlit as st

    configure_page()
    render_dashboard_header()

    selected_road = render_road_selector(SAMPLE_ROADS, SAMPLE_SELECTED_ROAD)
    selected_road_id = selected_road["road_id"] if selected_road else None
    selected_summary = (
        get_sample_summary_result_by_road_id(selected_road_id)
        if selected_road_id
        else None
    )
    selected_criteria = (
        get_sample_criteria_results_by_road_id(selected_road_id)
        if selected_road_id
        else []
    )

    st.header("LGA Overview")
    overview_cols = st.columns(3)
    overview_cols[0].metric("Mock roads", len(SAMPLE_ROADS))
    overview_cols[1].metric("Mock criteria rows", len(SAMPLE_CRITERIA_RESULTS))
    overview_cols[2].metric("Selected road criteria", len(selected_criteria))
    st.divider()

    render_selected_road_summary(selected_road, selected_summary)

    render_placeholder_section(
        "Interactive Road Map",
        "Map logic is not implemented yet. This section will later display "
        "prepared GeoJSON for the selected road.",
    )

    st.header("Criteria Results")
    if selected_criteria:
        st.dataframe(selected_criteria, use_container_width=True)
    else:
        st.info("No mock criteria rows are available for the selected road.")

    render_placeholder_section(
        "Screening Summary",
        "Summary display is using mock data only. No criteria scoring is "
        "implemented in the dashboard.",
    )

    render_placeholder_section(
        "Data Gaps And Manual Review",
        "Data gap and manual review details will be connected once processed "
        "outputs are available.",
    )


if __name__ == "__main__":
    main()
