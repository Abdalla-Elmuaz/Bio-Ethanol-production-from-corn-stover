"""
Page 3 — Analysis & Visualization
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import set_page_background, page_header

THEME = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor ="rgba(0,0,0,0)",
    font=dict(color="#e2e8f0", family="Exo 2"),
    xaxis=dict(gridcolor="rgba(255,255,255,0.06)", linecolor="rgba(255,255,255,0.1)"),
    yaxis=dict(gridcolor="rgba(255,255,255,0.06)", linecolor="rgba(255,255,255,0.1)"),
)

@st.cache_data
def load_data():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    df1  = pd.read_csv(os.path.join(base, "data", "fermentation.csv"))
    df2  = pd.read_csv(os.path.join(base, "data", "production.csv"))

    # ── Feature Engineering for Visualizations ──────────────
    df1["Cooling_Duty"]          = df1["Temp"] * df1["Time"]
    df1["Ethanol_Production_Rate"] = df1["Yield"] / df1["Time"]

    return df1, df2

def show():
    set_page_background("analysis.svg", overlay_opacity=0.82)
    page_header(
        "Analysis & Visualization",
        "Exploratory data analysis across both datasets",
        accent_color="#a78bfa"
    )

    try:
        df1, df2 = load_data()
    except Exception:
        st.warning("⚠️ Place your CSV files in the `data/` folder as `fermentation.csv` and `production.csv`")
        return

    tab1, tab2, tab3 = st.tabs([
        "📊 Distributions", "🔥 Correlations", "📈 Visualizations"
    ])

    with tab1:
        _distributions(df1, df2)
    with tab2:
        _correlations(df1, df2)
    with tab3:
        _visualizations(df1)


# ── Tab 1: Distributions ─────────────────────────────────────
def _distributions(df1, df2):

    # Dataset 1 — exclude Year if present
    st.markdown("#### Dataset 1 — Fermentation Parameter Distributions")
    num1 = [c for c in df1.select_dtypes(include="number").columns if c.lower() != "year"]
    sel1 = st.multiselect("Select features", num1, default=num1[:4], key="dist1")
    if sel1:
        cols = st.columns(min(len(sel1), 4))
        for i, col in enumerate(sel1):
            with cols[i % 4]:
                fig = px.histogram(df1, x=col, nbins=40,
                                   color_discrete_sequence=["#8b5cf6"])
                fig.update_layout(**THEME, height=250,
                                  margin=dict(l=10,r=10,t=30,b=10),
                                  title=dict(text=col, font=dict(size=13)))
                st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Dataset 2 — exclude Year if present
    st.markdown("#### Dataset 2 — Production Metrics Distributions")
    num2 = [c for c in df2.select_dtypes(include="number").columns if c.lower() != "year"]
    sel2 = st.multiselect("Select features", num2, default=num2[:4], key="dist2")
    if sel2:
        cols2 = st.columns(min(len(sel2), 4))
        for i, col in enumerate(sel2):
            with cols2[i % 4]:
                fig = px.histogram(df2, x=col, nbins=40,
                                   color_discrete_sequence=["#14b8a6"])
                fig.update_layout(**THEME, height=250,
                                  margin=dict(l=10,r=10,t=30,b=10),
                                  title=dict(text=col, font=dict(size=13)))
                st.plotly_chart(fig, use_container_width=True)


# ── Tab 2: Correlations ──────────────────────────────────────
def _correlations(df1, df2):
    col1, col2 = st.columns(2, gap="medium")

    with col1:
        st.markdown("#### Dataset 1 — Fermentation")
        # Exclude Year
        num1 = [c for c in df1.select_dtypes(include="number").columns if c.lower() != "year"]
        corr1 = df1[num1].corr().round(2)
        fig = px.imshow(corr1, color_continuous_scale="RdBu_r",
                        zmin=-1, zmax=1, text_auto=True, aspect="auto")
        fig.update_layout(**THEME, height=450, margin=dict(l=10,r=10,t=10,b=10))
        fig.update_traces(textfont_size=9)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("#### Dataset 2 — Production (numeric only)")
        # Exclude Year
        num2 = [c for c in df2.select_dtypes(include="number").columns if c.lower() != "year"]
        corr2 = df2[num2].corr().round(2)
        fig2 = px.imshow(corr2, color_continuous_scale="RdBu_r",
                         zmin=-1, zmax=1, text_auto=True, aspect="auto")
        fig2.update_layout(**THEME, height=450, margin=dict(l=10,r=10,t=10,b=10))
        fig2.update_traces(textfont_size=7)
        st.plotly_chart(fig2, use_container_width=True)


# ── Tab 3: Visualizations (replaced Trends) ──────────────────
def _visualizations(df1):

    # Check required columns exist
    has_cooling  = "Cooling_Duty" in df1.columns
    has_epr      = "Ethanol_Production_Rate" in df1.columns

    st.markdown("#### Fermentation Relationship Visualizations")
    st.markdown("---")

    # ── Chart 1: Yield vs Substrate ──────────────────────────
    st.markdown("##### 1️⃣ Ethanol Yield vs Glucose Concentration")
    fig1 = px.scatter(
        df1, x="Substrate", y="Yield",
        trendline="lowess", opacity=0.5,
        color_discrete_sequence=["#7c3aed"],
        title="Ethanol Yield vs Glucose Concentration",
        labels={"Substrate": "Glucose Concentration", "Yield": "Ethanol Yield (%)"}
    )
    fig1.update_layout(**THEME, height=420, margin=dict(l=10,r=10,t=45,b=10))
    fig1.update_traces(marker=dict(size=4))
    st.plotly_chart(fig1, use_container_width=True)

    st.markdown("---")

    # ── Charts 2 & 3: Cooling Duty (if column exists) ────────
    if has_cooling:
        c1, c2 = st.columns(2, gap="medium")

        with c1:
            st.markdown("##### 2️⃣ Cooling Duty vs Temperature")
            fig2 = px.scatter(
                df1, x="Temp", y="Cooling_Duty",
                trendline="lowess", opacity=0.5,
                color_discrete_sequence=["#0ea5e9"],
                title="Cooling Duty vs Fermentation Temperature",
                labels={"Temp": "Fermentation Temperature (°C)", "Cooling_Duty": "Cooling Duty"}
            )
            fig2.update_layout(**THEME, height=380, margin=dict(l=10,r=10,t=45,b=10))
            fig2.update_traces(marker=dict(size=4))
            st.plotly_chart(fig2, use_container_width=True)

        with c2:
            st.markdown("##### 3️⃣ Cooling Duty vs Glucose Concentration")
            fig3 = px.scatter(
                df1, x="Substrate", y="Cooling_Duty",
                trendline="lowess", opacity=0.5,
                color_discrete_sequence=["#f59e0b"],
                title="Cooling Duty vs Glucose Concentration",
                labels={"Substrate": "Glucose Concentration", "Cooling_Duty": "Cooling Duty"}
            )
            fig3.update_layout(**THEME, height=380, margin=dict(l=10,r=10,t=45,b=10))
            fig3.update_traces(marker=dict(size=4))
            st.plotly_chart(fig3, use_container_width=True)

        st.markdown("---")

    # ── Charts 4 & 5: 2D Heatmaps ────────────────────────────
    if has_epr:
        st.markdown("##### 4️⃣ Effect of Glucose Concentration & Temperature on Ethanol Production")
        _heatmap_2d(
            df1,
            x_col="Substrate", y_col="Temp", weight_col="Ethanol_Production_Rate",
            x_label="Glucose Concentration",
            y_label="Fermentation Temperature (°C)",
            title="Avg Ethanol Production Rate — Substrate × Temperature",
            colorscale="Blues"
        )

        st.markdown("---")

        st.markdown("##### 5️⃣ Effect of Glucose Concentration & pH on Ethanol Production")
        _heatmap_2d(
            df1,
            x_col="Substrate", y_col="pH", weight_col="Ethanol_Production_Rate",
            x_label="Glucose Concentration",
            y_label="pH",
            title="Avg Ethanol Production Rate — Substrate × pH",
            colorscale="Teal"
        )

    elif not has_epr:
        st.info("ℹ️ Column `Ethanol_Production_Rate` not found in Dataset 1 — heatmaps skipped.")


def _heatmap_2d(df, x_col, y_col, weight_col, x_label, y_label, title, colorscale="Blues"):
    """Build a 2D binned heatmap using Plotly (replaces matplotlib)."""
    x_bins = np.linspace(df[x_col].min(), df[x_col].max(), 20)
    y_bins = np.linspace(df[y_col].min(), df[y_col].max(), 20)

    heatmap, xedges, yedges = np.histogram2d(
        df[x_col], df[y_col],
        bins=[x_bins, y_bins],
        weights=df[weight_col]
    )
    counts, _, _ = np.histogram2d(df[x_col], df[y_col], bins=[x_bins, y_bins])

    with np.errstate(invalid="ignore"):
        heatmap = np.where(counts > 0, heatmap / counts, np.nan)

    x_centers = (xedges[:-1] + xedges[1:]) / 2
    y_centers = (yedges[:-1] + yedges[1:]) / 2

    fig = go.Figure(go.Heatmap(
        z=heatmap.T,
        x=x_centers,
        y=y_centers,
        colorscale=colorscale,
        colorbar=dict(title="Avg Ethanol<br>Production Rate",
                      titlefont=dict(color="#e2e8f0"),
                      tickfont=dict(color="#e2e8f0")),
        hoverongaps=False,
    ))
    fig.update_layout(
        **THEME,
        height=430,
        title=title,
        xaxis_title=x_label,
        yaxis_title=y_label,
        margin=dict(l=10, r=10, t=45, b=10)
    )
    st.plotly_chart(fig, use_container_width=True)