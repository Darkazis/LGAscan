"""Evidence panel helpers for LGAScan."""

from __future__ import annotations

from typing import Any


def render_evidence_panel(evidence_records: list[dict[str, Any]]) -> None:
    """Render evidence records for selected roads."""
    import streamlit as st

    if not evidence_records:
        st.info("No processed evidence records found yet.")
        return

    for record in evidence_records:
        title = record.get("road_name") or record.get("road_id") or "Road evidence"
        with st.expander(str(title)):
            st.json(record)
