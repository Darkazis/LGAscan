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


def inject_dashboard_styles() -> None:
    """Add small layout styles for the prototype dashboard."""
    st.markdown(
        """
        <style>
        .block-container {
            padding-top: 3rem;
            padding-bottom: 2rem;
        }
        .lga-topbar {
            border: 1px solid #d7dee8;
            border-radius: 8px;
            padding: 0.75rem 1rem;
            margin-bottom: 0.85rem;
            background: #ffffff;
        }
        .lga-kpi {
            border: 1px solid #d7dee8;
            border-radius: 8px;
            padding: 0.95rem 1rem;
            min-height: 6rem;
            background: #ffffff;
        }
        .lga-kpi-value {
            font-size: 1.6rem;
            font-weight: 750;
            line-height: 1.1;
            color: #0f2f5f;
        }
        .lga-kpi-label {
            margin-top: 0.2rem;
            font-size: 0.74rem;
            font-weight: 700;
            letter-spacing: 0.02em;
            text-transform: uppercase;
            color: #26364d;
        }
        .lga-panel {
            border: 1px solid #d7dee8;
            border-radius: 8px;
            padding: 0.9rem 1rem;
            background: #ffffff;
        }
        .lga-status-pill {
            display: inline-block;
            border-radius: 999px;
            padding: 0.2rem 0.55rem;
            margin-top: 0.35rem;
            border: 1px solid #f1b66d;
            color: #9a4f00;
            background: #fff6e8;
            font-size: 0.8rem;
            font-weight: 700;
        }
        .lga-ranking-wrap {
            width: 100%;
            overflow-x: auto;
            border: 1px solid #d7dee8;
            border-radius: 8px;
            background: #ffffff;
        }
        .lga-ranking-table {
            width: 100%;
            min-width: 54rem;
            border-collapse: collapse;
            table-layout: fixed;
        }
        .lga-ranking-table th,
        .lga-ranking-table td {
            border-bottom: 1px solid #e5eaf0;
            padding: 0.55rem 0.6rem;
            vertical-align: top;
            white-space: normal;
            overflow-wrap: break-word;
            word-break: normal;
            line-height: 1.35;
            font-size: 0.92rem;
        }
        .lga-ranking-table th {
            background: #f7f9fc;
            color: #5c6675;
            font-weight: 700;
            text-align: left;
            white-space: nowrap;
            overflow-wrap: normal;
        }
        .lga-ranking-table tr:last-child td {
            border-bottom: 0;
        }
        .lga-ranking-table .numeric {
            text-align: right;
            white-space: nowrap;
        }
        .lga-ranking-table .road-number {
            text-align: right;
            white-space: nowrap;
        }
        .lga-ranking-table .current-category {
            white-space: nowrap;
        }
        .lga-ranking-table .map-link {
            white-space: nowrap;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_dashboard_header() -> None:
    """Render the main dashboard heading and prototype context."""
    st.markdown(
        """
        <div class="lga-topbar">
            <strong>LGAScan</strong>
            <span style="margin-left: 1rem; color: #516173;">
                Case Study LGA: development mock sample
            </span>
            <span style="float: right; color: #516173;">Export placeholder</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.caption(
        "Early road category review screening dashboard using mock data. "
        "Heavy GIS and data processing should happen before data reaches Streamlit."
    )


def render_kpi_card(label: str, value: int | str, help_text: str = "") -> None:
    """Render a compact dashboard KPI card."""
    st.markdown(
        f"""
        <div class="lga-kpi">
            <div class="lga-kpi-value">{value}</div>
            <div class="lga-kpi-label">{label}</div>
            <div style="margin-top: 0.35rem; color: #6b7788; font-size: 0.82rem;">
                {help_text}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_placeholder_section(title: str, body: str) -> None:
    """Render a consistent placeholder section."""
    st.header(title)
    st.info(body)
