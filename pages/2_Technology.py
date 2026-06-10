import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Technology — OASIS", page_icon="⚙️", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
#MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
[data-testid="stSidebar"] { background-color: #0d1117 !important; border-right: 1px solid rgba(255,255,255,0.08) !important; }
[data-testid="stSidebar"] * { color: #e6edf3 !important; }
[data-testid="stAppViewContainer"] { background-color: #0d1117; }
[data-testid="block-container"] { padding-top: 1.5rem; }
.oasis-card { background:#161b22; border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:1.5rem; margin-bottom:1rem; }
.muted { color:#8b949e; font-size:13px; line-height:1.65; }
.section-title { font-size:1.5rem; font-weight:500; color:#e6edf3; margin-bottom:0.4rem; }
.section-sub { font-size:14px; color:#8b949e; margin-bottom:1.5rem; }
.oasis-divider { border:none; border-top:1px solid rgba(255,255,255,0.06); margin:2rem 0; }
.tech-tag { font-size:11px; color:#4075C4; background:rgba(64,117,196,0.1); border:1px solid rgba(64,117,196,0.25); padding:4px 10px; border-radius:4px; display:inline-block; margin:2px; }
.flow-node { background:#0d1117; border:1px solid rgba(255,255,255,0.1); border-radius:8px; padding:10px 14px; font-size:13px; color:#8b949e; margin-bottom:4px; }
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

st.markdown("""
<div style="padding:2rem 0 1rem;border-bottom:1px solid rgba(255,255,255,0.06);margin-bottom:2rem;">
    <div class="section-title" style="font-size:2rem;">Engineering architecture</div>
    <div class="section-sub" style="font-size:15px;">
        How OASIS systems are built — from sensor to cloud.
    </div>
</div>
""", unsafe_allow_html=True)

# Architecture overview
a1, a2 = st.columns([3, 2])
with a1:
    st.markdown("<div class='section-title' style='font-size:1.1rem;'>Dual-node topology</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class="muted" style="margin-bottom:1.25rem;">
        OASIS VANGuard separates the Sensing Unit (Master) from the Action Unit (Slave) — 
        a deliberate architectural decision that places the sensor near the gas source while 
        keeping the valve actuator and fan relay at a safe distance. Communication happens 
        over ESP-NOW, a router-free peer-to-peer wireless protocol with sub-100ms latency.
    </div>
    """, unsafe_allow_html=True)
    tech_tags = ["ESP-NOW protocol", "Arduino microcontroller", "Smart relay network",
                 "Gas sensor array", "High-torque servo motor", "Solenoid valve control",
                 "Edge computing", "Cloud telemetry", "OASIS dashboard app"]
    tags_html = "".join([f'<span class="tech-tag">{t}</span>' for t in tech_tags])
    st.markdown(tags_html, unsafe_allow_html=True)

with a2:
    st.markdown("<div class='section-title' style='font-size:1rem;margin-bottom:0.75rem;'>System data flow</div>", unsafe_allow_html=True)
    flow = [
        ("📡", "Gas sensor network (Master node)"),
        ("↓ ESP-NOW wireless", None),
        ("🔲", "Arduino microcontroller"),
        ("↓ Signal processing", None),
        ("🔧", "Smart relay decision logic"),
        ("↓ Relay trigger", None),
        ("⚙️", "Solenoid valve + fan (Slave node)"),
        ("↓ Event logging", None),
        ("☁️", "Cloud data pipeline"),
        ("↓ Push notification", None),
        ("📱", "OASIS monitoring dashboard"),
    ]
    for item in flow:
        icon, label = item
        if label is None:
            st.markdown(f'<div style="font-size:11px;color:#708090;padding:2px 0 2px 14px;">{icon}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="flow-node">{icon} {label}</div>', unsafe_allow_html=True)

st.markdown("<hr class='oasis-divider'>", unsafe_allow_html=True)

# Reliability chart
st.markdown("<div class='section-title' style='font-size:1.1rem;'>Validation & testing results</div>", unsafe_allow_html=True)
st.markdown("<div class='section-sub'>VANGuard performance across 20+ controlled simulated trials</div>", unsafe_allow_html=True)

fig = go.Figure()
categories = ["Gas detection", "Valve actuation", "Fan relay trigger", "App notification", "False-positive rate"]
values = [100, 100, 100, 98, 2]
colors = ["#4075C4", "#4075C4", "#4075C4", "#4075C4", "#dc3545"]

fig.add_trace(go.Bar(
    x=categories,
    y=values,
    marker_color=colors,
    text=[f"{v}%" for v in values],
    textposition="outside",
    textfont=dict(color="#e6edf3", size=12),
))
fig.update_layout(
    plot_bgcolor="#161b22",
    paper_bgcolor="#161b22",
    font=dict(color="#8b949e", family="Inter"),
    xaxis=dict(gridcolor="rgba(255,255,255,0.05)", tickfont=dict(color="#8b949e")),
    yaxis=dict(gridcolor="rgba(255,255,255,0.05)", tickfont=dict(color="#8b949e"), range=[0, 115]),
    height=320,
    margin=dict(t=20, b=20, l=20, r=20),
    showlegend=False,
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("<hr class='oasis-divider'>", unsafe_allow_html=True)

# Key technical differentiators
st.markdown("<div class='section-title' style='font-size:1.1rem;'>Key technical differentiators</div>", unsafe_allow_html=True)
st.markdown("<div class='section-sub'>What separates OASIS from standard gas detectors</div>", unsafe_allow_html=True)

d1, d2, d3 = st.columns(3)
diffs = [
    ("🌐", "Router-free operation", "Standard IoT devices depend on home Wi-Fi routers. OASIS uses ESP-NOW — a direct device-to-device protocol that works even during power cuts and router failures. Safety cannot depend on internet uptime."),
    ("🔧", "Physical first response", "Most detectors only alarm. OASIS physically actuates — closing the gas valve at the nozzle. The system acts as the first responder, not just a notifier."),
    ("💨", "LEL-aware ventilation", "OASIS calculates and mitigates below the Lower Explosive Limit — preventing the gas concentration from ever reaching explosive thresholds, not just alerting after."),
]
for col, (icon, title, desc) in zip([d1, d2, d3], diffs):
    with col:
        st.markdown(f"""
        <div class="oasis-card">
            <div style="font-size:1.75rem;margin-bottom:0.75rem;">{icon}</div>
            <div style="font-size:14px;font-weight:500;color:#e6edf3;margin-bottom:0.5rem;">{title}</div>
            <div class="muted">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<hr class='oasis-divider'>", unsafe_allow_html=True)

# Industrial monitoring architecture
st.markdown("<div class='section-title' style='font-size:1.1rem;'>Industrial intelligence architecture (Stage 2)</div>", unsafe_allow_html=True)
st.markdown("<div class='section-sub'>How the Asset Intelligence Suite processes industrial data — from sensor to prediction</div>", unsafe_allow_html=True)

ia1, ia2 = st.columns(2)
with ia1:
    st.markdown("""
    <div class="oasis-card">
        <div style="font-size:14px;font-weight:500;color:#e6edf3;margin-bottom:0.75rem;">✅ Real-Time Monitoring (Complete)</div>
        <div class="muted" style="margin-bottom:0.75rem;">Live edge telemetry pipeline — currently operational and field-tested at GPH Ispat.</div>
        <div style="font-size:12px;color:#8b949e;">
            <div style="margin-bottom:4px;">→ Multi-sensor array on industrial assets</div>
            <div style="margin-bottom:4px;">→ Edge node data aggregation</div>
            <div style="margin-bottom:4px;">→ Real-time cloud streaming</div>
            <div style="margin-bottom:4px;">→ Live dashboard & alert system</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with ia2:
    st.markdown("""
    <div class="oasis-card" style="border-color:rgba(255,193,7,0.2);">
        <div style="font-size:14px;font-weight:500;color:#e6edf3;margin-bottom:0.75rem;">⏳ Predictive ML Layer (In Development)</div>
        <div class="muted" style="margin-bottom:0.75rem;">LSTM neural network model being trained on historical sensor telemetry to forecast failure.</div>
        <div style="font-size:12px;color:#8b949e;">
            <div style="margin-bottom:4px;">→ LSTM/Neural Net model training</div>
            <div style="margin-bottom:4px;">→ Time-series anomaly detection</div>
            <div style="margin-bottom:4px;">→ Failure probability scoring</div>
            <div style="margin-bottom:4px;">→ Maintenance scheduling engine</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Validation partners
st.markdown("<hr class='oasis-divider'>", unsafe_allow_html=True)
st.markdown("<div class='section-title' style='font-size:1.1rem;'>Academic & industrial validation</div>", unsafe_allow_html=True)

v1, v2 = st.columns(2)
with v1:
    st.markdown("""
    <div class="oasis-card">
        <div style="font-size:14px;font-weight:500;color:#e6edf3;margin-bottom:0.4rem;">RISE, BUET</div>
        <div style="font-size:10px;color:#4075C4;background:rgba(64,117,196,0.1);border:1px solid rgba(64,117,196,0.2);border-radius:3px;padding:2px 7px;display:inline-block;margin-bottom:0.6rem;">Academic Collaboration</div>
        <div class="muted">Research Institute for Sustainable Energy at BUET — provides academic validation, technical review, and research infrastructure backing for OASIS engineering.</div>
    </div>
    """, unsafe_allow_html=True)
with v2:
    st.markdown("""
    <div class="oasis-card">
        <div style="font-size:14px;font-weight:500;color:#e6edf3;margin-bottom:0.4rem;">GPH Ispat</div>
        <div style="font-size:10px;color:#3fb27f;background:rgba(63,178,127,0.1);border:1px solid rgba(63,178,127,0.2);border-radius:3px;padding:2px 7px;display:inline-block;margin-bottom:0.6rem;">Industrial Partner</div>
        <div class="muted">Industrial validation partner for the Asset Intelligence monitoring suite. Real-world deployment and field testing on heavy industrial equipment.</div>
    </div>
    """, unsafe_allow_html=True)
