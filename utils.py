"""
utils.py — Shared helpers for all pages
"""

import base64
import os
import streamlit as st


def get_svg_as_base64(svg_path: str) -> str:
    """Read an SVG file and return as base64 data URI."""
    with open(svg_path, "r", encoding="utf-8") as f:
        svg_content = f.read()
    b64 = base64.b64encode(svg_content.encode("utf-8")).decode("utf-8")
    return f"data:image/svg+xml;base64,{b64}"


def set_page_background(svg_filename: str, overlay_opacity: float = 0.82):
    """
    Inject CSS to set an SVG as full-page background with a dark overlay.
    overlay_opacity: 0.0 = fully transparent, 1.0 = fully opaque overlay
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    svg_path  = os.path.join(base_dir, "assets", "backgrounds", svg_filename)
    data_uri  = get_svg_as_base64(svg_path)

    r = int(overlay_opacity * 5)
    g = int(overlay_opacity * 5)
    b = int(overlay_opacity * 8)
    oa = overlay_opacity

    st.markdown(f"""
    <style>
    /* ── Full background ── */
    .stApp {{
        background-image: url("{data_uri}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    /* ── Dark overlay ── */
    .stApp::before {{
        content: "";
        position: fixed;
        inset: 0;
        background: rgba({r},{g},{b},{oa});
        z-index: 0;
        pointer-events: none;
    }}
    /* ── Lift content above overlay ── */
    .stApp > * {{ position: relative; z-index: 1; }}

    /* ── Global typography ── */
    @import url('https://fonts.googleapis.com/css2?family=Exo+2:wght@300;400;500;600;700&family=Share+Tech+Mono&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Exo 2', sans-serif;
        color: #e2e8f0;
    }}

    /* ── Sidebar ── */
    section[data-testid="stSidebar"] {{
        background: rgba(2, 8, 20, 0.92) !important;
        border-right: 1px solid rgba(255,255,255,0.07);
    }}
    section[data-testid="stSidebar"] * {{
        color: #cbd5e1 !important;
    }}

    /* ── Cards / metric containers ── */
    div[data-testid="metric-container"] {{
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 12px;
        padding: 16px;
        backdrop-filter: blur(8px);
    }}

    /* ── Expanders ── */
    details {{
        background: rgba(255,255,255,0.04) !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
        border-radius: 10px;
    }}

    /* ── Input widgets ── */
    .stSlider, .stSelectbox, .stNumberInput {{
        background: transparent !important;
    }}

    /* ── Buttons ── */
    .stButton > button {{
        font-family: 'Exo 2', sans-serif;
        font-weight: 600;
        border-radius: 8px;
        border: 1px solid rgba(255,255,255,0.2);
        background: rgba(255,255,255,0.08);
        color: #f1f5f9;
        transition: all 0.2s;
    }}
    .stButton > button:hover {{
        background: rgba(255,255,255,0.15);
        border-color: rgba(255,255,255,0.4);
    }}

    /* ── Dataframes ── */
    .dataframe {{
        background: rgba(0,0,0,0.4) !important;
    }}

    /* ── Hide Streamlit branding ── */
    #MainMenu, footer, header {{ visibility: hidden; }}
    </style>
    """, unsafe_allow_html=True)


def page_header(title: str, subtitle: str, accent_color: str = "#4ade80"):
    """Render a styled page header with title and subtitle."""
    st.markdown(f"""
    <div style="
        padding: 2.5rem 0 1.5rem 0;
        border-bottom: 1px solid rgba(255,255,255,0.08);
        margin-bottom: 2rem;
    ">
        <h1 style="
            font-family: 'Exo 2', sans-serif;
            font-size: 2.8rem;
            font-weight: 700;
            color: {accent_color};
            margin: 0;
            letter-spacing: -0.02em;
            line-height: 1.1;
        ">{title}</h1>
        <p style="
            font-size: 1.1rem;
            color: rgba(255,255,255,0.55);
            margin: 0.6rem 0 0 0;
            font-weight: 300;
            letter-spacing: 0.02em;
        ">{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)


def info_card(content: str, accent: str = "#4ade80"):
    """Render a glassy info card."""
    st.markdown(f"""
    <div style="
        background: rgba(255,255,255,0.04);
        border: 1px solid {accent}33;
        border-left: 3px solid {accent};
        border-radius: 10px;
        padding: 1.2rem 1.4rem;
        margin: 0.8rem 0;
        backdrop-filter: blur(6px);
        font-size: 0.95rem;
        line-height: 1.7;
        color: #cbd5e1;
    ">{content}</div>
    """, unsafe_allow_html=True)


def result_badge(label: str, value: str, accent: str = "#4ade80"):
    """Render a metric badge."""
    st.markdown(f"""
    <div style="
        display: inline-block;
        background: rgba(255,255,255,0.05);
        border: 1px solid {accent}55;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        margin: 0.3rem;
        text-align: center;
        min-width: 140px;
    ">
        <div style="font-size:0.75rem; color:rgba(255,255,255,0.45); text-transform:uppercase; letter-spacing:0.08em;">{label}</div>
        <div style="font-size:1.4rem; font-weight:700; color:{accent}; margin-top:2px;">{value}</div>
    </div>
    """, unsafe_allow_html=True)
