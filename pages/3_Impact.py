import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="Impact & Market — OASIS", page_icon="📊", layout="wide")

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
.stat-card { background:#161b22; border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:1.25rem; text-align:center; }
.stat-num { font-size:1.7rem; font-weight:600; color:#4075C4; margin-bottom:0.25rem; }
.stat-label { font-size:12px; color:#8b949e; }
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
    <div class="section-title" style="font-size:2rem;">Impact & market opportunity</div>
    <div class="section-sub" style="font-size:15px;">The commercial case, the safety gap, and the sustainability vision.</div>
</div>
""", unsafe_allow_html=True)

# Market size
st.markdown("<div class='section-title' style='font-size:1.1rem;'>Market sizing — Bangladesh LPG safety</div>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
for col, (num, label, desc) in zip([c1, c2, c3], [
    ("1.33B", "Total Available Market (TAM)", "4M households using LPG + 2.88M using natural gas nationwide"),
    ("65.75M", "Serviceable Market (SAM)", "7,000–8,000 formal restaurants + 2.5M households in Dhaka"),
    ("157.4K", "Serviceable Obtainable (SOM)", "500–1,000 installs/month · Year 1 capacity: 10,000 installs"),
]):
    with col:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-num">{num}</div>
            <div class="stat-label" style="font-size:13px;font-weight:500;margin-bottom:4px;">{label}</div>
            <div class="stat-label">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<hr class='oasis-divider'>", unsafe_allow_html=True)

# Willingness to pay chart
st.markdown("<div class='section-title' style='font-size:1.1rem;'>Customer survey — willingness to pay</div>", unsafe_allow_html=True)
st.markdown("<div class='section-sub'>Primary research conducted across Dhaka households and restaurants</div>", unsafe_allow_html=True)

fig = go.Figure(go.Bar(
    x=["BDT 1,500–3,000", "BDT 3,000–5,000", "BDT 5,000+"],
    y=[30, 14, 5],
    marker_color=["#4075C4", "#4075C4", "#708090"],
    text=["30", "14", "5"],
    textposition="outside",
    textfont=dict(color="#e6edf3"),
))
fig.update_layout(
    plot_bgcolor="#161b22", paper_bgcolor="#161b22",
    font=dict(color="#8b949e", family="Inter"),
    xaxis=dict(title="Willingness to Pay (BDT)", gridcolor="rgba(255,255,255,0.04)", tickfont=dict(color="#8b949e")),
    yaxis=dict(title="Number of respondents", gridcolor="rgba(255,255,255,0.04)", tickfont=dict(color="#8b949e"), range=[0, 38]),
    height=300, margin=dict(t=20, b=40, l=40, r=20),
    annotations=[dict(
        text="OASIS kit: BDT 3,300 — within the dominant willingness-to-pay range",
        x=0.5, y=1.08, xref="paper", yref="paper",
        showarrow=False, font=dict(size=11, color="#4075C4")
    )]
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("<hr class='oasis-divider'>", unsafe_allow_html=True)

# Why now / Why us
st.markdown("<div class='section-title' style='font-size:1.1rem;'>Why now? Why OASIS?</div>", unsafe_allow_html=True)

wn1, wu1 = st.columns(2)
with wn1:
    st.markdown("<div style='font-size:14px;font-weight:500;color:#e6edf3;margin-bottom:0.75rem;'>Why now</div>", unsafe_allow_html=True)
    reasons_now = [
        ("⚠️", "High-consequence risk + rising awareness", "Gas explosions are headline news. The social pressure to act is at an inflection point."),
        ("🏙️", "Urban density amplifies exposure", "Dhaka's rapid urbanisation puts more LPG users in closer proximity — raising collective risk."),
        ("📋", "Regulatory pressure on restaurants", "Commercial kitchens face increasing compliance requirements around fire and gas safety."),
    ]
    for icon, title, desc in reasons_now:
        st.markdown(f"""
        <div style="display:flex;gap:10px;align-items:flex-start;margin-bottom:0.85rem;">
            <span style="font-size:1.25rem;">{icon}</span>
            <div>
                <div style="font-size:13px;font-weight:500;color:#e6edf3;margin-bottom:2px;">{title}</div>
                <div class="muted">{desc}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

with wu1:
    st.markdown("<div style='font-size:14px;font-weight:500;color:#e6edf3;margin-bottom:0.75rem;'>Why OASIS</div>", unsafe_allow_html=True)
    reasons_us = [
        ("🔧", "Full-stack solution", "Hardware device + installation + monitoring + alerts. Not just a sensor — an ecosystem."),
        ("💰", "Recurring software revenue", "BDT 50/month SaaS creates predictable revenue and customer lock-in beyond the one-time hardware sale."),
        ("🚨", "Built-in emergency workflow", "The system acts — valve closes, fan starts — before any human has to respond."),
    ]
    for icon, title, desc in reasons_us:
        st.markdown(f"""
        <div style="display:flex;gap:10px;align-items:flex-start;margin-bottom:0.85rem;">
            <span style="font-size:1.25rem;">{icon}</span>
            <div>
                <div style="font-size:13px;font-weight:500;color:#e6edf3;margin-bottom:2px;">{title}</div>
                <div class="muted">{desc}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<hr class='oasis-divider'>", unsafe_allow_html=True)

# Revenue model
st.markdown("<div class='section-title' style='font-size:1.1rem;'>Revenue model</div>", unsafe_allow_html=True)
st.markdown("<div class='section-sub'>Hardtech + SaaS hybrid — the modern standard for high-moat ventures</div>", unsafe_allow_html=True)

rm1, rm2 = st.columns(2)
with rm1:
    st.markdown("""
    <div class="oasis-card">
        <div style="font-size:1.5rem;margin-bottom:0.5rem;">💰</div>
        <div style="font-size:14px;font-weight:500;color:#e6edf3;margin-bottom:0.4rem;">One-time hardware revenue</div>
        <div class="muted" style="margin-bottom:0.75rem;">VANGuard 2.0 + Smart Solenoid Valve — BDT 3,300 per installation.</div>
        <div style="font-size:1.2rem;font-weight:600;color:#4075C4;">BDT 3,300 / install</div>
    </div>
    """, unsafe_allow_html=True)
with rm2:
    st.markdown("""
    <div class="oasis-card">
        <div style="font-size:1.5rem;margin-bottom:0.5rem;">🔄</div>
        <div style="font-size:14px;font-weight:500;color:#e6edf3;margin-bottom:0.4rem;">Recurring SaaS revenue</div>
        <div class="muted" style="margin-bottom:0.75rem;">OASIS Monitoring App subscription — cloud dashboard, alerts & remote monitoring.</div>
        <div style="font-size:1.2rem;font-weight:600;color:#4075C4;">BDT 50 / month / user</div>
    </div>
    """, unsafe_allow_html=True)

# Growth phases
st.markdown("<hr class='oasis-divider'>", unsafe_allow_html=True)
st.markdown("<div class='section-title' style='font-size:1.1rem;'>Go-to-market phases</div>", unsafe_allow_html=True)

g1, g2, g3 = st.columns(3)
phases = [
    ("Phase 1", "Day 1–20", "Lead activation", "Direct outreach to survey leads for beta-testing trials."),
    ("Phase 2", "Day 21–40", "Awareness & nurture", "Social media campaigns building trust around the 4-stage mitigation story."),
    ("Phase 3", "Day 41–60", "Conversion & SaaS", "One-time VANGuard 2.0 purchase + onboarding to OASIS monitoring app."),
]
for col, (phase, timeline, title, desc) in zip([g1, g2, g3], phases):
    with col:
        st.markdown(f"""
        <div class="oasis-card">
            <div style="font-size:10px;color:#4075C4;letter-spacing:0.5px;margin-bottom:4px;">{phase} · {timeline}</div>
            <div style="font-size:14px;font-weight:500;color:#e6edf3;margin-bottom:0.4rem;">{title}</div>
            <div class="muted">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<hr class='oasis-divider'>", unsafe_allow_html=True)

# SDG alignment
st.markdown("<div class='section-title' style='font-size:1.1rem;'>Sustainability & SDG alignment</div>", unsafe_allow_html=True)
st.markdown("<div class='section-sub'>OASIS contributes to multiple UN Sustainable Development Goals</div>", unsafe_allow_html=True)

sdg1, sdg2, sdg3 = st.columns(3)
sdgs = [
    ("SDG 3", "Good Health & Well-being", "Preventing LPG explosion injuries and fatalities — directly protecting lives in urban households and commercial kitchens."),
    ("SDG 9", "Industry, Innovation & Infrastructure", "Deploying smart IoT infrastructure for industrial asset optimization and building Bangladesh's industrial intelligence capacity."),
    ("SDG 13", "Climate Action", "Long-term R&D toward CO₂ capture from industrial exhausts and biogas optimization — directly targeting industrial emissions."),
]
for col, (sdg, title, desc) in zip([sdg1, sdg2, sdg3], sdgs):
    with col:
        st.markdown(f"""
        <div class="oasis-card" style="text-align:center;">
            <div style="font-size:11px;color:#4075C4;font-weight:500;letter-spacing:1px;margin-bottom:0.4rem;">{sdg}</div>
            <div style="font-size:13px;font-weight:500;color:#e6edf3;margin-bottom:0.4rem;">{title}</div>
            <div class="muted">{desc}</div>
        </div>
        """, unsafe_allow_html=True)
