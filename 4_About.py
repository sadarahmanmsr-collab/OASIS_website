import streamlit as st

st.set_page_config(page_title="About Us — OASIS", page_icon="👥", layout="wide")

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
.team-card { background:#161b22; border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:1.5rem; text-align:center; height:100%; }
.team-avatar { width:64px; height:64px; border-radius:50%; background:rgba(64,117,196,0.15); border:1px solid rgba(64,117,196,0.3); display:flex; align-items:center; justify-content:center; font-size:18px; font-weight:600; color:#4075C4; margin:0 auto 0.85rem; }
.advisor-card { background:#0f1520; border:1px solid rgba(64,117,196,0.25); border-radius:12px; padding:1.5rem; }
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
    <div class="section-title" style="font-size:2rem;">About OASIS</div>
    <div class="section-sub" style="font-size:15px;">Engineering students from BUET — building the future of industrial safety and intelligence.</div>
</div>
""", unsafe_allow_html=True)

# Story
st.markdown("""
<div class="oasis-card" style="margin-bottom:2rem;">
    <div style="font-size:1.1rem;font-weight:500;color:#e6edf3;margin-bottom:0.75rem;">Our story</div>
    <div class="muted">
        OASIS — Optimized Automated Sensor Integrated System — was born inside the BUET engineering ecosystem from 
        a simple but urgent question: why do gas explosions still happen when the technology to prevent them exists?<br><br>
        As engineering students, we saw that existing solutions either alarm without acting, or require human presence 
        to respond. We built VANGuard to eliminate that gap — a system that detects, shuts off, and ventilates 
        autonomously, before anyone even wakes up.<br><br>
        From household safety, we're expanding into industrial asset intelligence — using the same core 
        IoT architecture to bring predictive maintenance to Bangladesh's industrial sector. And on the long horizon, 
        we're working on the deep-tech breakthroughs that could decarbonise factories entirely.
    </div>
</div>
""", unsafe_allow_html=True)

# Mission / Vision
mv1, mv2 = st.columns(2)
with mv1:
    st.markdown("""
    <div class="oasis-card">
        <div style="font-size:11px;color:#4075C4;letter-spacing:1px;margin-bottom:0.5rem;">MISSION</div>
        <div style="font-size:14px;color:#e6edf3;line-height:1.65;">
            To make industries and households cleaner, safer, sustainable, and smart through 
            advanced automation, edge computing, and system optimisation.
        </div>
    </div>
    """, unsafe_allow_html=True)
with mv2:
    st.markdown("""
    <div class="oasis-card">
        <div style="font-size:11px;color:#4075C4;letter-spacing:1px;margin-bottom:0.5rem;">VISION</div>
        <div style="font-size:14px;color:#e6edf3;line-height:1.65;">
            A future where no household explosion is preventable, every industrial asset is optimised, 
            and every factory is on a path to net-zero emissions.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr class='oasis-divider'>", unsafe_allow_html=True)

# Founders
st.markdown("<div class='section-title' style='font-size:1.1rem;'>Founders</div>", unsafe_allow_html=True)
st.markdown("<div class='section-sub'>Student engineers from BUET — Team Dibyo Drishty</div>", unsafe_allow_html=True)

t1, t2, t3, t4 = st.columns(4)
team = [
    ("OA", "Mohammad Omayer Ahamed", "Founder", "Product & Safety Testing",
     "Leads product development and hardware validation. Responsible for field testing, sensor reliability trials, and safety protocol engineering."),
    ("SR", "M Sadat Rahman", "Co-founder", "App & Dashboard Design",
     "Designs and develops the OASIS monitoring app and customer dashboard. Responsible for UI/UX and the SaaS product interface."),
    ("TH", "Tasnim Al Hossain", "Co-founder", "Head of R&D",
     "Leads the research and development pipeline — from the industrial monitoring suite to the long-term predictive maintenance ML architecture."),
    ("+1", "Team Member", "Co-founder", "Role pending",
     "Additional team member details to be updated shortly."),
]
for col, (initials, name, role, dept, bio) in zip([t1, t2, t3, t4], team):
    with col:
        st.markdown(f"""
        <div class="team-card">
            <div class="team-avatar">{initials}</div>
            <div style="font-size:14px;font-weight:500;color:#e6edf3;margin-bottom:3px;">{name}</div>
            <div style="font-size:12px;color:#4075C4;margin-bottom:3px;">{role}</div>
            <div style="font-size:11px;color:#708090;margin-bottom:0.75rem;">{dept}</div>
            <div class="muted" style="font-size:12px;">{bio}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<hr class='oasis-divider'>", unsafe_allow_html=True)

# Advisors
st.markdown("<div class='section-title' style='font-size:1.1rem;'>Advisors</div>", unsafe_allow_html=True)
st.markdown("<div class='section-sub'>Academic and industry authority backing OASIS</div>", unsafe_allow_html=True)

adv1, adv2 = st.columns(2)
with adv1:
    st.markdown("""
    <div class="advisor-card">
        <div style="display:flex;align-items:center;gap:14px;margin-bottom:0.75rem;">
            <div style="width:52px;height:52px;border-radius:50%;background:rgba(64,117,196,0.2);border:1px solid rgba(64,117,196,0.3);display:flex;align-items:center;justify-content:center;font-size:16px;font-weight:600;color:#4075C4;flex-shrink:0;">AC</div>
            <div>
                <div style="font-size:14px;font-weight:500;color:#e6edf3;">Dr. Md. Ali Ahammad Shoukat Choudhury</div>
                <div style="font-size:12px;color:#8b949e;">Professor, Department of Chemical Engineering</div>
                <div style="font-size:10px;color:#4075C4;background:rgba(64,117,196,0.1);border:1px solid rgba(64,117,196,0.2);border-radius:3px;padding:2px 7px;display:inline-block;margin-top:4px;">BUET · Faculty Advisor</div>
            </div>
        </div>
        <div class="muted">
            Faculty advisor from the Department of Chemical Engineering at BUET. Provides academic mentorship, 
            technical validation, and institutional backing for OASIS's engineering and research work.
        </div>
    </div>
    """, unsafe_allow_html=True)

with adv2:
    st.markdown("""
    <div class="advisor-card">
        <div style="display:flex;align-items:center;gap:14px;margin-bottom:0.75rem;">
            <div style="width:52px;height:52px;border-radius:50%;background:rgba(64,117,196,0.2);border:1px solid rgba(64,117,196,0.3);display:flex;align-items:center;justify-content:center;font-size:16px;font-weight:600;color:#4075C4;flex-shrink:0;">AH</div>
            <div>
                <div style="font-size:14px;font-weight:500;color:#e6edf3;">Md Anamul Hauque Bhuiyan</div>
                <div style="font-size:12px;color:#8b949e;">Deputy General Manager, PCD</div>
                <div style="font-size:10px;color:#3fb27f;background:rgba(63,178,127,0.1);border:1px solid rgba(63,178,127,0.2);border-radius:3px;padding:2px 7px;display:inline-block;margin-top:4px;">TITAS GAS T&D Co. Ltd · Industry Advisor</div>
            </div>
        </div>
        <div class="muted">
            Senior industry advisor from TITAS GAS Transmission & Distribution. Brings deep domain expertise 
            in gas infrastructure, safety compliance, and commercial deployment at scale in Bangladesh.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr class='oasis-divider'>", unsafe_allow_html=True)

# Collaborators
st.markdown("<div class='section-title' style='font-size:1.1rem;'>Collaborators & ecosystem</div>", unsafe_allow_html=True)

ec1, ec2, ec3 = st.columns(3)
for col, (init, name, type_, desc) in zip([ec1, ec2, ec3], [
    ("BUET", "BUET", "Academic Institution", "Bangladesh University of Engineering and Technology — OASIS's founding academic home. Our engineering rigour is rooted in BUET's standards."),
    ("RISE", "RISE, BUET", "Research Institute", "Research Institute for Sustainable Energy — academic validation partner for our IoT architecture and sensor systems."),
    ("GPH", "GPH Ispat", "Industrial Partner", "Leading steel manufacturer — industrial validation partner for the Asset Intelligence Suite real-time monitoring deployment."),
]):
    with col:
        st.markdown(f"""
        <div class="oasis-card" style="text-align:center;">
            <div style="width:48px;height:48px;border-radius:10px;background:rgba(64,117,196,0.15);border:1px solid rgba(64,117,196,0.2);display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:600;color:#4075C4;margin:0 auto 0.75rem;">{init}</div>
            <div style="font-size:14px;font-weight:500;color:#e6edf3;margin-bottom:3px;">{name}</div>
            <div style="font-size:11px;color:#4075C4;margin-bottom:0.5rem;">{type_}</div>
            <div class="muted">{desc}</div>
        </div>
        """, unsafe_allow_html=True)
