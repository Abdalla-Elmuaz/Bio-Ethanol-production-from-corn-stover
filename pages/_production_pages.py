"""
Pages 5, 6, 7 — Carbon Emissions / Water Usage / Bioethanol Growth
Shared prediction page template for Dataset 2 targets
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import set_page_background, page_header, info_card

PLOTLY_THEME = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="#e2e8f0", family="Exo 2"),
    xaxis=dict(gridcolor="rgba(255,255,255,0.06)"),
    yaxis=dict(gridcolor="rgba(255,255,255,0.06)"),
)

PAGE_CONFIG = {
    "carbon": {
        "bg":       "carbon.svg",
        "overlay":  0.82,
        "title":    "Carbon Emissions",
        "subtitle": "Predict CO₂ emissions from industrial bioethanol production",
        "accent":   "#ef4444",
        "target":   "Carbon_Emissions",
        "icon":     "💨",
        "unit":     "Mt CO₂",
    },
    "water": {
        "bg":       "water.svg",
        "overlay":  0.80,
        "title":    "Water Usage",
        "subtitle": "Predict water consumption across production operations",
        "accent":   "#38bdf8",
        "target":   "Water_Usage",
        "icon":     "💧",
        "unit":     "ML",
    },
    "growth": {
        "bg":       "growth.svg",
        "overlay":  0.80,
        "title":    "Bioethanol Growth",
        "subtitle": "Predict bioethanol industry growth rate (0–15 scale)",
        "accent":   "#4ade80",
        "target":   "Bioethanol_Growth",
        "icon":     "📈",
        "unit":     "Growth Index",
    },
}


@st.cache_resource
def train_production_models():
    """Train all 3 production models once and cache."""
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler, LabelEncoder
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(base, "data", "production.csv")
    df   = pd.read_csv(path)

    # Encode
    le = LabelEncoder()
    for col in df.select_dtypes(include="object").columns:
        df[col] = le.fit_transform(df[col])
    if str(df["Year"].dtype).startswith("datetime"):
        df["Year"] = df["Year"].dt.year.astype(int)

    # Redefine Bioethanol_Growth
    pc = df["Production_Capacity"]
    df["Bioethanol_Growth"] = ((pc - pc.min()) / (pc.max() - pc.min())) * 15

    # Engineer features
    df["Total_Cost"]        = df["Feedstock_Cost"] + df["Transportation_Cost"] + df["Distribution_Cost"]
    df["Energy_Efficiency"] = df["Production_Capacity"] / (df["Energy_Consumption"] + 1e-6)
    df["Revenue"]           = df["Production_Capacity"] * df["Price_Per_Gallon"]
    df["Carbon_Intensity"]  = df["Carbon_Emissions"]  / (df["Production_Capacity"] + 1e-6)
    df["Water_Intensity"]   = df["Water_Usage"]       / (df["Production_Capacity"] + 1e-6)
    df["Cost_Efficiency"]   = df["Production_Capacity"] / (df["Total_Cost"] + 1e-6)
    df["Water_per_Energy"]  = df["Water_Usage"]        / (df["Energy_Consumption"] + 1e-6)
    df["BG_per_Energy"]     = df["Bioethanol_Growth"]  / (df["Energy_Consumption"] + 1e-6)

    all_targets = ["Bioethanol_Growth","Water_Usage","Carbon_Emissions","Production_Capacity"]
    feature_cols = [c for c in df.select_dtypes(include="number").columns
                    if c not in all_targets]

    models  = {}
    metrics = {}

    for target in ["Carbon_Emissions", "Water_Usage", "Bioethanol_Growth"]:
        X = df[feature_cols]
        y = df[target]
        X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

        pipe = Pipeline([
            ("scaler", StandardScaler()),
            ("model",  RandomForestRegressor(n_estimators=200, random_state=42, n_jobs=-1))
        ])
        pipe.fit(X_tr, y_tr)
        y_pred = pipe.predict(X_te)

        models[target]  = pipe
        metrics[target] = {
            "r2":       round(r2_score(y_te, y_pred), 4),
            "mae":      round(mean_absolute_error(y_te, y_pred), 4),
            "rmse":     round(np.sqrt(mean_squared_error(y_te, y_pred)), 4),
            "features": feature_cols,
            "y_te":     y_te.values[:200],
            "y_pred":   y_pred[:200],
            "df":       df,
        }

    return models, metrics


def _show_prediction_page(page_key: str):
    cfg = PAGE_CONFIG[page_key]
    set_page_background(cfg["bg"], cfg["overlay"])
    page_header(cfg["title"], cfg["subtitle"], cfg["accent"])

    try:
        all_models, all_metrics = train_production_models()
        target   = cfg["target"]
        model    = all_models[target]
        metrics  = all_metrics[target]
        df       = metrics["df"]
        loaded   = True
    except Exception as e:
        st.warning(f"⚠️ Could not load data: {e}. Place `production.csv` in `data/`.")
        return

    accent = cfg["accent"]

    # ── Metrics banner ──────────────────────────────────────
    c1, c2, c3, c4 = st.columns(4)
    for col, label, val in [
        (c1, "R² Score",  str(metrics["r2"])),
        (c2, "MAE",       str(metrics["mae"])),
        (c3, "RMSE",      str(metrics["rmse"])),
        (c4, "Train Rows","~22,000"),
    ]:
        with col:
            st.markdown(f"""
            <div style="background:rgba(255,255,255,0.04);
                        border:1px solid {accent}33; border-top:2px solid {accent};
                        border-radius:10px; padding:1rem; text-align:center;">
                <div style="font-size:0.7rem; color:rgba(255,255,255,0.4);
                            text-transform:uppercase; letter-spacing:0.07em;">{label}</div>
                <div style="font-size:1.3rem; font-weight:700; color:{accent};
                            margin-top:4px;">{val}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["🎯 Predictor", "📊 Model Performance", "🔍 Feature Importance"])

    with tab1:
        _predictor_tab(model, metrics, cfg)

    with tab2:
        _performance_tab(metrics, cfg)

    with tab3:
        _importance_tab(metrics, cfg)


