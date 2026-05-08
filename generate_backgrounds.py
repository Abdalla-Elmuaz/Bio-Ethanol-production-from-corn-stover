"""
Generate SVG background images for each page of the Bioethanol Streamlit App.
Run this once to create all background files in assets/backgrounds/
"""

import os

backgrounds = {

    # 1. AIM OF THE WORK — Deep green organic/scientific
    "aim.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 900">
  <defs>
    <radialGradient id="bg1" cx="30%" cy="40%" r="80%">
      <stop offset="0%" stop-color="#0a2e1a"/>
      <stop offset="60%" stop-color="#051a0e"/>
      <stop offset="100%" stop-color="#020d07"/>
    </radialGradient>
    <radialGradient id="glow1" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#16a34a" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#16a34a" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="1400" height="900" fill="url(#bg1)"/>
  <!-- Molecule rings -->
  <circle cx="200" cy="200" r="120" fill="none" stroke="#16a34a" stroke-width="0.8" opacity="0.3"/>
  <circle cx="200" cy="200" r="80"  fill="none" stroke="#22c55e" stroke-width="0.5" opacity="0.2"/>
  <circle cx="200" cy="200" r="40"  fill="none" stroke="#4ade80" stroke-width="0.5" opacity="0.15"/>
  <circle cx="200" cy="200" r="8"   fill="#4ade80" opacity="0.6"/>
  <!-- Atom bonds -->
  <line x1="200" y1="200" x2="400" y2="150" stroke="#22c55e" stroke-width="0.8" opacity="0.25"/>
  <line x1="200" y1="200" x2="350" y2="350" stroke="#22c55e" stroke-width="0.8" opacity="0.25"/>
  <line x1="200" y1="200" x2="80"  y2="350" stroke="#22c55e" stroke-width="0.8" opacity="0.2"/>
  <circle cx="400" cy="150" r="12" fill="none" stroke="#4ade80" stroke-width="1" opacity="0.4"/>
  <circle cx="350" cy="350" r="10" fill="none" stroke="#4ade80" stroke-width="1" opacity="0.4"/>
  <circle cx="80"  cy="350" r="8"  fill="none" stroke="#4ade80" stroke-width="1" opacity="0.3"/>
  <!-- DNA-like helix right side -->
  <path d="M1100,0 Q1150,150 1100,300 Q1050,450 1100,600 Q1150,750 1100,900" fill="none" stroke="#16a34a" stroke-width="1.5" opacity="0.2"/>
  <path d="M1150,0 Q1100,150 1150,300 Q1200,450 1150,600 Q1100,750 1150,900" fill="none" stroke="#22c55e" stroke-width="1"   opacity="0.15"/>
  <!-- Cross connections on helix -->
  <line x1="1100" y1="75"  x2="1150" y2="75"  stroke="#4ade80" stroke-width="0.8" opacity="0.3"/>
  <line x1="1100" y1="225" x2="1150" y2="225" stroke="#4ade80" stroke-width="0.8" opacity="0.3"/>
  <line x1="1100" y1="375" x2="1150" y2="375" stroke="#4ade80" stroke-width="0.8" opacity="0.3"/>
  <line x1="1100" y1="525" x2="1150" y2="525" stroke="#4ade80" stroke-width="0.8" opacity="0.3"/>
  <line x1="1100" y1="675" x2="1150" y2="675" stroke="#4ade80" stroke-width="0.8" opacity="0.3"/>
  <line x1="1100" y1="825" x2="1150" y2="825" stroke="#4ade80" stroke-width="0.8" opacity="0.3"/>
  <!-- Glow center -->
  <ellipse cx="700" cy="450" rx="400" ry="300" fill="url(#glow1)"/>
  <!-- Grid dots -->
  <g opacity="0.06" fill="#4ade80">
    <circle cx="600" cy="100" r="2"/><circle cx="700" cy="100" r="2"/><circle cx="800" cy="100" r="2"/>
    <circle cx="600" cy="200" r="2"/><circle cx="700" cy="200" r="2"/><circle cx="800" cy="200" r="2"/>
    <circle cx="600" cy="300" r="2"/><circle cx="700" cy="300" r="2"/><circle cx="800" cy="300" r="2"/>
  </g>
</svg>''',

    # 2. ML OF THE PROJECT — Dark tech / neural network blue
    "ml.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 900">
  <defs>
    <radialGradient id="bg2" cx="60%" cy="50%" r="80%">
      <stop offset="0%" stop-color="#0c1a3a"/>
      <stop offset="70%" stop-color="#060e22"/>
      <stop offset="100%" stop-color="#020510"/>
    </radialGradient>
  </defs>
  <rect width="1400" height="900" fill="url(#bg2)"/>
  <!-- Neural network nodes -->
  <!-- Layer 1 -->
  <circle cx="150" cy="200" r="16" fill="none" stroke="#3b82f6" stroke-width="1.5" opacity="0.6"/>
  <circle cx="150" cy="350" r="16" fill="none" stroke="#3b82f6" stroke-width="1.5" opacity="0.6"/>
  <circle cx="150" cy="500" r="16" fill="none" stroke="#3b82f6" stroke-width="1.5" opacity="0.6"/>
  <circle cx="150" cy="650" r="16" fill="none" stroke="#3b82f6" stroke-width="1.5" opacity="0.6"/>
  <!-- Layer 2 -->
  <circle cx="400" cy="150" r="16" fill="none" stroke="#60a5fa" stroke-width="1.5" opacity="0.5"/>
  <circle cx="400" cy="300" r="16" fill="none" stroke="#60a5fa" stroke-width="1.5" opacity="0.5"/>
  <circle cx="400" cy="450" r="16" fill="none" stroke="#60a5fa" stroke-width="1.5" opacity="0.5"/>
  <circle cx="400" cy="600" r="16" fill="none" stroke="#60a5fa" stroke-width="1.5" opacity="0.5"/>
  <circle cx="400" cy="720" r="16" fill="none" stroke="#60a5fa" stroke-width="1.5" opacity="0.5"/>
  <!-- Layer 3 -->
  <circle cx="650" cy="250" r="16" fill="none" stroke="#93c5fd" stroke-width="1.5" opacity="0.4"/>
  <circle cx="650" cy="420" r="16" fill="none" stroke="#93c5fd" stroke-width="1.5" opacity="0.4"/>
  <circle cx="650" cy="590" r="16" fill="none" stroke="#93c5fd" stroke-width="1.5" opacity="0.4"/>
  <!-- Layer 4 output -->
  <circle cx="900" cy="350" r="20" fill="#1d4ed8" stroke="#3b82f6" stroke-width="2" opacity="0.7"/>
  <circle cx="900" cy="520" r="20" fill="#1d4ed8" stroke="#3b82f6" stroke-width="2" opacity="0.7"/>
  <!-- Connections layer1->layer2 -->
  <g stroke="#3b82f6" stroke-width="0.5" opacity="0.12">
    <line x1="166" y1="200" x2="384" y2="150"/><line x1="166" y1="200" x2="384" y2="300"/>
    <line x1="166" y1="200" x2="384" y2="450"/><line x1="166" y1="200" x2="384" y2="600"/>
    <line x1="166" y1="350" x2="384" y2="150"/><line x1="166" y1="350" x2="384" y2="300"/>
    <line x1="166" y1="350" x2="384" y2="450"/><line x1="166" y1="350" x2="384" y2="600"/>
    <line x1="166" y1="500" x2="384" y2="300"/><line x1="166" y1="500" x2="384" y2="450"/>
    <line x1="166" y1="500" x2="384" y2="600"/><line x1="166" y1="500" x2="384" y2="720"/>
    <line x1="166" y1="650" x2="384" y2="450"/><line x1="166" y1="650" x2="384" y2="600"/>
    <line x1="166" y1="650" x2="384" y2="720"/>
  </g>
  <!-- Connections layer2->layer3 -->
  <g stroke="#60a5fa" stroke-width="0.5" opacity="0.1">
    <line x1="416" y1="150" x2="634" y2="250"/><line x1="416" y1="150" x2="634" y2="420"/>
    <line x1="416" y1="300" x2="634" y2="250"/><line x1="416" y1="300" x2="634" y2="420"/>
    <line x1="416" y1="450" x2="634" y2="250"/><line x1="416" y1="450" x2="634" y2="420"/>
    <line x1="416" y1="450" x2="634" y2="590"/><line x1="416" y1="600" x2="634" y2="420"/>
    <line x1="416" y1="600" x2="634" y2="590"/><line x1="416" y1="720" x2="634" y2="590"/>
  </g>
  <!-- Connections layer3->output -->
  <g stroke="#93c5fd" stroke-width="0.8" opacity="0.2">
    <line x1="666" y1="250" x2="880" y2="350"/><line x1="666" y1="250" x2="880" y2="520"/>
    <line x1="666" y1="420" x2="880" y2="350"/><line x1="666" y1="420" x2="880" y2="520"/>
    <line x1="666" y1="590" x2="880" y2="350"/><line x1="666" y1="590" x2="880" y2="520"/>
  </g>
  <!-- Binary rain right -->
  <g font-family="monospace" font-size="11" fill="#3b82f6" opacity="0.07">
    <text x="1050" y="50">10110</text><text x="1100" y="120">01001</text>
    <text x="1050" y="190">11010</text><text x="1150" y="260">00111</text>
    <text x="1050" y="330">10101</text><text x="1100" y="400">11100</text>
    <text x="1050" y="470">01011</text><text x="1150" y="540">10010</text>
    <text x="1050" y="610">11001</text><text x="1100" y="680">00101</text>
    <text x="1050" y="750">10110</text><text x="1150" y="820">01110</text>
    <text x="1250" y="80">11010</text><text x="1300" y="200">00110</text>
    <text x="1250" y="320">10001</text><text x="1300" y="440">11011</text>
    <text x="1250" y="560">01100</text><text x="1300" y="680">10111</text>
    <text x="1250" y="800">00011</text>
  </g>
</svg>''',

    # 3. ANALYSIS & VISUALIZATION — Data/chart purple-teal
    "analysis.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 900">
  <defs>
    <linearGradient id="bg3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f0a2e"/>
      <stop offset="50%" stop-color="#0a1a2e"/>
      <stop offset="100%" stop-color="#0a2e2a"/>
    </linearGradient>
  </defs>
  <rect width="1400" height="900" fill="url(#bg3)"/>
  <!-- Bar chart silhouette -->
  <rect x="100" y="600" width="60" height="200" fill="#7c3aed" opacity="0.15" rx="4"/>
  <rect x="180" y="500" width="60" height="300" fill="#7c3aed" opacity="0.15" rx="4"/>
  <rect x="260" y="400" width="60" height="400" fill="#8b5cf6" opacity="0.15" rx="4"/>
  <rect x="340" y="550" width="60" height="250" fill="#7c3aed" opacity="0.15" rx="4"/>
  <rect x="420" y="450" width="60" height="350" fill="#8b5cf6" opacity="0.15" rx="4"/>
  <rect x="500" y="350" width="60" height="450" fill="#a78bfa" opacity="0.12" rx="4"/>
  <!-- Line chart overlay -->
  <polyline points="100,620 200,510 320,410 440,500 560,360 680,420 800,310 920,380 1040,290 1160,340 1280,250"
            fill="none" stroke="#14b8a6" stroke-width="2" opacity="0.35"/>
  <polyline points="100,700 200,650 320,580 440,620 560,540 680,590 800,510 920,560 1040,490 1160,530 1280,460"
            fill="none" stroke="#8b5cf6" stroke-width="1.5" opacity="0.25"/>
  <!-- Data points -->
  <g fill="#14b8a6" opacity="0.5">
    <circle cx="100" cy="620" r="4"/><circle cx="200" cy="510" r="4"/>
    <circle cx="320" cy="410" r="4"/><circle cx="440" cy="500" r="4"/>
    <circle cx="560" cy="360" r="4"/><circle cx="680" cy="420" r="4"/>
    <circle cx="800" cy="310" r="4"/><circle cx="920" cy="380" r="4"/>
    <circle cx="1040" cy="290" r="4"/><circle cx="1160" cy="340" r="4"/>
    <circle cx="1280" cy="250" r="4"/>
  </g>
  <!-- Scatter plot top right -->
  <g fill="#a78bfa" opacity="0.2">
    <circle cx="1050" cy="150" r="5"/><circle cx="1100" cy="180" r="7"/>
    <circle cx="1150" cy="130" r="4"/><circle cx="1200" cy="200" r="6"/>
    <circle cx="1250" cy="160" r="8"/><circle cx="1300" cy="140" r="5"/>
    <circle cx="1080" cy="220" r="6"/><circle cx="1180" cy="110" r="4"/>
    <circle cx="1320" cy="190" r="7"/><circle cx="1130" cy="250" r="5"/>
  </g>
  <!-- Grid lines -->
  <g stroke="#7c3aed" stroke-width="0.5" opacity="0.08">
    <line x1="0" y1="200" x2="1400" y2="200"/>
    <line x1="0" y1="400" x2="1400" y2="400"/>
    <line x1="0" y1="600" x2="1400" y2="600"/>
    <line x1="0" y1="800" x2="1400" y2="800"/>
    <line x1="200" y1="0" x2="200" y2="900"/>
    <line x1="400" y1="0" x2="400" y2="900"/>
    <line x1="600" y1="0" x2="600" y2="900"/>
    <line x1="800" y1="0" x2="800" y2="900"/>
    <line x1="1000" y1="0" x2="1000" y2="900"/>
    <line x1="1200" y1="0" x2="1200" y2="900"/>
  </g>
</svg>''',

    # 4. YIELD PREDICTION — Warm amber/orange biomass
    "yield.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 900">
  <defs>
    <radialGradient id="bg4" cx="40%" cy="60%" r="80%">
      <stop offset="0%" stop-color="#2d1200"/>
      <stop offset="60%" stop-color="#1a0a00"/>
      <stop offset="100%" stop-color="#0d0500"/>
    </radialGradient>
    <radialGradient id="glow4" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#f59e0b" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="1400" height="900" fill="url(#bg4)"/>
  <ellipse cx="700" cy="500" rx="500" ry="350" fill="url(#glow4)"/>
  <!-- Flask/beaker silhouette -->
  <path d="M580,100 L580,400 L450,700 L950,700 L820,400 L820,100 Z"
        fill="none" stroke="#f59e0b" stroke-width="1.5" opacity="0.12"/>
  <path d="M580,100 L820,100" stroke="#f59e0b" stroke-width="2" opacity="0.2"/>
  <!-- Liquid inside flask -->
  <path d="M490,580 Q700,520 910,580 L950,700 L450,700 Z"
        fill="#f59e0b" opacity="0.06"/>
  <!-- Bubbles -->
  <circle cx="600" cy="550" r="15" fill="none" stroke="#fbbf24" stroke-width="1" opacity="0.2"/>
  <circle cx="650" cy="500" r="10" fill="none" stroke="#fbbf24" stroke-width="1" opacity="0.15"/>
  <circle cx="700" cy="470" r="18" fill="none" stroke="#fcd34d" stroke-width="1" opacity="0.2"/>
  <circle cx="750" cy="520" r="12" fill="none" stroke="#fbbf24" stroke-width="1" opacity="0.18"/>
  <circle cx="780" cy="560" r="8"  fill="none" stroke="#fbbf24" stroke-width="1" opacity="0.12"/>
  <!-- Fermenter tower left -->
  <rect x="80" y="200" width="120" height="500" rx="60" fill="none" stroke="#f59e0b" stroke-width="1" opacity="0.1"/>
  <line x1="140" y1="300" x2="140" y2="600" stroke="#fbbf24" stroke-width="0.5" stroke-dasharray="5,10" opacity="0.15"/>
  <!-- Temperature curve top right -->
  <path d="M1000,100 Q1050,200 1020,300 Q990,400 1050,500 Q1100,600 1070,700"
        fill="none" stroke="#f59e0b" stroke-width="1.5" opacity="0.2"/>
  <!-- Corn/wheat dots scattered -->
  <g fill="#fbbf24" opacity="0.08">
    <ellipse cx="300" cy="750" rx="30" ry="12"/><ellipse cx="400" cy="800" rx="25" ry="10"/>
    <ellipse cx="1000" cy="780" rx="35" ry="13"/><ellipse cx="1100" cy="750" rx="28" ry="11"/>
    <ellipse cx="1200" cy="800" rx="22" ry="9"/>
  </g>
</svg>''',

    # 5. CARBON EMISSIONS — Dark smoky grey/red industrial
    "carbon.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 900">
  <defs>
    <radialGradient id="bg5" cx="50%" cy="80%" r="80%">
      <stop offset="0%" stop-color="#1a0505"/>
      <stop offset="60%" stop-color="#0d0303"/>
      <stop offset="100%" stop-color="#050101"/>
    </radialGradient>
  </defs>
  <rect width="1400" height="900" fill="url(#bg5)"/>
  <!-- Factory chimneys -->
  <rect x="200" y="500" width="60" height="300" fill="#1f1f1f" opacity="0.6"/>
  <rect x="320" y="450" width="50" height="350" fill="#1f1f1f" opacity="0.6"/>
  <rect x="900" y="520" width="70" height="280" fill="#1f1f1f" opacity="0.6"/>
  <rect x="1020" y="470" width="55" height="330" fill="#1f1f1f" opacity="0.6"/>
  <rect x="1150" y="500" width="65" height="300" fill="#1f1f1f" opacity="0.6"/>
  <!-- Smoke plumes -->
  <path d="M230,500 Q200,400 240,300 Q280,200 230,100"
        fill="none" stroke="#ef4444" stroke-width="30" stroke-linecap="round" opacity="0.05"/>
  <path d="M345,450 Q310,340 350,230 Q390,120 350,20"
        fill="none" stroke="#ef4444" stroke-width="25" stroke-linecap="round" opacity="0.05"/>
  <path d="M935,520 Q900,410 940,300 Q980,190 935,80"
        fill="none" stroke="#ef4444" stroke-width="35" stroke-linecap="round" opacity="0.05"/>
  <path d="M1048,470 Q1010,360 1050,250 Q1090,140 1048,30"
        fill="none" stroke="#ef4444" stroke-width="28" stroke-linecap="round" opacity="0.05"/>
  <!-- CO2 molecule diagrams -->
  <circle cx="700" cy="200" r="30" fill="none" stroke="#ef4444" stroke-width="1.5" opacity="0.2"/>
  <circle cx="620" cy="200" r="22" fill="none" stroke="#fca5a5" stroke-width="1"   opacity="0.15"/>
  <circle cx="780" cy="200" r="22" fill="none" stroke="#fca5a5" stroke-width="1"   opacity="0.15"/>
  <line x1="648" y1="200" x2="670" y2="200" stroke="#ef4444" stroke-width="2" opacity="0.3"/>
  <line x1="730" y1="200" x2="758" y2="200" stroke="#ef4444" stroke-width="2" opacity="0.3"/>
  <text x="696" y="205" font-family="monospace" font-size="12" fill="#ef4444" opacity="0.35" text-anchor="middle">C</text>
  <text x="620" y="205" font-family="monospace" font-size="10" fill="#fca5a5" opacity="0.3" text-anchor="middle">O</text>
  <text x="780" y="205" font-family="monospace" font-size="10" fill="#fca5a5" opacity="0.3" text-anchor="middle">O</text>
  <!-- Rising line graph -->
  <polyline points="100,800 250,720 400,680 550,620 700,550 850,480 1000,390 1150,300 1300,200"
            fill="none" stroke="#ef4444" stroke-width="2" opacity="0.25"/>
  <g fill="#ef4444" opacity="0.3">
    <circle cx="100" cy="800" r="4"/><circle cx="400" cy="680" r="4"/>
    <circle cx="700" cy="550" r="4"/><circle cx="1000" cy="390" r="4"/>
    <circle cx="1300" cy="200" r="4"/>
  </g>
  <!-- Atmosphere haze top -->
  <rect x="0" y="0" width="1400" height="150" fill="#ef4444" opacity="0.03"/>
</svg>''',

    # 6. WATER USAGE — Deep ocean blue
    "water.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 900">
  <defs>
    <linearGradient id="bg6" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#001a2e"/>
      <stop offset="50%" stop-color="#002040"/>
      <stop offset="100%" stop-color="#001428"/>
    </linearGradient>
    <radialGradient id="glw6" cx="50%" cy="60%" r="60%">
      <stop offset="0%" stop-color="#0ea5e9" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#0ea5e9" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="1400" height="900" fill="url(#bg6)"/>
  <ellipse cx="700" cy="600" rx="600" ry="300" fill="url(#glw6)"/>
  <!-- Wave layers -->
  <path d="M0,600 Q175,540 350,600 Q525,660 700,600 Q875,540 1050,600 Q1225,660 1400,600 L1400,900 L0,900 Z"
        fill="#0ea5e9" opacity="0.06"/>
  <path d="M0,650 Q175,590 350,650 Q525,710 700,650 Q875,590 1050,650 Q1225,710 1400,650 L1400,900 L0,900 Z"
        fill="#0ea5e9" opacity="0.05"/>
  <path d="M0,700 Q175,650 350,700 Q525,750 700,700 Q875,650 1050,700 Q1225,750 1400,700 L1400,900 L0,900 Z"
        fill="#38bdf8" opacity="0.04"/>
  <!-- Water drop shapes -->
  <path d="M200,100 Q200,50 230,80 Q260,110 230,160 Q200,190 170,160 Q140,130 170,80 Q200,50 200,100Z"
        fill="none" stroke="#38bdf8" stroke-width="1.5" opacity="0.2"/>
  <path d="M1200,150 Q1200,90 1235,125 Q1270,160 1235,220 Q1200,260 1165,220 Q1130,180 1165,125 Q1200,90 1200,150Z"
        fill="none" stroke="#38bdf8" stroke-width="1" opacity="0.15"/>
  <!-- Ripple circles -->
  <circle cx="700" cy="450" r="80"  fill="none" stroke="#0ea5e9" stroke-width="1" opacity="0.12"/>
  <circle cx="700" cy="450" r="140" fill="none" stroke="#0ea5e9" stroke-width="1" opacity="0.08"/>
  <circle cx="700" cy="450" r="200" fill="none" stroke="#0ea5e9" stroke-width="1" opacity="0.05"/>
  <circle cx="700" cy="450" r="260" fill="none" stroke="#0ea5e9" stroke-width="0.5" opacity="0.04"/>
  <!-- Water molecule -->
  <circle cx="700" cy="300" r="20" fill="none" stroke="#38bdf8" stroke-width="1.5" opacity="0.3"/>
  <circle cx="660" cy="340" r="14" fill="none" stroke="#7dd3fc" stroke-width="1"   opacity="0.25"/>
  <circle cx="740" cy="340" r="14" fill="none" stroke="#7dd3fc" stroke-width="1"   opacity="0.25"/>
  <line x1="682" y1="316" x2="668" y2="328" stroke="#38bdf8" stroke-width="1.5" opacity="0.3"/>
  <line x1="718" y1="316" x2="732" y2="328" stroke="#38bdf8" stroke-width="1.5" opacity="0.3"/>
  <!-- Horizontal flow lines -->
  <g stroke="#0ea5e9" stroke-width="0.5" opacity="0.06">
    <path d="M0,200 Q350,180 700,200 Q1050,220 1400,200"/>
    <path d="M0,350 Q350,330 700,350 Q1050,370 1400,350"/>
    <path d="M0,500 Q350,480 700,500 Q1050,520 1400,500"/>
  </g>
</svg>''',

    # 7. BIOETHANOL GROWTH — Sunrise golden/green growth
    "growth.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 900">
  <defs>
    <linearGradient id="bg7" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0f1a05"/>
      <stop offset="40%" stop-color="#0a1500"/>
      <stop offset="100%" stop-color="#050d00"/>
    </linearGradient>
    <radialGradient id="sun7" cx="50%" cy="55%" r="35%">
      <stop offset="0%" stop-color="#fbbf24" stop-opacity="0.2"/>
      <stop offset="60%" stop-color="#f59e0b" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#f59e0b" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="1400" height="900" fill="url(#bg7)"/>
  <ellipse cx="700" cy="500" rx="400" ry="300" fill="url(#sun7)"/>
  <!-- Growth curve (exponential) -->
  <path d="M100,800 Q300,790 500,750 Q700,700 900,600 Q1100,470 1300,200"
        fill="none" stroke="#84cc16" stroke-width="3" opacity="0.35"/>
  <!-- Area under curve -->
  <path d="M100,800 Q300,790 500,750 Q700,700 900,600 Q1100,470 1300,200 L1300,900 L100,900 Z"
        fill="#84cc16" opacity="0.04"/>
  <!-- Data points on curve -->
  <g fill="#a3e635" opacity="0.4">
    <circle cx="300"  cy="792" r="5"/>
    <circle cx="500"  cy="750" r="5"/>
    <circle cx="700"  cy="700" r="5"/>
    <circle cx="900"  cy="600" r="6"/>
    <circle cx="1100" cy="470" r="6"/>
    <circle cx="1300" cy="200" r="7"/>
  </g>
  <!-- Plant/sprout silhouette -->
  <path d="M700,900 L700,500" stroke="#4ade80" stroke-width="2" opacity="0.15"/>
  <path d="M700,650 Q600,580 550,500 Q620,530 700,600" fill="#16a34a" opacity="0.1"/>
  <path d="M700,600 Q800,530 850,450 Q780,480 700,550" fill="#16a34a" opacity="0.1"/>
  <path d="M700,550 Q620,490 580,410 Q650,440 700,510" fill="#22c55e" opacity="0.08"/>
  <!-- Year markers X axis -->
  <g fill="#84cc16" opacity="0.15" font-family="monospace" font-size="13">
    <text x="280"  y="870">2000</text>
    <text x="480"  y="870">2005</text>
    <text x="680"  y="870">2010</text>
    <text x="880"  y="870">2015</text>
    <text x="1080" y="870">2020</text>
    <text x="1280" y="870">2024</text>
  </g>
  <!-- Arrow up right -->
  <path d="M1280,220 L1320,160 L1340,210" fill="none" stroke="#a3e635" stroke-width="2" opacity="0.3"/>
  <line x1="1320" y1="160" x2="1320" y2="280" stroke="#a3e635" stroke-width="1" stroke-dasharray="5,8" opacity="0.2"/>
</svg>'''
}

os.makedirs("assets/backgrounds", exist_ok=True)

for filename, content in backgrounds.items():
    path = f"assets/backgrounds/{filename}"
    with open(path, "w") as f:
        f.write(content)
    print(f"✅ Created: {path}")

print("\n🎉 All 7 background SVGs generated!")
