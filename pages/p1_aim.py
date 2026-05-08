"""
Page 1 — Aim of the Work
"""
import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import set_page_background, page_header, info_card

def show():
    set_page_background("aim.svg", overlay_opacity=0.78)
    page_header(
        "Aim of the Work",
        "Understanding the objectives and scope of this bioethanol ML study",
        accent_color="#4ade80"
    )

    col1, col2 = st.columns([3, 2], gap="large")

    with col1:
        st.markdown("""
        <h3 style="color:#86efac; font-size:1.2rem; font-weight:600; margin-bottom:1rem;">
            🔬 Research Objective
        </h3>
        """, unsafe_allow_html=True)

        info_card("""
        This project aims to leverage <b>Machine Learning</b> to optimize bioethanol
        production by analyzing two complementary datasets — one covering
        <b>fermentation process parameters</b> and another covering
        <b>large-scale industrial production metrics</b>.
        """, accent="#4ade80")

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <h3 style="color:#86efac; font-size:1.2rem; font-weight:600; margin-bottom:1rem;">
            📦 Dataset 1 — Fermentation Parameters
        </h3>
        """, unsafe_allow_html=True)

        info_card("""
        <b>5,000 rows · 8 columns</b><br><br>
        Covers biochemical conversion conditions that directly impact ethanol yield:
        Temperature, pH, Fermentation Time, Substrate Concentration,
        Enzyme Dosage, Inoculum Size, and Agitation Speed.
        <br><br>🎯 <b>Target:</b> Yield (10–100%)
        """, accent="#22c55e")

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <h3 style="color:#86efac; font-size:1.2rem; font-weight:600; margin-bottom:1rem;">
            🏭 Dataset 2 — Industrial Production Metrics
        </h3>
        """, unsafe_allow_html=True)

        info_card("""
        <b>27,856 rows · 15 columns</b><br><br>
        Covers operational, environmental, and economic facets:
        Feedstock Yield, Production Capacity, Energy Consumption,
        Feedstock/Transportation/Distribution Costs, Carbon Emissions,
        Water Usage, Market Demand, and Price per Gallon.
        <br><br>🎯 <b>Targets:</b> Bioethanol Growth, Carbon Emissions, Water Usage, Production Capacity
        """, accent="#16a34a")

    with col2:
        st.markdown("""
        <h3 style="color:#86efac; font-size:1.2rem; font-weight:600; margin-bottom:1rem;">
            🎯 Key Goals
        </h3>
        """, unsafe_allow_html=True)

        goals = [
            ("⚗️", "Predict ethanol yield", "from fermentation process conditions using regression models"),
            ("🌍", "Forecast sustainability", "metrics: carbon emissions, water usage, and production capacity"),
            ("🔍", "Feature importance", "reveal which parameters most affect yield and environmental impact"),
            ("⚙️", "Process optimization", "find the optimal combination of settings to maximize yield"),
            ("📉", "Reduce emissions", "model the relationship between operations and CO₂ output"),
        ]

        for icon, title, desc in goals:
            st.markdown(f"""
            <div style="
                background: rgba(255,255,255,0.04);
                border: 1px solid rgba(74,222,128,0.15);
                border-radius: 10px;
                padding: 0.9rem 1.1rem;
                margin-bottom: 0.6rem;
                display: flex;
                gap: 0.8rem;
                align-items: flex-start;
            ">
                <span style="font-size:1.4rem; line-height:1;">{icon}</span>
                <div>
                    <div style="font-weight:600; color:#86efac; font-size:0.9rem;">{title}</div>
                    <div style="color:rgba(255,255,255,0.5); font-size:0.82rem; margin-top:2px;">{desc}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <div style="
            background: rgba(74,222,128,0.06);
            border: 1px solid rgba(74,222,128,0.2);
            border-radius: 12px;
            padding: 1.2rem;
            text-align: center;
        ">
            <div style="font-size:0.75rem; color:rgba(255,255,255,0.4);
                        text-transform:uppercase; letter-spacing:0.08em; margin-bottom:0.8rem;">
                Dataset Overview
            </div>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.8rem;">
                <div>
                    <div style="font-size:1.8rem; font-weight:700; color:#4ade80;">5K</div>
                    <div style="font-size:0.75rem; color:rgba(255,255,255,0.4);">Fermentation rows</div>
                </div>
                <div>
                    <div style="font-size:1.8rem; font-weight:700; color:#22c55e;">27K</div>
                    <div style="font-size:0.75rem; color:rgba(255,255,255,0.4);">Production rows</div>
                </div>
                <div>
                    <div style="font-size:1.8rem; font-weight:700; color:#16a34a;">8</div>
                    <div style="font-size:0.75rem; color:rgba(255,255,255,0.4);">Process features</div>
                </div>
                <div>
                    <div style="font-size:1.8rem; font-weight:700; color:#4ade80;">4</div>
                    <div style="font-size:0.75rem; color:rgba(255,255,255,0.4);">ML targets</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