def _predictor_tab(model, metrics, cfg):
    accent    = cfg["accent"]
    feat_cols = metrics["features"]
    df        = metrics["df"]

    col_inputs, col_output = st.columns([1, 1], gap="large")

    with col_inputs:
        st.markdown(f"""
        <h3 style="color:{accent}; font-size:1.05rem; font-weight:600; margin-bottom:1rem;">
            ⚙️ Set Input Parameters
        </h3>
        """, unsafe_allow_html=True)

        inputs = {}
        for feat in feat_cols:
            if feat not in df.columns:
                continue
            col_min = float(df[feat].min())
            col_max = float(df[feat].max())
            col_mean= float(df[feat].mean())
            step    = (col_max - col_min) / 100
            inputs[feat] = st.slider(
                f"{feat}", col_min, col_max, col_mean, step,
                key=f"{cfg['target']}_{feat}"
            )

        predict_btn = st.button(
            f"🚀 Predict {cfg['title']}",
            use_container_width=True,
            key=f"btn_{cfg['target']}"
        )

    with col_output:
        st.markdown(f"""
        <h3 style="color:{accent}; font-size:1.05rem; font-weight:600; margin-bottom:1rem;">
            {cfg['icon']} Prediction Result
        </h3>
        """, unsafe_allow_html=True)

        if predict_btn:
            # Build input row
            row = [inputs.get(f, float(df[f].mean())) for f in feat_cols]
            input_df   = pd.DataFrame([row], columns=feat_cols)
            prediction = float(model.predict(input_df)[0])

            y_min = float(df[cfg["target"]].min())
            y_max = float(df[cfg["target"]].max())

            # Gauge
            fig = go.Figure(go.Indicator(
                mode="gauge+number+delta",
                value=prediction,
                delta={"reference": float(df[cfg["target"]].mean()),
                       "valueformat": ".2f"},
                number={"font": {"size": 44, "color": accent}},
                gauge={
                    "axis":    {"range": [y_min, y_max], "tickcolor": "#e2e8f0"},
                    "bar":     {"color": accent, "thickness": 0.28},
                    "bgcolor": "rgba(0,0,0,0)",
                    "steps": [
                        {"range": [y_min, y_min + (y_max-y_min)*0.33],
                         "color": "rgba(255,255,255,0.03)"},
                        {"range": [y_min + (y_max-y_min)*0.33, y_min + (y_max-y_min)*0.66],
                         "color": "rgba(255,255,255,0.05)"},
                        {"range": [y_min + (y_max-y_min)*0.66, y_max],
                         "color": "rgba(255,255,255,0.07)"},
                    ],
                }
            ))
            fig.update_layout(**PLOTLY_THEME, height=310,
                              margin=dict(l=20,r=20,t=20,b=20))
            st.plotly_chart(fig, use_container_width=True)

            st.markdown(f"""
            <div style="text-align:center; background:rgba(255,255,255,0.04);
                        border:1px solid {accent}44; border-radius:10px; padding:0.8rem;">
                <span style="font-size:0.9rem; color:{accent}; font-weight:600;">
                    {cfg['icon']} Predicted {cfg['title']}: {prediction:.3f} {cfg['unit']}
                </span>
            </div>
            """, unsafe_allow_html=True)
        else:
            info_card(
                f"Set the parameters and click <b>Predict {cfg['title']}</b> to see the result.",
                accent=accent
            )


