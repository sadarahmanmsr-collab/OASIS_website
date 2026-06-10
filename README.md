# OASIS Website

**Optimized Automated Sensor Integrated System**  
*Protecting lives before danger strikes*

A multi-page Streamlit website for OASIS — a CleanTech / IoT startup from the BUET ecosystem.

---

## Pages

| Page | File |
|------|------|
| Home | `app.py` |
| Products | `pages/1_Products.py` |
| Technology | `pages/2_Technology.py` |
| Impact & Market | `pages/3_Impact.py` |
| About Us | `pages/4_About.py` |
| Blog | `pages/5_Blog.py` |
| Contact | `pages/6_Contact.py` |

---

## Local setup

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/oasis-website.git
cd oasis-website

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run locally
streamlit run app.py
```

---

## Deploy on Streamlit Community Cloud (free shareable link)

1. Push this repo to GitHub (see instructions below)
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click **New app**
5. Select your repo → Branch: `main` → Main file: `app.py`
6. Click **Deploy** — you'll get a public URL like:  
   `https://your-app-name.streamlit.app`

---

## Push to GitHub

```bash
# Inside the project folder:
git init
git add .
git commit -m "Initial OASIS website"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/oasis-website.git
git push -u origin main
```

---

## Tech stack

- **Framework:** Streamlit
- **Charts:** Plotly
- **Styling:** Custom CSS injected via `st.markdown`
- **Theme:** Dark mode — configured in `.streamlit/config.toml`

---

## Contact

- Email: oasisnextbd@gmail.com  
- Phone: 01795241547  
- Location: Dhaka, Bangladesh · BUET Ecosystem
