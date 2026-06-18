"""Main Streamlit entry point for the LGAScan prototype."""

from __future__ import annotations

from html import escape
from urllib.parse import quote

from mockdata.sample_data import (
    SAMPLE_CRITERIA_RESULTS,
    SAMPLE_ROADS,
    SAMPLE_SELECTED_ROAD,
    SAMPLE_SUMMARY_RESULTS,
    get_sample_criteria_results_by_road_id,
    get_sample_summary_result_by_road_id,
)
from ui.app_shell import (
    configure_page,
    inject_dashboard_styles,
    render_dashboard_header,
    render_kpi_card,
    render_placeholder_section,
)
from ui.road_selector import render_road_selector
from ui.selected_road_panel import render_selected_road_summary


SCREENING_REVIEW_CANDIDATE = "Review candidate"
SCREENING_CURRENT_SUPPORTED = "Current category supported"
SCREENING_INSUFFICIENT = "Insufficient evidence"


def _map_url_for_road(road: dict | None) -> str:
    """Return the Map page URL with enough query params to identify a road."""
    if not road:
        return "/Map"

    road_id = quote(str(road.get("road_id", "")), safe="")
    road_number = quote(str(road.get("road_number", "")), safe="")
    road_name = quote(str(road.get("road_name", "")), safe="")
    return (
        f"/Map?road_id={road_id}"
        f"&road_number={road_number}"
        f"&road_name={road_name}"
    )


def _screening_category(summary: dict | None) -> str:
    """Map mock summary wording to project screening categories."""
    if not summary:
        return SCREENING_INSUFFICIENT

    verdict = str(summary.get("summary_verdict", "")).lower()
    if "current category" in verdict:
        return SCREENING_CURRENT_SUPPORTED
    if "potential review" in verdict:
        return SCREENING_REVIEW_CANDIDATE
    return SCREENING_INSUFFICIENT


def _road_summary_lookup() -> dict[str, dict]:
    """Return mock summary rows keyed by road id."""
    return {row["road_id"]: row for row in SAMPLE_SUMMARY_RESULTS}


def _build_road_ranking_rows(roads: list[dict]) -> list[dict[str, object]]:
    """Build a compact mock road table for the dashboard."""
    summaries = _road_summary_lookup()
    rows = []

    for road in roads:
        road_id = road.get("road_id")
        summary = summaries.get(road_id)
        criteria_count = len(get_sample_criteria_results_by_road_id(road_id))
        rows.append(
            {
                "Road Name": road.get("road_name", "Unnamed road"),
                "Road Number": road.get("road_number", "Not available"),
                "LGA": road.get("lga", "Not available"),
                "Current Category": road.get("current_category", "Not available"),
                "Length (km)": road.get("length_km", "Not available"),
                "Segments": road.get("segment_count", "Not available"),
                "Evidence Rows": criteria_count,
                "Screening Category": _screening_category(summary),
                "View In Map": _map_url_for_road(road),
            }
        )

    category_rank = {
        SCREENING_REVIEW_CANDIDATE: 0,
        SCREENING_INSUFFICIENT: 1,
        SCREENING_CURRENT_SUPPORTED: 2,
    }
    rows = sorted(
        rows,
        key=lambda row: (
            category_rank.get(str(row["Screening Category"]), 99),
            -int(row["Evidence Rows"]),
            -float(row["Length (km)"])
            if isinstance(row["Length (km)"], (int, float))
            else 0,
            str(row["Road Name"]),
        ),
    )

    for index, row in enumerate(rows, start=1):
        row["Rank"] = index

    return rows


def _render_data_gap_panel() -> None:
    """Render data gap placeholder content."""
    import streamlit as st

    render_placeholder_section(
        "Data Gaps And Evidence Review",
        "This prototype still uses a small mock road subset. Data gap details "
        "will come from prepared processed outputs once the offline pipeline is connected.",
    )
    st.caption("No real data loading or criteria scoring is running in Streamlit.")


def _render_selected_road_map_action(selected_road: dict | None) -> None:
    """Render a handoff action for the selected road map view."""
    import streamlit as st

    st.markdown("#### Map View Handoff")
    st.write(
        "The homepage does not render a map. Use this handoff to open the "
        "dedicated Map page with the selected road identifiers in the URL."
    )
    st.link_button(
        "View selected road in Map view",
        _map_url_for_road(selected_road),
        disabled=selected_road is None,
    )
    if selected_road:
        st.caption(
            "Map page receives: "
            f"road_id={selected_road.get('road_id')}, "
            f"road_number={selected_road.get('road_number')}, "
            f"road_name={selected_road.get('road_name')}"
        )


def _scroll_to_road_evidence_panel(selected_road_id: str | None) -> None:
    """Smooth-scroll to the Road Evidence Panel after a sidebar selection."""
    import json

    import streamlit.components.v1 as components

    scroll_token = json.dumps(str(selected_road_id or "no-road"))
    components.html(
        f"""
        <script>
        const selectedRoadScrollToken = {scroll_token};
        let attempts = 0;

        const scrollToEvidencePanel = () => {{
            const anchor = window.parent.document.getElementById("road-evidence-panel");
            if (anchor) {{
                anchor.scrollIntoView({{ behavior: "smooth", block: "start" }});
                return;
            }}

            attempts += 1;
            if (attempts < 8) {{
                setTimeout(scrollToEvidencePanel, 100);
            }}
        }};

        setTimeout(scrollToEvidencePanel, 120);
        </script>
        """,
        height=1,
    )


