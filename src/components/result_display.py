import pandas as pd
import streamlit as st

from engine.summary_verdict import create_summary_verdict


STATUS_LABELS = {
    "met": "Met",
    "not_met": "Not met",
    "unknown": "Evidence unavailable",
    "manual_review": "Review required",
}

STATUS_BADGES = {
    "met": "🟢 Met",
    "not_met": "🔴 Not met",
    "unknown": "⚪ Evidence unavailable",
    "manual_review": "🟠 Review required",
}

STATUS_PRIORITY = {
    "manual_review": 0,
    "unknown": 1,
    "not_met": 2,
    "met": 3,
}

SOURCE_LABELS = {
    "criteria_registry": "Criteria definition",
    "mock_data": "Prototype assessment data",
    "sample_data": "Prototype evidence",
    "manual_review": "Manual evidence review",
}


def _filter_by_scope(criteria_results, criteria_scope):
    """Return criteria matching the selected assessment scope."""
    prefix = {
        "State": "S-",
        "Regional": "R-",
    }.get(criteria_scope)

    if prefix is None:
        return criteria_results

    return [
        result
        for result in criteria_results
        if result["criteria_id"].startswith(prefix)
    ]


def _clean_source(source):
    """Return a readable data-source label."""
    if not source:
        return "Not recorded"
    return SOURCE_LABELS.get(source, str(source).replace("_", " ").title())


def _clean_notes(notes):
    """Remove implementation language from user-facing notes."""
    if not notes:
        return "No additional notes."
    implementation_terms = ("placeholder", "implement", "test", "replace")
    if any(term in notes.lower() for term in implementation_terms):
        return "Further evidence validation is required before final assessment."
    return notes


def _clean_evidence(evidence):
    """Return evidence wording suitable for the assessment display."""
    if not evidence:
        return "No supporting evidence has been recorded."

    cleaned = str(evidence)
    cleaned = cleaned.replace("No mock result available", "No processed evidence available")
    cleaned = cleaned.replace("Sample ", "Available ")
    cleaned = cleaned.replace("sample ", "available ")
    cleaned = cleaned.replace("not implemented", "not yet assessed")
    return cleaned


def _result_reason(result):
    """Explain why the criterion has its current status."""
    status = result["status"]
    if status == "met":
        return "The available evidence supports this criterion."
    if status == "not_met":
        return "The available evidence indicates this criterion is not satisfied."
    if status == "manual_review":
        return "Available evidence needs review before this criterion can be decided."
    return "There is not enough evidence available to assess this criterion."


def _render_result_detail(result):
    """Render wrapped supporting information for one selected criterion."""
    with st.container(border=True):
        st.markdown(
            f"**{result['criteria_id']} — {result['criteria_name']}**"
        )

        detail_cols = st.columns([1, 1, 2])
        detail_cols[0].markdown(
            f"**Status**  \n{STATUS_BADGES.get(result['status'], result['status'])}"
        )
        detail_cols[1].markdown(
            f"**Mandatory**  \n{'Yes' if result['is_mandatory'] else 'No'}"
        )
        detail_cols[2].markdown(
            f"**Target category**  \n{result['target_category']}"
        )

        st.markdown("**Why this result?**")
        st.write(_result_reason(result))

        st.markdown("**Evidence**")
        st.write(_clean_evidence(result.get("evidence")))

        source_col, notes_col = st.columns(2)
        with source_col:
            st.markdown("**Data source**")
            st.write(_clean_source(result.get("data_source")))
        with notes_col:
            st.markdown("**Notes**")
            st.write(_clean_notes(result.get("notes")))


