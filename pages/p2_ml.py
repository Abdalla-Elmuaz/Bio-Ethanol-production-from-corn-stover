"""
Page 2 — ML of the Project
"""
import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import set_page_background, page_header, info_card

def show():
    set_page_background("ml.svg", overlay_opacity=0.80)
    page_header(
        "ML of the Project",
        "Models, pipeline architecture, and machine learning strategy",
        accent_color="#60a5fa"
    )

    # ── Pipeline diagram ────────────────────────────────────
    st.markdown("""
    <h3 style="color:#93c5fd; font-size:1.1rem; font-weight:600; margin-bottom:1rem;">
        🏗️ Pipeline Architecture
    </h3>
    """, unsafe_allow_html=True)

    steps = [
        ("01", "Label Encoding",    "Convert categorical columns (Country) to integers",         "#3b82f6"),
        ("02", "Feature Engineering","Engineer ratio features: Water_per_Energy, BG_per_Energy, Carbon_Intensity…", "#60a5fa"),
        ("03", "Train / Test Split", "80% training · 20% testing · random_state=42",             "#93c5fd"),
        ("04", "StandardScaler",    "Normalize all features inside the Pipeline (no leakage)",   "#bfdbfe"),
        ("05", "Model Training",    "RandomForest · GradientBoosting · Ridge Regression",        "#60a5fa"),
        ("06", "Evaluation",        "R² · MAE · RMSE · MSE for every model and target",          "#3b82f6"),
    ]

    cols = st.columns(6, gap="small")
    for i, (num, title, desc, color) in enumerate(steps):
        with cols[i]:
            st.markdown(f"""
            <div style="
                background: rgba(255,255,255,0.04);
                border: 1px solid {color}33;
                border-top: 3px solid {color};
                border-radius: 10px;
                padding: 1rem 0.8rem;
                text-align: center;
                height: 160px;
            ">
                <div style="font-size:1.5rem; font-weight:700; color:{color}; opacity:0.5;">{num}</div>
                <div style="font-size:0.82rem; font-weight:600; color:{color}; margin:0.4rem 0;">{title}</div>
                <div style="font-size:0.73rem; color:rgba(255,255,255,0.4); line-height:1.4;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Two tracks ──────────────────────────────────────────
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <h3 style="color:#93c5fd; font-size:1.1rem; font-weight:600; margin-bottom:0.8rem;">
            ⚗️ Track A — Fermentation (Dataset 1)
        </h3>
        """, unsafe_allow_html=True)
        info_card("""
        <b>Target:</b> Yield (10–100%)<br>
        <b>Features:</b> Temp, pH, Time, Substrate, EnzymeDose, InoculumSize, AgitationSpeed<br><br>
        Nonlinear relationships captured by tree-based models.
        Substrate concentration is the strongest predictor (r = 0.76).
        """, accent="#3b82f6")

    with col2:
        st.markdown("""
        <h3 style="color:#93c5fd; font-size:1.1rem; font-weight:600; margin-bottom:0.8rem;">
            🌍 Track B — Industrial (Dataset 2)
        </h3>
        """, unsafe_allow_html=True)
        info_card("""
        <b>Targets:</b> Bioethanol Growth · Water Usage · Carbon Emissions · Production Capacity<br>
        <b>Features:</b> All numeric cols + 8 engineered ratio features<br><br>
        Ratio features (Water_per_Energy, BG_per_Energy) unlocked R² ≈ 1.000.
        """, accent="#60a5fa")

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Model comparison table ───────────────────────────────
    st.markdown("""
    <h3 style="color:#93c5fd; font-size:1.1rem; font-weight:600; margin-bottom:1rem;">
        🤖 Model Comparison
    </h3>
    """, unsafe_allow_html=True)

    models = [
        ("Random Forest",     "Ensemble of 200 decision trees (n_estimators=200)",
         "Handles nonlinearity · Built-in feature importance · Robust to outliers",
         "R² ≈ 1.0000 on all targets", "#4ade80", "🥇"),
        ("Gradient Boosting", "Sequential boosting (n_estimators=200, max_depth=5)",
         "Corrects errors iteratively · Best on tabular data · SHAP-compatible",
         "R² ≈ 0.9994 on best target", "#60a5fa", "🥈"),
        ("Ridge Regression",  "Regularized linear model (alpha=1.0)",
         "Fast linear baseline · L2 regularization · Interpretable coefficients",
         "R² ≈ 0.96–0.99 on structured targets", "#fbbf24", "🥉"),
    ]

    for medal, name, desc, performance, color, rank in [(m[5],m[0],m[1],m[3],m[4],m[5]) for m in models]:
        st.markdown(f"""
        <div style="
            background: rgba(255,255,255,0.04);
            border: 1px solid {color}22;
            border-left: 3px solid {color};
            border-radius: 10px;
            padding: 1rem 1.4rem;
            margin-bottom: 0.6rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        ">
            <div style="flex:1;">
                <span style="font-size:1.1rem; margin-right:0.5rem;">{rank}</span>
                <span style="font-weight:600; color:{color}; font-size:1rem;">{name}</span>
                <div style="font-size:0.82rem; color:rgba(255,255,255,0.45); margin-top:4px;">{desc}</div>
            </div>
            <div style="
                background: {color}15;
                border: 1px solid {color}33;
                border-radius: 8px;
                padding: 0.4rem 0.8rem;
                font-size:0.8rem;
                color:{color};
                font-weight:600;
                white-space:nowrap;
                margin-left: 1rem;
            ">{performance}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Final R2 summary ────────────────────────────────────
    st.markdown("""
    <h3 style="color:#93c5fd; font-size:1.1rem; font-weight:600; margin-bottom:1rem;">
        📊 Final R² Results (Random Forest)
    </h3>
    """, unsafe_allow_html=True)

    results = [
        ("Yield",              "Dataset 1", "~1.0000", "#4ade80"),
        ("Production Capacity","Dataset 2", "~1.0000", "#4ade80"),
        ("Water Usage",        "Dataset 2", "~0.9980", "#60a5fa"),
        ("Carbon Emissions",   "Dataset 2", "~0.9991", "#60a5fa"),
        ("Bioethanol Growth",  "Dataset 2", "~1.0000", "#4ade80"),
    ]

    cols = st.columns(5, gap="small")
    for i, (target, dataset, r2, color) in enumerate(results):
        with cols[i]:
            st.markdown(f"""
            <div style="
                background: rgba(255,255,255,0.04);
                border: 1px solid {color}33;
                border-radius: 10px;
                padding: 1rem;
                text-align: center;
            ">
                <div style="font-size:0.7rem; color:rgba(255,255,255,0.35);
                            text-transform:uppercase; letter-spacing:0.06em;">{dataset}</div>
                <div style="font-size:0.82rem; font-weight:600; color:{color};
                            margin: 0.3rem 0;">{target}</div>
                <div style="font-size:1.6rem; font-weight:700; color:{color};">{r2}</div>
                <div style="font-size:0.7rem; color:rgba(255,255,255,0.3);">R² Score</div>
            </div>
            """, unsafe_allow_html=True)
