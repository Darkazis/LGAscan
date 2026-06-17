"""Shared page setup and layout helpers for LGAScan."""

from __future__ import annotations

from pathlib import Path

import streamlit as st


SRC_DIR = Path(__file__).resolve().parents[1]
LOGO_PATH = SRC_DIR / "assets" / "logo.png"


def configure_page() -> None:
    """Apply Streamlit page settings for the dashboard."""
    page_icon = None

    if LOGO_PATH.exists():
        from PIL import Image

        page_icon = Image.open(LOGO_PATH)

    st.set_page_config(
        page_title="LGAScan",
        page_icon=page_icon,
        layout="wide",
    )


def render_dashboard_header() -> None:
    """Render the main dashboard heading and prototype context."""
    st.title("LGAScan Dashboard Prototype")
    st.caption("Early road recategorisation screening dashboard using mock data.")
    st.info(
        "This prototype uses mock road records only. Heavy GIS and data "
        "processing should happen before data reaches the Streamlit dashboard."
    )


def render_placeholder_section(title: str, body: str) -> None:
    """Render a consistent placeholder section."""
    st.header(title)
    st.info(body)