def _performance_tab(metrics, cfg):
    accent = cfg["accent"]
    y_te   = metrics["y_te"]
    y_pred = metrics["y_pred"]

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        # Actual vs Predicted scatter
        fig = px.scatter(
            x=y_te, y=y_pred,
            labels={"x": "Actual", "y": "Predicted"},
            color_discrete_sequence=[accent],
            opacity=0.5
        )
        min_val = min(y_te.min(), y_pred.min())
        max_val = max(y_te.max(), y_pred.max())
        fig.add_shape(type="line", x0=min_val, y0=min_val,
                      x1=max_val, y1=max_val,
                      line=dict(color="white", dash="dash", width=1))
        fig.update_layout(**PLOTLY_THEME, height=380,
                          title="Actual vs Predicted",
                          margin=dict(l=10,r=10,t=40,b=10))
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # Residuals
        residuals = y_te - y_pred
        fig2 = px.histogram(residuals, nbins=40,
                            color_discrete_sequence=[accent],
                            labels={"value": "Residual"})
        fig2.update_layout(**PLOTLY_THEME, height=380,
                           title="Residuals Distribution",
                           margin=dict(l=10,r=10,t=40,b=10))
        st.plotly_chart(fig2, use_container_width=True)


def _importance_tab(metrics, cfg):
    accent    = cfg["accent"]
    feat_cols = metrics["features"]
    df        = metrics["df"]

    from sklearn.ensemble import RandomForestRegressor
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import Pipeline
    from sklearn.model_selection import train_test_split

    X = df[feat_cols]
    y = df[cfg["target"]]
    X_tr, _, y_tr, _ = train_test_split(X, y, test_size=0.2, random_state=42)

    pipe = Pipeline([("scaler", StandardScaler()),
                     ("model", RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1))])
    pipe.fit(X_tr, y_tr)

    imp = pd.Series(
        pipe.named_steps["model"].feature_importances_,
        index=feat_cols
    ).sort_values()

    colors = [accent if v == imp.max() else "rgba(255,255,255,0.25)"
              for v in imp.values]

    fig = go.Figure(go.Bar(
        x=imp.values, y=imp.index,
        orientation="h",
        marker_color=colors
    ))
    fig.update_layout(**PLOTLY_THEME, height=500,
                      title=f"Feature Importance — {cfg['title']}",
                      margin=dict(l=10,r=10,t=40,b=10))
    st.plotly_chart(fig, use_container_width=True)


# ── Individual page entry points ────────────────────────────

# p5_carbon.py compatible show()
def show_carbon():
    _show_prediction_page("carbon")

# p6_water.py compatible show()
def show_water():
    _show_prediction_page("water")

# p7_growth.py compatible show()
def show_growth():
    _show_prediction_page("growth")
