import pandas as pd
import streamlit as st


def display_results(criteria_results, summary_verdict):
    status_labels = {
        "met": "Met",
        "not_met": "Not met",
        "unknown": "Unknown",
        "manual_review": "Manual review",
    }

    st.markdown("### Summary verdict")
    st.info(summary_verdict["summary_verdict"], icon="ℹ️")

    summary_cols = st.columns(4)
    summary_cols[0].metric(
        "Met",
        summary_verdict["met_count"],
        help="Criteria with sufficient evidence to be marked as met.",
    )
    summary_cols[1].metric(
        "Not met",
        summary_verdict["not_met_count"],
        help="Criteria where the available evidence does not meet the requirement.",
    )
    summary_cols[2].metric(
        "Unknown",
        summary_verdict["unknown_count"],
        help="Criteria without enough available evidence for an assessment.",
    )
    summary_cols[3].metric(
        "Manual review",
        summary_verdict["manual_review_count"],
        help="Criteria that require a person to review the available evidence.",
    )

    st.markdown("### Criteria results")

    filter_cols = st.columns([2, 1])
    status_options = list(status_labels)
    selected_statuses = filter_cols[0].multiselect(
        "Filter by status",
        options=status_options,
        default=status_options,
        format_func=lambda status: status_labels[status],
    )
    mandatory_only = filter_cols[1].toggle(
        "Mandatory criteria only",
        value=False,
    )

    visible_results = [
        result
        for result in criteria_results
        if result["status"] in selected_statuses
        and (not mandatory_only or result["is_mandatory"])
    ]

    st.caption(
        f"Showing {len(visible_results)} of {len(criteria_results)} criteria. "
        "Use the table controls to search, resize columns, or download CSV."
    )

    table_rows = [
        {
            "Criteria ID": result["criteria_id"],
            "Criterion": result["criteria_name"],
            "Status": status_labels.get(result["status"], result["status"]),
            "Target category": result["target_category"],
            "Mandatory": result["is_mandatory"],
            "Evidence": result["evidence"],
            "Data source": result["data_source"],
            "Notes": result["notes"],
        }
        for result in visible_results
    ]

    if not table_rows:
        st.warning("No criteria match the selected table filters.")
        return

    st.dataframe(
        pd.DataFrame(table_rows),
        hide_index=True,
        use_container_width=True,
        height=min(680, 38 + (len(table_rows) * 35)),
        column_config={
            "Criteria ID": st.column_config.TextColumn(width="small"),
            "Criterion": st.column_config.TextColumn(width="large"),
            "Status": st.column_config.TextColumn(width="small"),
            "Target category": st.column_config.TextColumn(width="small"),
            "Mandatory": st.column_config.CheckboxColumn(width="small"),
            "Evidence": st.column_config.TextColumn(width="large"),
            "Data source": st.column_config.TextColumn(width="medium"),
            "Notes": st.column_config.TextColumn(width="large"),
        },
    )
