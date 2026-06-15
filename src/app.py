"""Starter Streamlit dashboard for LGAScan."""

from data_loader import (
    load_data_gap_summary,
    load_evidence_records,
    load_lga_summary,
    load_road_results,
)
from evidence_panel import render_evidence_panel
from export_tools import render_export_tools
from map_view import render_road_map


def main() -> None:
    """Render the LGAScan prototype dashboard."""
    import streamlit as st

    st.set_page_config(page_title="LGAScan", layout="wide")

    st.title("LGAScan")
    st.caption("LGA-wide road category review readiness screening")

    lga_summary = load_lga_summary()
    road_results = load_road_results()
    evidence_records = load_evidence_records()
    data_gap_summary = load_data_gap_summary()

    with st.sidebar:
        st.header("Case Study")
        selected_lga = st.selectbox(
            "LGA",
            options=[lga_summary.get("lga_name", "Example LGA")],
        )
        st.write(f"Selected: {selected_lga}")

    st.header("LGA Overview")
    overview_cols = st.columns(3)
    overview_cols[0].metric("Roads reviewed", len(road_results))
    overview_cols[1].metric("Evidence records", len(evidence_records))
    overview_cols[2].metric("Data gap rows", len(data_gap_summary))

    st.header("Interactive Road Map")
    render_road_map(road_results)

    st.header("Road Ranking Table")
    if road_results.empty:
        st.info("No processed road ranking data found yet.")
    else:
        st.dataframe(road_results, use_container_width=True)

    st.header("Road Evidence Panel")
    render_evidence_panel(evidence_records)

    st.header("Data Gap Summary")
    if data_gap_summary.empty:
        st.info("No data gap summary found yet.")
    else:
        st.dataframe(data_gap_summary, use_container_width=True)

    st.header("Export Tools")
    render_export_tools(road_results, data_gap_summary)


if __name__ == "__main__":
    main()
