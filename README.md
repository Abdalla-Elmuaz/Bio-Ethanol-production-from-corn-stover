# 🌿 Bioethanol ML Dashboard

## Project Structure
```
bioethanol_app/
├── app.py                          ← Main entry point
├── utils.py                        ← Shared helpers (backgrounds, styling)
├── generate_backgrounds.py         ← Run once to generate SVG backgrounds
├── requirements.txt
├── data/
│   ├── fermentation.csv            ← Dataset 1 (BioEthanol_Production_5000rows)
│   └── production.csv              ← Dataset 2 (bioethanol_growth_prediction)
├── assets/
│   └── backgrounds/                ← 7 SVG background files (auto-generated)
│       ├── aim.svg
│       ├── ml.svg
│       ├── analysis.svg
│       ├── yield.svg
│       ├── carbon.svg
│       ├── water.svg
│       └── growth.svg
└── pages/
    ├── p1_aim.py
    ├── p2_ml.py
    ├── p3_analysis.py
    ├── p4_yield.py
    ├── p5_carbon.py
    ├── p6_water.py
    ├── p7_growth.py
    └── _production_pages.py        ← Shared template for pages 5-7
```

## Setup (Spyder / Anaconda)

### Step 1 — Install dependencies
Open Anaconda Prompt and run:
```
pip install streamlit plotly scikit-learn pandas numpy
```

### Step 2 — Add your CSV files
Copy your two datasets into the `data/` folder:
- `BioEthanol_Production_5000rows-1.csv`  →  rename to  `fermentation.csv`
- `bioethanol_growth_prediction_dataset__2___1_.csv`  →  rename to  `production.csv`

### Step 3 — Generate backgrounds (already done)
```
cd bioethanol_app
python generate_backgrounds.py
```

### Step 4 — Run the app
In Anaconda Prompt:
```
cd path/to/bioethanol_app
streamlit run app.py
```
Then open http://localhost:8501 in your browser.

### Running from Spyder
In the Spyder IPython console:
```python
import subprocess
subprocess.Popen(["streamlit", "run", "app.py"])
```
