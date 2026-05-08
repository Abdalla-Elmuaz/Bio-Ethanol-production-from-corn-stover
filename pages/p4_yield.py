"""
Page 4 — Yield Prediction (Dataset 1)
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import set_page_background, page_header, info_card

PLOTLY_THEME = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="#e2e8f0", family="Exo 2"),
)

@st.cache_resource
def train_yield_model():
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import r2_score, mean_absolute_error

    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(base, "data", "fermentation.csv")
    df = pd.read_csv(path)

    X = df.drop("Yield", axis=1).select_dtypes(include="number")
    y = df["Yield"]
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("model",  RandomForestRegressor(n_estimators=200, random_state=42, n_jobs=-1))
    ])
    pipe.fit(X_tr, y_tr)

    y_pred = pipe.predict(X_te)
    metrics = {
        "r2":  round(r2_score(y_te, y_pred), 4),
        "mae": round(mean_absolute_error(y_te, y_pred), 4),
        "features": list(X.columns)
    }
    return pipe, metrics


def show():
    set_page_background("yield.svg", overlay_opacity=0.80)
    page_header(
        "Yield Prediction",
        "Predict ethanol fermentation yield from process parameters",
        accent_color="#fbbf24"
    )

    try:
        model, metrics = train_yield_model()
        model_loaded = True
    except Exception as e:
        model_loaded = False
        st.warning(f"⚠️ Could not load model: {e}. Place `fermentation.csv` in `data/`.")

    # ── Model metrics banner ────────────────────────────────
    if model_loaded:
        c1, c2, c3, c4 = st.columns(4)
        for col, label, val, color in [
            (c1, "Model",     "Random Forest",    "#fbbf24"),
            (c2, "R² Score",  str(metrics["r2"]), "#fbbf24"),
            (c3, "MAE",       str(metrics["mae"]), "#fb923c"),
            (c4, "Features",  str(len(metrics["features"])), "#f59e0b"),
        ]:
            with col:
                st.markdown(f"""
                <div style="background:rgba(255,255,255,0.04);
                            border:1px solid {color}33; border-top:2px solid {color};
                            border-radius:10px; padding:1rem; text-align:center;">
                    <div style="font-size:0.7rem; color:rgba(255,255,255,0.4);
                                text-transform:uppercase; letter-spacing:0.07em;">{label}</div>
                    <div style="font-size:1.3rem; font-weight:700; color:{color};
                                margin-top:4px;">{val}</div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Input form ──────────────────────────────────────────
    col_form, col_result = st.columns([1, 1], gap="large")

    with col_form:
        st.markdown("""
        <h3 style="color:#fcd34d; font-size:1.1rem; font-weight:600; margin-bottom:1rem;">
            ⚙️ Set Fermentation Parameters
        </h3>
        """, unsafe_allow_html=True)

        temp      = st.slider("🌡️ Temperature (°C)",         28.0, 40.0, 34.0, 0.5)
        ph        = st.slider("⚗️ pH",                        4.0,  6.0,  5.0, 0.1)
        time      = st.slider("⏱️ Fermentation Time (hrs)",   24.0, 96.0, 48.0, 1.0)
        substrate = st.slider("🧪 Substrate Concentration",   50.0, 300.0, 150.0, 5.0)
        enzyme    = st.slider("🔬 Enzyme Dose",                0.5,  5.0,  2.0, 0.1)
        inoculum  = st.slider("🦠 Inoculum Size",             1.0,  10.0, 5.0, 0.5)
        agitation = st.slider("🌀 Agitation Speed (rpm)",     50.0, 300.0, 150.0, 10.0)

        predict_btn = st.button("🚀 Predict Yield", use_container_width=True)

    with col_result:
        st.markdown("""
        <h3 style="color:#fcd34d; font-size:1.1rem; font-weight:600; margin-bottom:1rem;">
            📊 Prediction Result
        </h3>
        """, unsafe_allow_html=True)

        if predict_btn and model_loaded:
            input_df = pd.DataFrame([[temp, ph, time, substrate, enzyme, inoculum, agitation]],
                                    columns=metrics["features"])
            prediction = model.predict(input_df)[0]
            prediction = float(np.clip(prediction, 10, 100))

            # Gauge chart
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=prediction,
                number={"suffix": "%", "font": {"size": 48, "color": "#fbbf24"}},
                gauge={
                    "axis":  {"range": [0, 100], "tickcolor": "#e2e8f0"},
                    "bar":   {"color": "#f59e0b", "thickness": 0.3},
                    "bgcolor": "rgba(0,0,0,0)",
                    "steps": [
                        {"range": [0,  40],  "color": "rgba(239,68,68,0.15)"},
                        {"range": [40, 70],  "color": "rgba(251,191,36,0.12)"},
                        {"range": [70, 100], "color": "rgba(74,222,128,0.12)"},
                    ],
                    "threshold": {
                        "line":  {"color": "#4ade80", "width": 3},
                        "thickness": 0.75,
                        "value": 70
                    }
                }
            ))
            fig.update_layout(**PLOTLY_THEME, height=320,
                              margin=dict(l=20,r=20,t=20,b=20))
            st.plotly_chart(fig, use_container_width=True)

            # Quality label
            if prediction >= 70:
                quality, color, icon = "High Yield", "#4ade80", "✅"
            elif prediction >= 40:
                quality, color, icon = "Moderate Yield", "#fbbf24", "⚠️"
            else:
                quality, color, icon = "Low Yield", "#ef4444", "❌"

            st.markdown(f"""
            <div style="text-align:center;
                        background:rgba(255,255,255,0.04);
                        border:1px solid {color}44;
                        border-radius:10px; padding:1rem;">
                <span style="font-size:1.5rem;">{icon}</span>
                <span style="font-size:1.1rem; font-weight:600;
                             color:{color}; margin-left:0.5rem;">{quality}</span>
                <br>
                <span style="font-size:0.82rem; color:rgba(255,255,255,0.45);">
                    Predicted Yield: <b style="color:{color};">{prediction:.2f}%</b>
                </span>
            </div>
            """, unsafe_allow_html=True)

        elif not predict_btn:
            info_card("""
            Adjust the fermentation parameters on the left and click
            <b>Predict Yield</b> to get the model's prediction.<br><br>
            The gauge will show the predicted ethanol yield percentage
            with a quality classification: Low / Moderate / High.
            """, accent="#fbbf24")

        # Feature importance mini chart
        if model_loaded:
            st.markdown("<br>", unsafe_allow_html=True)
            rf_model = model.named_steps["model"]
            imp = pd.Series(rf_model.feature_importances_,
                            index=metrics["features"]).sort_values()
            fig2 = go.Figure(go.Bar(
                x=imp.values, y=imp.index,
                orientation="h",
                marker_color=["#f59e0b" if v == imp.max() else "#78716c"
                              for v in imp.values]
            ))
            fig2.update_layout(**PLOTLY_THEME, height=280,
                               title="Feature Importance",
                               margin=dict(l=10,r=10,t=35,b=10))
            st.plotly_chart(fig2, use_container_width=True)
