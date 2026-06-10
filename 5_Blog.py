import streamlit as st

st.set_page_config(page_title="Blog — OASIS", page_icon="📝", layout="wide")

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
.tag-pill { display:inline-block; font-size:11px; color:#8b949e; background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.08); padding:3px 9px; border-radius:4px; margin:2px; }
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
    <div class="section-title" style="font-size:2rem;">Blog & technical articles</div>
    <div class="section-sub" style="font-size:15px;">Engineering insights, safety research, and product updates from the OASIS team.</div>
</div>
""", unsafe_allow_html=True)

# Featured article
st.markdown("""
<div class="oasis-card" style="border-color:rgba(64,117,196,0.3);margin-bottom:1.5rem;">
    <div style="font-size:10px;color:#4075C4;letter-spacing:0.5px;margin-bottom:6px;">FEATURED · SAFETY TECH · June 2025</div>
    <div style="font-size:1.2rem;font-weight:500;color:#e6edf3;margin-bottom:0.5rem;">
        Why gas detectors that only alarm are not enough — the case for autonomous intervention
    </div>
    <div class="muted" style="margin-bottom:1rem;">
        The fundamental problem with conventional gas detectors is that they outsource the response to 
        a human being. In the time it takes for an alarm to wake someone up, for that person to locate 
        the leak, understand what's happening, and physically shut off the gas — enough LPG can accumulate 
        to exceed the Lower Explosive Limit. This article explores why physical autonomy is the only 
        architecturally sound response to combustible gas hazards...
    </div>
    <div>
        <span class="tag-pill">Safety Tech</span>
        <span class="tag-pill">LPG</span>
        <span class="tag-pill">IoT</span>
        <span class="tag-pill">VANGuard</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Article grid
articles = [
    {
        "category": "INDUSTRIAL IoT",
        "date": "May 2025",
        "title": "Edge computing in industrial environments — why sending everything to the cloud isn't always smart",
        "excerpt": "Industrial sensors generate enormous volumes of data. A naive architecture sends all of it to the cloud for processing — creating latency, bandwidth cost, and single points of failure. OASIS's approach to edge-first architecture...",
        "tags": ["Industrial IoT", "Edge computing", "Architecture"]
    },
    {
        "category": "SUSTAINABILITY R&D",
        "date": "April 2025",
        "title": "From passive digester to smart grid: the case for automated biogas optimization",
        "excerpt": "Most biogas systems in use today are passive installations — waste goes in, some gas comes out, and very little optimisation happens. Applying the same sensor-automation loop we use for safety monitoring to biogas systems could unlock...",
        "tags": ["Sustainability", "Biogas", "R&D Roadmap"]
    },
    {
        "category": "ENGINEERING",
        "date": "March 2025",
        "title": "ESP-NOW vs Wi-Fi for safety-critical IoT — a practical comparison",
        "excerpt": "When we chose ESP-NOW as the wireless protocol for VANGuard, the decision wasn't arbitrary. Router-dependent IoT devices inherit all the reliability problems of the home network. For a safety-critical system...",
        "tags": ["Engineering", "ESP-NOW", "Wireless protocols"]
    },
    {
        "category": "MARKET INSIGHT",
        "date": "February 2025",
        "title": "The LPG safety gap in Bangladesh — what the data actually shows",
        "excerpt": "Bangladesh has over 6.8 million households using LPG or natural gas for cooking. Incidents are underreported, but news archives reveal a steady drumbeat of preventable explosions. This piece analyses the structural reasons why...",
        "tags": ["Market", "Bangladesh", "LPG Safety"]
    },
    {
        "category": "PRODUCT UPDATE",
        "date": "January 2025",
        "title": "VANGuard 2.0 — what changed from the pre-seed prototype",
        "excerpt": "Our first prototype was a proof of concept. VANGuard 2.0 is a product. This post walks through the engineering decisions that changed between versions — from sensor placement to the dual-node architecture to the solenoid valve integration...",
        "tags": ["Product", "VANGuard", "Engineering"]
    },
    {
        "category": "PREDICTIVE MAINTENANCE",
        "date": "December 2024",
        "title": "LSTM networks for industrial asset failure prediction — a primer",
        "excerpt": "Long Short-Term Memory networks are particularly well-suited to time-series sensor data from industrial equipment. Unlike standard threshold alerts that trigger after a failure begins, LSTM models learn the temporal signatures that precede failure...",
        "tags": ["ML", "LSTM", "Predictive maintenance"]
    },
]

col1, col2 = st.columns(2)
for i, article in enumerate(articles):
    col = col1 if i % 2 == 0 else col2
    with col:
        tags_html = "".join([f'<span class="tag-pill">{t}</span>' for t in article["tags"]])
        st.markdown(f"""
        <div class="oasis-card">
            <div style="font-size:10px;color:#4075C4;letter-spacing:0.5px;margin-bottom:6px;">
                {article["category"]} · {article["date"]}
            </div>
            <div style="font-size:14px;font-weight:500;color:#e6edf3;margin-bottom:0.5rem;line-height:1.4;">
                {article["title"]}
            </div>
            <div class="muted" style="margin-bottom:0.75rem;">{article["excerpt"]}</div>
            <div>{tags_html}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<hr class='oasis-divider'>", unsafe_allow_html=True)

# Newsletter signup
st.markdown("""
<div style="background:#0f1520;border:1px solid rgba(64,117,196,0.2);border-radius:12px;padding:2rem;text-align:center;">
    <div style="font-size:1.1rem;font-weight:500;color:#e6edf3;margin-bottom:0.4rem;">Stay updated</div>
    <div class="muted" style="margin-bottom:1rem;">Get notified when we publish new technical articles and product updates.</div>
</div>
""", unsafe_allow_html=True)

col_email, col_btn = st.columns([3, 1])
with col_email:
    st.text_input("", placeholder="Your email address", label_visibility="collapsed")
with col_btn:
    st.button("Subscribe", use_container_width=True)
