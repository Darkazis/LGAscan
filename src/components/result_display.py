import streamlit as st


def display_results(criteria_results, summary_verdict):
    st.subheader("Summary Verdict")

    st.info(summary_verdict["summary_verdict"])

    st.write(f'Criteria met: {summary_verdict["met_count"]}')
    st.write(f'Not met: {summary_verdict["not_met_count"]}')
    st.write(f'Unknown: {summary_verdict["unknown_count"]}')
    st.write(f'Manual review: {summary_verdict["manual_review_count"]}')

    st.subheader("Criteria Results")

    for result in criteria_results:
        status = result["status"]

        if status == "met":
            st.success(f'{result["criteria_id"]}: {result["criteria_name"]}')
        elif status == "not_met":
            st.error(f'{result["criteria_id"]}: {result["criteria_name"]}')
        elif status == "unknown":
            st.warning(f'{result["criteria_id"]}: {result["criteria_name"]}')
        elif status == "manual_review":
            st.warning(f'{result["criteria_id"]}: {result["criteria_name"]}')

        with st.expander("View evidence"):
            st.write(f'**Status:** {result["status"]}')
            st.write(f'**Target category:** {result["target_category"]}')
            st.write(f'**Mandatory:** {result["is_mandatory"]}')
            st.write(f'**Evidence:** {result["evidence"]}')
            st.write(f'**Data source:** {result["data_source"]}')
            st.write(f'**Notes:** {result["notes"]}')