def _display_value(value: object) -> str:
    """Return an escaped display value for ranking table cells."""
    if value is None or value == "":
        return "Not available"
    return escape(str(value))


def _render_road_ranking_table(rows: list[dict[str, object]]) -> None:
    """Render a ranking table with wrapping text and map handoff links."""
    import streamlit as st

    if not rows:
        st.info("No roads are available for the selected LGA scope.")
        return

    table_rows = []
    for row in rows:
        map_url = _display_value(row.get("View In Map"))
        table_rows.append(
            "<tr>"
            f"<td class=\"numeric\">{_display_value(row.get('Rank'))}</td>"
            f"<td class=\"road-name\">{_display_value(row.get('Road Name'))}</td>"
            f"<td class=\"road-number\">{_display_value(row.get('Road Number'))}</td>"
            f"<td class=\"lga-name\">{_display_value(row.get('LGA'))}</td>"
            f"<td class=\"current-category\">{_display_value(row.get('Current Category'))}</td>"
            f"<td class=\"numeric\">{_display_value(row.get('Length (km)'))}</td>"
            f"<td class=\"numeric\">{_display_value(row.get('Segments'))}</td>"
            f"<td class=\"numeric\">{_display_value(row.get('Evidence Rows'))}</td>"
            f"<td class=\"screening\">{_display_value(row.get('Screening Category'))}</td>"
            f"<td class=\"map-link\"><a href=\"{map_url}\">Open map</a></td>"
            "</tr>"
        )

    st.markdown(
        """
        <div class="lga-ranking-wrap">
            <table class="lga-ranking-table">
                <colgroup>
                    <col style="width: 5%;">
                    <col style="width: 18%;">
                    <col style="width: 7%;">
                    <col style="width: 24%;">
                    <col style="width: 9%;">
                    <col style="width: 8%;">
                    <col style="width: 6%;">
                    <col style="width: 7%;">
                    <col style="width: 11%;">
                    <col style="width: 5%;">
                </colgroup>
                <thead>
                    <tr>
                        <th>Rank</th>
                        <th>Road</th>
                        <th>No.</th>
                        <th>LGA</th>
                        <th>Category</th>
                        <th>km</th>
                        <th>Seg.</th>
                        <th>Evid.</th>
                        <th>Screening</th>
                        <th>Map</th>
                    </tr>
                </thead>
                <tbody>
                    {rows}
                </tbody>
            </table>
        </div>
        """.format(rows="\n".join(table_rows)),
        unsafe_allow_html=True,
    )


def main() -> None:
    """Render the LGAScan prototype dashboard."""
    import streamlit as st

    configure_page()
    inject_dashboard_styles()
    render_dashboard_header()

    selection_state = render_road_selector(SAMPLE_ROADS, SAMPLE_SELECTED_ROAD)
    selected_road = selection_state["selected_road"]
    lga_scoped_roads = selection_state["lga_scoped_roads"]
    selected_lga = selection_state["selected_lga"]
    selected_road_id = selected_road["road_id"] if selected_road else None
    should_scroll_to_evidence = (
        selected_road is not None
        and bool(selection_state.get("road_selection_changed"))
    )
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
    road_rows = _build_road_ranking_rows(lga_scoped_roads)
    kpi_rows = road_rows
    selected_category = _screening_category(selected_summary)
    kpi_counts = {
        SCREENING_REVIEW_CANDIDATE: 0,
        SCREENING_CURRENT_SUPPORTED: 0,
        SCREENING_INSUFFICIENT: 0,
    }
    for row in kpi_rows:
        kpi_counts[row["Screening Category"]] += 1

    kpi_cols = st.columns(4)
    with kpi_cols[0]:
        render_kpi_card(
            "Roads scanned",
            len(lga_scoped_roads),
            f"LGA scope: {selected_lga}",
        )
    with kpi_cols[1]:
        render_kpi_card(
            "Review candidates",
            kpi_counts[SCREENING_REVIEW_CANDIDATE],
            "Within selected LGA scope",
        )
    with kpi_cols[2]:
        render_kpi_card(
            "Current category supported",
            kpi_counts[SCREENING_CURRENT_SUPPORTED],
            "Within selected LGA scope",
        )
    with kpi_cols[3]:
        render_kpi_card(
            "Insufficient evidence",
            kpi_counts[SCREENING_INSUFFICIENT],
            "Within selected LGA scope",
        )

    st.markdown("#### Road Ranking Table")
    st.caption(
        "Ranked within the selected LGA scope. Use the Map link on a row to "
        "hand that road to the dedicated Map page."
    )
    _render_road_ranking_table(road_rows)

    st.divider()
    content_col, evidence_col = st.columns([2.2, 1])

    with content_col:
        _render_selected_road_map_action(selected_road)

    with evidence_col:
        render_selected_road_summary(selected_road, selected_summary, selected_category)

    if should_scroll_to_evidence:
        _scroll_to_road_evidence_panel(selected_road_id)

    st.divider()

    criteria_col, gap_col = st.columns([1.35, 1])
    with criteria_col:
        st.markdown("#### Criteria Results")
        if selected_criteria:
            st.dataframe(selected_criteria, width="stretch", hide_index=True)
        else:
            st.info("No mock criteria rows are available for the selected road.")

    with gap_col:
        _render_data_gap_panel()


if __name__ == "__main__":
    main()