def display_results(criteria_results, default_scope="All", road_id="selected-road"):
    scope_key = f"criteria_scope_{road_id}"
    if scope_key not in st.session_state:
        st.session_state[scope_key] = default_scope

    criteria_scope = st.session_state[scope_key]
    scoped_results = _filter_by_scope(criteria_results, criteria_scope)
    summary_verdict = create_summary_verdict(scoped_results)

    st.markdown("### Summary verdict")
    st.info(summary_verdict["summary_verdict"], icon="ℹ️")
    st.caption(summary_verdict["explanation"])

    assessed_count = (
        summary_verdict["met_count"] + summary_verdict["not_met_count"]
    )
    attention_count = (
        summary_verdict["unknown_count"]
        + summary_verdict["manual_review_count"]
    )
    st.progress(
        assessed_count / summary_verdict["total_count"]
        if summary_verdict["total_count"]
        else 0,
        text=(
            f"{assessed_count} of {summary_verdict['total_count']} criteria "
            f"assessed · {attention_count} require evidence or review"
        ),
    )

    summary_cols = st.columns(4)
    summary_cols[0].metric("Met", summary_verdict["met_count"])
    summary_cols[1].metric("Not met", summary_verdict["not_met_count"])
    summary_cols[2].metric(
        "Evidence unavailable",
        summary_verdict["unknown_count"],
    )
    summary_cols[3].metric(
        "Review required",
        summary_verdict["manual_review_count"],
    )

    st.markdown("### Criteria results")
    st.caption("Choose which criteria set to apply to the selected road.")
    st.segmented_control(
        "Assessment scope",
        options=["State", "Regional", "All"],
        selection_mode="single",
        label_visibility="collapsed",
        help=(
            "State includes S- criteria, Regional includes R- criteria, and "
            "All includes every registered criterion."
        ),
        key=scope_key,
    )

    st.caption(
        "🟢 Met · 🔴 Not met · 🟠 Review required · "
        "⚪ Evidence unavailable · ◆ Mandatory"
    )

    filter_cols = st.columns([2, 1])
    status_options = list(STATUS_LABELS)
    selected_statuses = filter_cols[0].multiselect(
        "Status",
        options=status_options,
        default=status_options,
        format_func=lambda status: STATUS_LABELS[status],
        placeholder="Filter by status",
    )
    mandatory_only = filter_cols[1].toggle(
        "Mandatory only",
        value=False,
    )

    visible_results = sorted(
        (
            result
            for result in scoped_results
            if result["status"] in selected_statuses
            and (not mandatory_only or result["is_mandatory"])
        ),
        key=lambda result: (
            STATUS_PRIORITY.get(result["status"], 99),
            not result["is_mandatory"],
            result["criteria_id"],
        ),
    )

    st.caption(
        f"Showing {len(visible_results)} of {len(scoped_results)} criteria. "
        "Items needing attention are shown first."
    )

    if not visible_results:
        st.info(
            "No criteria match the selected filters. Clear a filter to see results."
        )
        return

    table_rows = [
        {
            "ID": result["criteria_id"],
            "Criterion": result["criteria_name"],
            "Status": STATUS_BADGES.get(
                result["status"],
                result["status"],
            ),
            "Mandatory": "◆" if result["is_mandatory"] else "",
        }
        for result in visible_results
    ]
    table_frame = pd.DataFrame(table_rows)

    table_event = st.dataframe(
        table_frame,
        hide_index=True,
        width="stretch",
        height=min(520, 38 + (len(table_rows) * 35)),
        on_select="rerun",
        selection_mode="multi-row",
        key="criteria_results_table",
        column_config={
            "ID": st.column_config.TextColumn(width="small"),
            "Criterion": st.column_config.TextColumn(width="large"),
            "Status": st.column_config.TextColumn(width="medium"),
            "Mandatory": st.column_config.TextColumn(width="small"),
        },
    )

    selected_rows = table_event.selection.rows
    selected_indices = selected_rows if selected_rows else [0]

    heading = (
        "Selected criterion"
        if len(selected_indices) == 1
        else "Selected criteria"
    )
    st.markdown(f"#### {heading}")
    st.caption(
        f"{len(selected_indices)} criterion selected. "
        "Select additional table rows to compare their evidence."
    )

    for selected_index in selected_indices:
        _render_result_detail(visible_results[selected_index])

    export_rows = [
        {
            "Criteria ID": result["criteria_id"],
            "Criterion": result["criteria_name"],
            "Status": STATUS_LABELS.get(result["status"], result["status"]),
            "Mandatory": "Yes" if result["is_mandatory"] else "No",
            "Target category": result["target_category"],
            "Evidence": _clean_evidence(result.get("evidence")),
            "Data source": _clean_source(result.get("data_source")),
            "Notes": _clean_notes(result.get("notes")),
        }
        for result in visible_results
    ]
    st.download_button(
        "Download assessment CSV",
        data=pd.DataFrame(export_rows).to_csv(index=False),
        file_name="criteria_assessment.csv",
        mime="text/csv",
        help="Download the currently filtered criteria assessment.",
    )
