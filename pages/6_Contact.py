import streamlit as st

st.set_page_config(page_title="Contact — OASIS", page_icon="✉️", layout="wide")

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
.contact-item { display:flex; align-items:center; gap:12px; padding:12px 0; border-bottom:1px solid rgba(255,255,255,0.05); }
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
    <div class="section-title" style="font-size:2rem;">Get in touch</div>
    <div class="section-sub" style="font-size:15px;">Request a demo, ask about our products, or explore partnership opportunities.</div>
</div>
""", unsafe_allow_html=True)

form_col, info_col = st.columns([3, 2])

with form_col:
    st.markdown("<div class='section-title' style='font-size:1.1rem;margin-bottom:1rem;'>Send us a message</div>", unsafe_allow_html=True)

    inquiry_type = st.selectbox(
        "Inquiry type",
        ["Request a product demo", "Purchase inquiry — VANGuard", "Partnership / B2B inquiry",
         "Investor inquiry", "Download brochure / datasheet", "General question"],
    )

    c1, c2 = st.columns(2)
    with c1:
        name = st.text_input("Full name", placeholder="Your name")
    with c2:
        email = st.text_input("Email address", placeholder="your@email.com")

    phone = st.text_input("Phone number (optional)", placeholder="+880 ...")
    org = st.text_input("Organisation / company (optional)", placeholder="Company or institution")
    message = st.text_area("Message", placeholder="Tell us about your needs or questions...", height=140)

    col_submit, col_dl = st.columns(2)
    with col_submit:
        submitted = st.button("Send message", use_container_width=True, type="primary")
    with col_dl:
        dl = st.button("📥 Download brochure", use_container_width=True)

    if submitted:
        if name and email and message:
            st.success(f"Thank you, {name}! We'll get back to you at {email} within 24 hours.")
        else:
            st.warning("Please fill in your name, email, and message.")

    if dl:
        st.info("Brochure download will be available soon. We'll notify you at your email — please use the contact form above.")

with info_col:
    st.markdown("<div class='section-title' style='font-size:1.1rem;margin-bottom:1rem;'>Contact details</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="oasis-card">
        <div class="contact-item">
            <span style="font-size:1.25rem;">✉️</span>
            <div>
                <div style="font-size:12px;color:#708090;margin-bottom:2px;">Email</div>
                <div style="font-size:13px;color:#4075C4;">oasisnextbd@gmail.com</div>
            </div>
        </div>
        <div class="contact-item">
            <span style="font-size:1.25rem;">📞</span>
            <div>
                <div style="font-size:12px;color:#708090;margin-bottom:2px;">Phone</div>
                <div style="font-size:13px;color:#e6edf3;">01795241547</div>
            </div>
        </div>
        <div class="contact-item" style="border:none;">
            <span style="font-size:1.25rem;">📍</span>
            <div>
                <div style="font-size:12px;color:#708090;margin-bottom:2px;">Location</div>
                <div style="font-size:13px;color:#e6edf3;">Dhaka, Bangladesh</div>
                <div style="font-size:12px;color:#708090;">BUET Ecosystem</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='margin-top:1rem;'></div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title' style='font-size:1rem;margin-bottom:0.75rem;'>What to expect</div>", unsafe_allow_html=True)

    items = [
        ("🎯", "Demo requests", "We'll schedule a live demonstration of VANGuard within 48 hours of your request."),
        ("💼", "B2B / industrial", "For industrial monitoring inquiries, we'll connect you with our technical team directly."),
        ("📊", "Investor inquiries", "Reach out for our pitch deck, financials overview, and a team meeting."),
    ]
    for icon, title, desc in items:
        st.markdown(f"""
        <div style="display:flex;gap:10px;align-items:flex-start;margin-bottom:0.85rem;">
            <span style="font-size:1.1rem;">{icon}</span>
            <div>
                <div style="font-size:13px;font-weight:500;color:#e6edf3;margin-bottom:2px;">{title}</div>
                <div class="muted">{desc}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<hr class='oasis-divider'>", unsafe_allow_html=True)

# Quick action cards
st.markdown("<div class='section-title' style='font-size:1.1rem;margin-bottom:1rem;'>Quick actions</div>", unsafe_allow_html=True)
qa1, qa2, qa3, qa4 = st.columns(4)
quick = [
    ("📅", "Request a demo", "See VANGuard in action — live demonstration in Dhaka"),
    ("📥", "Download datasheet", "Full technical specs and product brochure"),
    ("🤝", "Partnership inquiry", "Industrial monitoring, distribution, or investment"),
    ("📋", "Get a quote", "Pricing for bulk or commercial installation orders"),
]
for col, (icon, title, desc) in zip([qa1, qa2, qa3, qa4], quick):
    with col:
        st.markdown(f"""
        <div class="oasis-card" style="text-align:center;cursor:pointer;">
            <div style="font-size:1.75rem;margin-bottom:0.5rem;">{icon}</div>
            <div style="font-size:13px;font-weight:500;color:#e6edf3;margin-bottom:0.3rem;">{title}</div>
            <div class="muted" style="font-size:12px;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)
