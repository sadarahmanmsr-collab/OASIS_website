import streamlit as st

st.set_page_config(page_title="Products — OASIS", page_icon="🛡️", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
#MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
[data-testid="stSidebar"] { background-color: #0d1117 !important; border-right: 1px solid rgba(255,255,255,0.08) !important; }
[data-testid="stSidebar"] * { color: #e6edf3 !important; }
[data-testid="stAppViewContainer"] { background-color: #0d1117; }
[data-testid="block-container"] { padding-top: 1.5rem; }
.badge-live { background:rgba(25,135,84,0.15); color:#3fb27f; border:1px solid rgba(63,178,127,0.3); border-radius:20px; padding:4px 12px; font-size:12px; font-weight:500; display:inline-block; }
.badge-dev { background:rgba(255,193,7,0.1); color:#FFC107; border:1px solid rgba(255,193,7,0.25); border-radius:20px; padding:4px 12px; font-size:12px; font-weight:500; display:inline-block; }
.badge-rd { background:rgba(64,117,196,0.1); color:#4075C4; border:1px solid rgba(64,117,196,0.3); border-radius:20px; padding:4px 12px; font-size:12px; font-weight:500; display:inline-block; }
.badge-ready { background:rgba(25,135,84,0.1); color:#3fb27f; border:1px solid rgba(63,178,127,0.2); border-radius:4px; padding:3px 8px; font-size:11px; display:inline-block; }
.badge-coming { background:rgba(255,193,7,0.1); color:#FFC107; border:1px solid rgba(255,193,7,0.2); border-radius:4px; padding:3px 8px; font-size:11px; display:inline-block; }
.oasis-card { background:#161b22; border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:1.5rem; margin-bottom:1rem; }
.spec-row { display:flex; justify-content:space-between; padding:8px 0; border-bottom:1px solid rgba(255,255,255,0.05); font-size:13px; }
.spec-label { color:#8b949e; }
.spec-value { color:#e6edf3; font-weight:500; }
.tag-pill { display:inline-block; font-size:11px; color:#8b949e; background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.08); padding:3px 9px; border-radius:4px; margin:2px; }
.muted { color:#8b949e; font-size:13px; line-height:1.65; }
.section-title { font-size:1.5rem; font-weight:500; color:#e6edf3; margin-bottom:0.4rem; }
.section-sub { font-size:14px; color:#8b949e; margin-bottom:1.5rem; }
.oasis-divider { border:none; border-top:1px solid rgba(255,255,255,0.06); margin:2rem 0; }
.feature-item { display:flex; gap:10px; align-items:flex-start; margin-bottom:0.85rem; }
.feature-icon { color:#4075C4; font-size:16px; margin-top:1px; flex-shrink:0; }
.feature-text { font-size:13px; color:#8b949e; line-height:1.5; }
.feature-title { font-size:13px; font-weight:500; color:#e6edf3; margin-bottom:2px; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div style="padding:1rem 0 1.5rem;border-bottom:1px solid rgba(255,255,255,0.08);margin-bottom:1rem;">
        <div style="font-size:22px;font-weight:600;color:#e6edf3;letter-spacing:1px;"><span style="color:#4075C4;">O</span>ASIS</div>
        <div style="font-size:9px;color:#708090;letter-spacing:0.5px;margin-top:3px;">OPTIMIZED AUTOMATED SENSOR INTEGRATED SYSTEM</div>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("app.py", label="🏠  Home")
    st.page_link("pages/1_Products.py", label="🛡️  Products")
    st.page_link("pages/2_Technology.py", label="⚙️  Technology")
    st.page_link("pages/3_Impact.py", label="📊  Impact & Market")
    st.page_link("pages/4_About.py", label="👥  About Us")
    st.page_link("pages/5_Blog.py", label="📝  Blog")
    st.page_link("pages/6_Contact.py", label="✉️  Contact")

# Page Header
st.markdown("""
<div style="padding:2rem 0 1rem;border-bottom:1px solid rgba(255,255,255,0.06);margin-bottom:2rem;">
    <div class="section-title" style="font-size:2rem;">Our solutions</div>
    <div class="section-sub" style="font-size:15px;">
        A staged product pipeline built on engineering rigour — from market-ready safety hardware to long-term industrial intelligence.
    </div>
</div>
""", unsafe_allow_html=True)

# ── STAGE 1: VANGuard ─────────────────────────────────────────────────────────
st.markdown("""
<div style="display:flex;align-items:center;gap:12px;margin-bottom:1rem;">
    <span class="badge-live">● Available now</span>
    <span style="font-size:11px;color:#708090;letter-spacing:0.5px;">STAGE 1 · COMMERCIAL PRODUCT</span>
</div>
<div style="font-size:1.5rem;font-weight:500;color:#e6edf3;margin-bottom:0.4rem;">VANGuard — Smart Gas Detector System</div>
<div class="muted" style="margin-bottom:1.5rem;max-width:700px;">
    A dual-node, router-free IoT safety ecosystem that autonomously detects LPG, Methane, and 
    Propane leaks — then shuts off gas valves and triggers active ventilation without any human input. 
    Market-validated with 100% detection across 20+ simulated trials.
</div>
""", unsafe_allow_html=True)

col_left, col_right = st.columns([3, 2])

with col_left:
    st.markdown("<div class='section-title' style='font-size:1rem;margin-bottom:1rem;'>Key features</div>", unsafe_allow_html=True)

    features = [
        ("🌐", "Remote wireless actuation (safety at a distance)", "The Sensing Unit (Master) and Action Unit (Slave) are physically separated — sensor near the leak, valve and fan at a safe distance."),
        ("📡", "Router-free ESP-NOW communication", "Operates on a proprietary ESP-NOW protocol — no Wi-Fi router required. Works even when home networks fail."),
        ("🧠", "Intelligent 'Hush' & safety timer", "Smart alarm logic prevents false-positive fatigue while maintaining true emergency responsiveness."),
        ("📱", "OASIS monitoring app dashboard", "Cloud-connected dashboard for real-time sensor status, thresholds, and emergency alerts at BDT 50/month."),
    ]
    for icon, title, desc in features:
        st.markdown(f"""
        <div class="feature-item">
            <span class="feature-icon">{icon}</span>
            <div>
                <div class="feature-title">{title}</div>
                <div class="feature-text">{desc}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

with col_right:
    st.markdown("<div class='section-title' style='font-size:1rem;margin-bottom:1rem;'>Technical specifications</div>", unsafe_allow_html=True)
    st.markdown('<div class="oasis-card" style="padding:1.25rem;">', unsafe_allow_html=True)
    specs = [
        ("Gas detection", "LPG, Methane, Propane"),
        ("Architecture", "Dual-node Master/Slave"),
        ("Wireless protocol", "ESP-NOW (router-free)"),
        ("Microcontroller", "Arduino-based"),
        ("Mechanical shut-off", "High-torque servo motor"),
        ("Valve type", "Smart solenoid valve"),
        ("Ventilation", "Relay-controlled exhaust fan"),
        ("Detection rate", "100% across 20+ trials"),
        ("Hardware kit", "BDT 3,300"),
        ("SaaS (app)", "BDT 50/month"),
    ]
    for label, value in specs:
        st.markdown(f"""
        <div class="spec-row">
            <span class="spec-label">{label}</span>
            <span class="spec-value">{value}</span>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div style="margin-top:1rem;">
    <div class="section-title" style="font-size:1rem;margin-bottom:0.75rem;">Pricing breakdown</div>
</div>
""", unsafe_allow_html=True)

pr1, pr2, pr3 = st.columns(3)
pricing = [
    ("BDT 2,100", "VANGuard 2.0", "Main detector unit + smart relay + exhaust fan relay"),
    ("BDT 1,200", "VANGuard Smart Valve", "Smart solenoid valve for mechanical gas shut-off"),
    ("BDT 50/mo", "OASIS Monitoring App", "Cloud dashboard, alerts & remote monitoring — monthly SaaS"),
]
for col, (price, name, desc) in zip([pr1, pr2, pr3], pricing):
    with col:
        st.markdown(f"""
        <div class="oasis-card" style="text-align:center;">
            <div style="font-size:1.4rem;font-weight:600;color:#4075C4;margin-bottom:0.25rem;">{price}</div>
            <div style="font-size:14px;font-weight:500;color:#e6edf3;margin-bottom:0.4rem;">{name}</div>
            <div style="font-size:12px;color:#8b949e;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
<div style="margin-top:1rem;">
    <div class="section-title" style="font-size:1rem;margin-bottom:0.75rem;">Target markets</div>
</div>
""", unsafe_allow_html=True)
m1, m2, m3 = st.columns(3)
markets = [
    ("🏠", "Households", "Residential LPG and natural gas users across Bangladesh"),
    ("🍽️", "Commercial kitchens", "Restaurants and food service establishments under regulatory pressure"),
    ("🏢", "Real estate & infra", "Apartment complexes, commercial buildings, and institutional facilities"),
]
for col, (icon, title, desc) in zip([m1, m2, m3], markets):
    with col:
        st.markdown(f"""
        <div class="oasis-card" style="text-align:center;">
            <div style="font-size:2rem;margin-bottom:0.5rem;">{icon}</div>
            <div style="font-size:14px;font-weight:500;color:#e6edf3;margin-bottom:0.3rem;">{title}</div>
            <div style="font-size:12px;color:#8b949e;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<hr class='oasis-divider'>", unsafe_allow_html=True)

# ── STAGE 2: Industrial Suite ─────────────────────────────────────────────────
st.markdown("""
<div style="display:flex;align-items:center;gap:12px;margin-bottom:1rem;">
    <span class="badge-dev">⚙ In development</span>
    <span style="font-size:11px;color:#708090;letter-spacing:0.5px;">STAGE 2 · INDUSTRIAL B2B PRODUCT</span>
</div>
<div style="font-size:1.5rem;font-weight:500;color:#e6edf3;margin-bottom:0.4rem;">Industrial Asset Intelligence Suite</div>
<div class="muted" style="margin-bottom:1.5rem;max-width:700px;">
    Real-time edge telemetry and cloud monitoring for industrial equipment, with an advanced 
    Machine Learning predictive maintenance layer actively under development.
</div>
""", unsafe_allow_html=True)

ia1, ia2 = st.columns(2)
with ia1:
    st.markdown("""
    <div class="oasis-card" style="border-color:rgba(63,178,127,0.25);">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:0.75rem;">
            <span class="badge-ready">✓ Ready now</span>
            <span style="font-size:13px;font-weight:500;color:#e6edf3;">Real-Time Monitoring Unit</span>
        </div>
        <div class="muted" style="margin-bottom:1rem;">
            100% complete and fully functional. Handles edge telemetry, live sensor data streaming, 
            and cloud logging for industrial assets.
        </div>
        <div>
            <span class="tag-pill">Edge telemetry</span>
            <span class="tag-pill">Live sensor streaming</span>
            <span class="tag-pill">Cloud logging</span>
            <span class="tag-pill">GPH Ispat validated</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with ia2:
    st.markdown("""
    <div class="oasis-card" style="border-color:rgba(255,193,7,0.2);">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:0.75rem;">
            <span class="badge-coming">⏳ In development</span>
            <span style="font-size:13px;font-weight:500;color:#e6edf3;">Predictive Maintenance ML Layer</span>
        </div>
        <div class="muted" style="margin-bottom:1rem;">
            Advanced LSTM / Neural Network model being built to forecast asset failure, 
            optimize maintenance cycles, and extend equipment lifespan.
        </div>
        <div>
            <span class="tag-pill">LSTM networks</span>
            <span class="tag-pill">Failure prediction</span>
            <span class="tag-pill">Lifespan optimization</span>
            <span class="tag-pill">Active R&D</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="muted" style="margin:0.5rem 0 0.25rem;">Target equipment:</div>
<div>
    <span class="tag-pill">Industrial pumps</span>
    <span class="tag-pill">Coolers & chillers</span>
    <span class="tag-pill">Boilers</span>
    <span class="tag-pill">Heavy industrial assets</span>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr class='oasis-divider'>", unsafe_allow_html=True)

# ── STAGE 3: Future Horizon ───────────────────────────────────────────────────
st.markdown("""
<div style="display:flex;align-items:center;gap:12px;margin-bottom:1rem;">
    <span class="badge-rd">◈ R&D roadmap</span>
    <span style="font-size:11px;color:#708090;letter-spacing:0.5px;">STAGE 3 · LONG-TERM DEEP-TECH R&D</span>
</div>
<div style="font-size:1.5rem;font-weight:500;color:#e6edf3;margin-bottom:0.4rem;">Future Horizon</div>
<div class="muted" style="margin-bottom:1.5rem;max-width:700px;">
    Our deep-tech sustainability vision. These projects extend OASIS's proven IoT architecture 
    into global-scale environmental and energy challenges.
</div>
""", unsafe_allow_html=True)

fh1, fh2 = st.columns(2)
with fh1:
    st.markdown("""
    <div class="oasis-card">
        <div style="font-size:1.5rem;margin-bottom:0.75rem;">🌿</div>
        <div style="font-size:14px;font-weight:500;color:#e6edf3;margin-bottom:0.4rem;">Automated Bio-Energy Optimization</div>
        <div class="muted">
            Extending our IoT sensor networks and automation architecture to transform 
            passive biogas waste digesters into smart, self-optimizing energy grids — 
            turning organic waste into a managed clean energy source.
        </div>
    </div>
    """, unsafe_allow_html=True)

with fh2:
    st.markdown("""
    <div class="oasis-card">
        <div style="font-size:1.5rem;margin-bottom:0.75rem;">🏭</div>
        <div style="font-size:14px;font-weight:500;color:#e6edf3;margin-bottom:0.4rem;">Industrial Exhaust & CO₂ Mitigation</div>
        <div class="muted">
            Advanced engineered systems to capture CO₂ and hazardous emissions directly 
            from industrial exhausts — retrofitting existing factories to become clean, 
            net-zero operations without rebuilding infrastructure.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div style="background:#0d1117;border:1px solid rgba(64,117,196,0.15);border-radius:8px;padding:1rem 1.25rem;margin-top:0.5rem;">
    <div style="font-size:12px;color:#708090;line-height:1.6;">
        <span style="color:#4075C4;font-weight:500;">Note:</span> Stage 3 projects are long-term R&D roadmap items. 
        They are not commercial offerings and are intentionally separated from our current product pipeline 
        to maintain scientific and business integrity.
    </div>
</div>
""", unsafe_allow_html=True)
