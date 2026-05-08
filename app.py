import streamlit as st
import importlib.util, os, sys

st.set_page_config(
    page_title="Bioethanol ML Dashboard",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Hide default Streamlit page navigation + all branding ───
st.markdown("""
<style>
/* Hide the auto-generated pages nav at top of sidebar */
[data-testid="stSidebarNav"]          { display: none !important; }
[data-testid="stSidebarNavItems"]     { display: none !important; }
[data-testid="collapsedControl"]      { display: none !important; }
div[data-testid="stSidebarNavSeparator"] { display: none !important; }

/* Hide Streamlit top header bar */
header[data-testid="stHeader"]        { display: none !important; }

/* Hide footer & main menu */
#MainMenu, footer                      { visibility: hidden !important; }

/* Remove top padding that header leaves */
.block-container { padding-top: 1rem !important; }
</style>
""", unsafe_allow_html=True)

# ── Dynamic base path ────────────────────────────────────────
BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
PAGES_DIR = os.path.join(BASE_DIR, "pages")
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, PAGES_DIR)

PAGES = {
    "🎯  Aim of the Work":           os.path.join(PAGES_DIR, "p1_aim.py"),
    "🤖  ML of the Project":         os.path.join(PAGES_DIR, "p2_ml.py"),
    "📊  Analysis & Visualization":  os.path.join(PAGES_DIR, "p3_analysis.py"),
    "⚗️  Yield Prediction":           os.path.join(PAGES_DIR, "p4_yield.py"),
    "💨  Carbon Emissions":           os.path.join(PAGES_DIR, "p5_carbon.py"),
    "💧  Water Usage":                os.path.join(PAGES_DIR, "p6_water.py"),
    "📈  Bioethanol Growth":          os.path.join(PAGES_DIR, "p7_growth.py"),
}

# ── Sidebar ──────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding:1.2rem 0 1.5rem 0;
                border-bottom:1px solid rgba(255,255,255,0.08);
                margin-bottom:1.2rem;">
        <div style="font-size:1.6rem; font-weight:700; color:#4ade80;
                    letter-spacing:-0.02em;">
            🌿 BioEthanol
        </div>
        <div style="font-size:0.72rem; color:rgba(255,255,255,0.35);
                    margin-top:3px; letter-spacing:0.07em;">
            ML PRODUCTION DASHBOARD
        </div>
    </div>
    """, unsafe_allow_html=True)

    selected = st.radio(
        "Navigation",
        list(PAGES.keys()),
        label_visibility="collapsed"
    )

    st.markdown("""
    <div style="margin-top: 3rem;
                padding-top: 1rem;
                border-top: 1px solid rgba(255,255,255,0.06);
                font-size: 0.68rem;
                color: rgba(255,255,255,0.2);
                text-align: center;">
        Bioethanol ML Project · 2026<br>
        Random Forest · R² ≈ 1.000
    </div>
    """, unsafe_allow_html=True)

# ── Load & run selected page ─────────────────────────────────
page_file = PAGES[selected]

if not os.path.exists(page_file):
    st.error(f"❌ File not found: `{page_file}`")
    st.stop()

spec   = importlib.util.spec_from_file_location("page", page_file)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
module.show()