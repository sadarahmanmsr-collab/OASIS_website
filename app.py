import streamlit as st

st.set_page_config(
    page_title="OASIS — Optimized Automated Sensor Integrated System",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* Import Google Font */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Hide default Streamlit elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background-color: #0d1117 !important;
    border-right: 1px solid rgba(255,255,255,0.08) !important;
}
[data-testid="stSidebar"] * {
    color: #e6edf3 !important;
}

/* Main background */
[data-testid="stAppViewContainer"] {
    background-color: #0d1117;
}
[data-testid="block-container"] {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

/* Card style */
.oasis-card {
    background: #161b22;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1rem;
}
.oasis-card-featured {
    background: #0f1520;
    border: 1px solid rgba(64,117,196,0.4);
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1rem;
}

/* Badge styles */
.badge-live {
    background: rgba(25,135,84,0.15);
    color: #3fb27f;
    border: 1px solid rgba(63,178,127,0.3);
    border-radius: 20px;
    padding: 4px 12px;
    font-size: 12px;
    font-weight: 500;
    display: inline-block;
}
.badge-dev {
    background: rgba(255,193,7,0.1);
    color: #FFC107;
    border: 1px solid rgba(255,193,7,0.25);
    border-radius: 20px;
    padding: 4px 12px;
    font-size: 12px;
    font-weight: 500;
    display: inline-block;
}
.badge-rd {
    background: rgba(64,117,196,0.1);
    color: #4075C4;
    border: 1px solid rgba(64,117,196,0.3);
    border-radius: 20px;
    padding: 4px 12px;
    font-size: 12px;
    font-weight: 500;
    display: inline-block;
}

/* Hero */
.hero-section {
    text-align: center;
    padding: 3rem 1rem 2rem;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    margin-bottom: 2rem;
}
.hero-eyebrow {
    display: inline-block;
    background: rgba(64,117,196,0.12);
    border: 1px solid rgba(64,117,196,0.3);
    border-radius: 20px;
    padding: 5px 16px;
    font-size: 12px;
    color: #4075C4;
    letter-spacing: 0.5px;
    margin-bottom: 1.25rem;
}
.hero-title {
    font-size: 2.6rem;
    font-weight: 600;
    color: #e6edf3;
    line-height: 1.2;
    margin-bottom: 1rem;
}
.hero-title span { color: #4075C4; }
.hero-sub {
    font-size: 1.05rem;
    color: #8b949e;
    max-width: 600px;
    margin: 0 auto 1.25rem;
    line-height: 1.7;
}
.hero-tagline {
    font-size: 11px;
    color: #708090;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 0;
}

/* Stat cards */
.stat-card {
    background: #161b22;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 10px;
    padding: 1.25rem;
    text-align: center;
}
.stat-num {
    font-size: 1.7rem;
    font-weight: 600;
    color: #4075C4;
    margin-bottom: 0.25rem;
}
.stat-label {
    font-size: 12px;
    color: #8b949e;
}

/* Section headings */
.section-title {
    font-size: 1.5rem;
    font-weight: 500;
    color: #e6edf3;
    margin-bottom: 0.4rem;
}
.section-sub {
    font-size: 14px;
    color: #8b949e;
    margin-bottom: 1.5rem;
}

/* Process steps */
.process-step {
    background: #161b22;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 10px;
    padding: 1.25rem;
    text-align: center;
    height: 100%;
}
.process-icon {
    font-size: 2rem;
    margin-bottom: 0.75rem;
}
.process-title {
    font-size: 14px;
    font-weight: 500;
    color: #e6edf3;
    margin-bottom: 0.4rem;
}
.process-desc {
    font-size: 12px;
    color: #8b949e;
    line-height: 1.5;
}

/* Team card */
.team-card {
    background: #161b22;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 10px;
    padding: 1.25rem;
    text-align: center;
}
.team-avatar {
    width: 56px;
    height: 56px;
    border-radius: 50%;
    background: rgba(64,117,196,0.15);
    border: 1px solid rgba(64,117,196,0.25);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
    font-weight: 600;
    color: #4075C4;
    margin: 0 auto 0.75rem;
}
.team-name {
    font-size: 14px;
    font-weight: 500;
    color: #e6edf3;
    margin-bottom: 3px;
}
.team-role {
    font-size: 12px;
    color: #4075C4;
    margin-bottom: 3px;
}
.team-dept {
    font-size: 11px;
    color: #708090;
}

/* CTA box */
.cta-box {
    background: #0f1520;
    border: 1px solid rgba(64,117,196,0.25);
    border-radius: 12px;
    padding: 2.5rem;
    text-align: center;
    margin: 1.5rem 0;
}

/* Divider */
.oasis-divider {
    border: none;
    border-top: 1px solid rgba(255,255,255,0.06);
    margin: 2rem 0;
}

/* Flow node */
.flow-node {
    background: #0d1117;
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 8px;
    padding: 10px 14px;
    font-size: 13px;
    color: #8b949e;
    margin-bottom: 4px;
}

/* Collab card */
.collab-card {
    background: #161b22;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 10px;
    padding: 1.25rem;
    height: 100%;
}
.collab-name {
    font-size: 14px;
    font-weight: 500;
    color: #e6edf3;
    margin-bottom: 4px;
}
.collab-title {
    font-size: 12px;
    color: #8b949e;
    margin-bottom: 6px;
    line-height: 1.4;
}
.collab-badge {
    font-size: 10px;
    color: #708090;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 2px 8px;
    border-radius: 4px;
    display: inline-block;
    letter-spacing: 0.3px;
}

/* Tag pill */
.tag-pill {
    display: inline-block;
    font-size: 11px;
    color: #8b949e;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 3px 9px;
    border-radius: 4px;
    margin: 2px;
}

/* Muted text */
.muted { color: #8b949e; font-size: 13px; }
.accent { color: #4075C4; }
</style>
""", unsafe_allow_html=True)


# ── Sidebar Navigation ───────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding: 1rem 0 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.08); margin-bottom: 1rem;">
        <div style="font-size:22px; font-weight:600; color:#e6edf3; letter-spacing:1px;">
            <span style="color:#4075C4;">O</span>ASIS
        </div>
        <div style="font-size:9px; color:#708090; letter-spacing:0.5px; margin-top:3px;">
            OPTIMIZED AUTOMATED SENSOR INTEGRATED SYSTEM
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.page_link("app.py", label="🏠  Home", )
    st.page_link("pages/1_Products.py", label="🛡️  Products")
    st.page_link("pages/2_Technology.py", label="⚙️  Technology")
    st.page_link("pages/3_Impact.py", label="📊  Impact & Market")
    st.page_link("pages/4_About.py", label="👥  About Us")
    st.page_link("pages/5_Blog.py", label="📝  Blog")
    st.page_link("pages/6_Contact.py", label="✉️  Contact")

    st.markdown("<hr style='border-color:rgba(255,255,255,0.06); margin: 1.5rem 0 1rem;'>", unsafe_allow_html=True)
    st.markdown("<div style='font-size:11px; color:#708090;'>BUET Ecosystem · Dhaka, Bangladesh</div>", unsafe_allow_html=True)


# ── Hero ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-section">
    <div class="hero-eyebrow">● Market-Ready · BUET-Engineered · IoT Safety</div>
    <div class="hero-title">Protecting lives before<br><span>danger strikes</span></div>
    <div class="hero-sub">
        OASIS builds autonomous hardware-software systems that detect hazards, eliminate risk,
        and optimize industrial assets — without waiting for human intervention.
    </div>
    <div class="hero-tagline">Detect early. Stay safe.</div>
</div>
""", unsafe_allow_html=True)


# ── Stat Row ─────────────────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
stats = [
    ("1.33B", "Total addressable market"),
    ("100%", "Detection rate — 20+ trials"),
    ("4-Stage", "Automated safety ecosystem"),
    ("BDT 3,300", "Full hardware kit price"),
]
for col, (num, label) in zip([c1, c2, c3, c4], stats):
    with col:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-num">{num}</div>
            <div class="stat-label">{label}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<hr class='oasis-divider'>", unsafe_allow_html=True)


# ── Products Preview ──────────────────────────────────────────────────────────
st.markdown("<div class='section-title'>Our solutions</div>", unsafe_allow_html=True)
st.markdown("<div class='section-sub'>From market-ready safety hardware to next-generation industrial intelligence</div>", unsafe_allow_html=True)

p1, p2, p3 = st.columns(3)

with p1:
    st.markdown("""
    <div class="oasis-card-featured">
        <div style="font-size:10px;color:#708090;text-align:right;margin-bottom:4px;">STAGE 1</div>
        <span class="badge-live">● Available now</span>
        <div style="font-size:15px;font-weight:500;color:#e6edf3;margin:0.75rem 0 0.5rem;">
            VANGuard — Smart Gas Detector
        </div>
        <div class="muted" style="margin-bottom:1rem;">
            Autonomous dual-node system detecting LPG, Methane & Propane — shuts off gas and 
            triggers ventilation without human input.
        </div>
        <div>
            <span class="tag-pill">ESP-NOW wireless</span>
            <span class="tag-pill">Smart solenoid valve</span>
            <span class="tag-pill">Active ventilation</span>
            <span class="tag-pill">BDT 3,300 kit</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with p2:
    st.markdown("""
    <div class="oasis-card">
        <div style="font-size:10px;color:#708090;text-align:right;margin-bottom:4px;">STAGE 2</div>
        <span class="badge-dev">⚙ In development</span>
        <div style="font-size:15px;font-weight:500;color:#e6edf3;margin:0.75rem 0 0.5rem;">
            Industrial Asset Intelligence Suite
        </div>
        <div class="muted" style="margin-bottom:1rem;">
            Real-time edge telemetry for industrial pumps, coolers, chillers & boilers.
            ML predictive maintenance layer actively in development.
        </div>
        <div>
            <span class="tag-pill">Monitoring: ready</span>
            <span class="tag-pill">LSTM: coming</span>
            <span class="tag-pill">Edge computing</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with p3:
    st.markdown("""
    <div class="oasis-card">
        <div style="font-size:10px;color:#708090;text-align:right;margin-bottom:4px;">STAGE 3</div>
        <span class="badge-rd">◈ R&D roadmap</span>
        <div style="font-size:15px;font-weight:500;color:#e6edf3;margin:0.75rem 0 0.5rem;">
            Future Horizon
        </div>
        <div class="muted" style="margin-bottom:1rem;">
            Long-term deep-tech breakthroughs: smart biogas optimization & 
            industrial CO₂ capture — turning factories net-zero.
        </div>
        <div>
            <span class="tag-pill">Automated bio-energy</span>
            <span class="tag-pill">CO₂ capture</span>
            <span class="tag-pill">Net-zero industrial</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr class='oasis-divider'>", unsafe_allow_html=True)


# ── 4-Stage Process ───────────────────────────────────────────────────────────
st.markdown("<div class='section-title'>How VANGuard protects you</div>", unsafe_allow_html=True)
st.markdown("<div class='section-sub'>A 4-stage automated response — no human presence required</div>", unsafe_allow_html=True)

s1, s2, s3, s4 = st.columns(4)
steps = [
    ("📡", "1. Detection", "Smart IoT sensors instantly detect LPG, Methane, or Propane at trace concentrations via the Master node."),
    ("🔔", "2. Smart alarm", "Tiered early-warning alerts — goes beyond standard buzzers with actionable notifications to occupants."),
    ("🔧", "3. Mechanical shut-off", "High-torque servo motor physically closes the gas valve at source — the autonomous first responder."),
    ("💨", "4. Active ventilation", "Exhaust fan relay engages to clear gas and prevent pooling below the Lower Explosive Limit (LEL)."),
]
for col, (icon, title, desc) in zip([s1, s2, s3, s4], steps):
    with col:
        st.markdown(f"""
        <div class="process-step">
            <div class="process-icon">{icon}</div>
            <div class="process-title">{title}</div>
            <div class="process-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<hr class='oasis-divider'>", unsafe_allow_html=True)


# ── Team Preview ──────────────────────────────────────────────────────────────
st.markdown("<div class='section-title'>The team</div>", unsafe_allow_html=True)
st.markdown("<div class='section-sub'>Engineering students from BUET — building solutions that matter</div>", unsafe_allow_html=True)

t1, t2, t3, t4 = st.columns(4)
team = [
    ("OA", "Mohammad Omayer Ahamed", "Founder", "Product & Safety Testing"),
    ("SR", "M Sadat Rahman", "Co-founder", "App & Dashboard Design"),
    ("TH", "Tasnim Al Hossain", "Co-founder", "Head of R&D"),
    ("+1", "Team Member", "Co-founder", "Details coming soon"),
]
for col, (initials, name, role, dept) in zip([t1, t2, t3, t4], team):
    with col:
        st.markdown(f"""
        <div class="team-card">
            <div class="team-avatar">{initials}</div>
            <div class="team-name">{name}</div>
            <div class="team-role">{role}</div>
            <div class="team-dept">{dept}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<hr class='oasis-divider'>", unsafe_allow_html=True)


# ── CTA ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="cta-box">
    <div style="font-size:1.4rem;font-weight:500;color:#e6edf3;margin-bottom:0.5rem;">
        Ready to protect your space?
    </div>
    <div class="muted" style="margin-bottom:1.5rem;">
        Request a demo, download our datasheet, or get in touch. Actively deploying in Dhaka.
    </div>
    <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;">
        <span style="background:rgba(64,117,196,0.1);border:1px solid rgba(64,117,196,0.3);border-radius:8px;padding:8px 18px;font-size:13px;color:#4075C4;">
            📅 Request a demo
        </span>
        <span style="background:rgba(64,117,196,0.1);border:1px solid rgba(64,117,196,0.3);border-radius:8px;padding:8px 18px;font-size:13px;color:#4075C4;">
            📥 Download datasheet
        </span>
        <span style="background:rgba(64,117,196,0.1);border:1px solid rgba(64,117,196,0.3);border-radius:8px;padding:8px 18px;font-size:13px;color:#4075C4;">
            ✉️ oasisnextbd@gmail.com
        </span>
        <span style="background:rgba(64,117,196,0.1);border:1px solid rgba(64,117,196,0.3);border-radius:8px;padding:8px 18px;font-size:13px;color:#4075C4;">
            📞 01795241547
        </span>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align:center;padding:1.5rem 0;border-top:1px solid rgba(255,255,255,0.06);margin-top:1rem;">
    <div style="font-size:13px;color:#8b949e;margin-bottom:4px;">
        OASIS — Optimized Automated Sensor Integrated System
    </div>
    <div style="font-size:12px;color:#708090;">
        CleanTech · IoT Hardware Automation · Industrial Intelligence · Dhaka, Bangladesh
    </div>
    <div style="font-size:11px;color:#708090;margin-top:6px;">© 2025 OASIS. BUET Ecosystem. All rights reserved.</div>
</div>
""", unsafe_allow_html=True)
