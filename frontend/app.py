import os
from dotenv import load_dotenv
import streamlit as st
import streamlit.components.v1 as components
import webbrowser
import sys
from pathlib import Path


load_dotenv()

whatsapp_number = os.getenv('PHONE_NUMBER')

# Page config
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# Custom CSS
st.markdown("""
    <style>
    div[data-testid="stSidebarNav"],
    div[data-testid="stSidebarNavItems"],
    ul[data-testid="stSidebarNavItems"],
    nav[data-testid="stSidebarNav"] {
        display: none !important;
    }

    /* Top right corner buttons */
    .top-right-buttons {
        position: fixed;
        top: 10px;
        right: 10px;
        display: flex;
        gap: 10px;
        z-index: 1000;
    }
    .top-right-btn {
        padding: 8px 15px;
        border-radius: 5px;
        font-weight: bold;
        text-decoration: none;
        font-size: 14px;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 5px;
    }
    .btn-login {
        background-color: #e94560;
        color: white;
    }
    .btn-register {
        background-color: #16213e;
        color: white;
        border: 1px solid #e94560;
    }
    .btn-demo {
        background-color: #f9c74f;
        color: #1a1a2e;
    }
    .top-right-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    .main {
        background-color: #1a1a2e;
        color: white;
    }
    .stApp {
        background-color: #1a1a2e;
    }
    .sidebar .sidebar-content {
        background-color: #16213e;
        color: white;
    }
    .sport-card {
        background-color: #0f3460;
        border-radius: 10px;
        padding: 10px;
        margin: 5px 0;
    }
    .sport-card:hover {
        background-color: #1a3a6a;
        cursor: pointer;
    }
    .match-row {
        display: flex;
        align-items: center;
        padding: 10px;
        border-bottom: 1px solid #2d4059;
        background-color: #16213e;
        margin: 5px 0;
        border-radius: 5px;
    }
    .match-row > div:first-child {
        flex: 1;
        text-align: left;
        padding: 5px 10px;
    }
    .odds-cell {
        text-align: center;
        padding: 8px 12px;
        margin: 0 5px;
        background-color: #2d4059;
        border-radius: 5px;
        min-width: 70px;
        font-weight: 500;
    }
    .header {
        background-color: #16213e;
        padding: 10px 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .nav-links {
        display: flex;
        gap: 20px;
    }
    .nav-link {
        color: white;
        text-decoration: none;
        font-weight: bold;
    }
    .sports-tabs {
        display: flex;
        overflow-x: auto;
        gap: 10px;
        padding: 10px 0;
        margin-bottom: 20px;
    }
    .sport-tab {
        padding: 5px 15px;
        background-color: #0f3460;
        color: #ffffff;
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 15px;
        white-space: nowrap;
        font-weight: 600;
        cursor: pointer;
    }
    .sport-tab:hover {
        background-color: #173f70;
        border-color: rgba(255, 255, 255, 0.35);
    }
    .sidebar-link {
        display: block;
        color: rgba(255, 255, 255, 0.92);
        text-decoration: none;
        padding: 6px 8px;
        border-radius: 8px;
        line-height: 1.2;
    }
    .sidebar-link:hover {
        background: rgba(255, 255, 255, 0.08);
        color: #ffffff;
    }
    .sidebar-link.section {
        font-weight: 700;
        padding-top: 10px;
        padding-bottom: 6px;
    }
    .game-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
        gap: 15px;
        margin-top: 20px;
    }
    .game-card {
        background-color: #0f3460;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
    }
    .whatsapp-float {
        position: fixed;
        bottom: 30px;
        right: 30px;
        background-color: #25D366;
        color: white;
        border-radius: 50%;
        width: 60px;
        height: 60px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 30px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.3);
        z-index: 100;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="header">
        <h1 style="margin: 0;">
            <a href="/Login" target="_top" style="color: white; text-decoration: none;">PLAYZONE9</a>
        </h1>
        <div class="nav-links">
            <a href="/Login" target="_top" class="nav-link">HOME</a>
            <a href="/Login" target="_top" class="nav-link">CRICKET</a>
            <a href="/Login" target="_top" class="nav-link">TENNIS</a>
            <a href="/Login" target="_top" class="nav-link">FOOTBALL</a>
            <a href="/Login" target="_top" class="nav-link">TABLE TENNIS</a>
            <a href="/Login" target="_top" class="nav-link">BACCARAT</a>
            <a href="/Login" target="_top" class="nav-link">TEENPATTI</a>
            <a href="/Login" target="_top" class="nav-link">POKER</a>
            <a href="/Login" target="_top" class="nav-link">LUCKY 7</a>
            <a href="/Login" target="_top" class="nav-link">CRASH</a>
         </div>
         <div>
            <a href="/Login" target="_top" style="background: #0f3460; color: white; border: none; padding: 5px 15px; border-radius: 5px; margin: 0 5px; cursor: pointer; display: inline-block; text-decoration: none;">Demo</a>
            <a href="/Login" target="_top" style="background: #e94560; color: white; border: none; padding: 5px 15px; border-radius: 5px; margin: 0 5px; cursor: pointer; display: inline-block; text-decoration: none;">Login</a>
            <a href="/Login" target="_top" style="background: #4CAF50; color: white; border: none; padding: 5px 15px; border-radius: 5px; margin: 0 5px; cursor: pointer; display: inline-block; text-decoration: none;">Register</a>
         </div>
     </div>
""", unsafe_allow_html=True)

# Marquee
st.markdown("""
    <div style="background: #e94560; color: white; padding: 5px 0; margin-bottom: 20px;">
        <marquee>
            🎉 Welcome to PLAYZONE9 - Your Ultimate Gaming Destination! Get 100% Welcome Bonus on First Deposit! 🎉
        </marquee>
    </div>
""", unsafe_allow_html=True)


st.markdown("""
    <style>
    .top-right-buttons {
        position: fixed;
        top: 10px;
        right: 10px;
        display: flex;
        gap: 10px;
        z-index: 1000;
    }
    .login-btn {
        background-color: #e94560;
        color: white;
        border: none;
        padding: 8px 15px;
        border-radius: 5px;
        cursor: pointer;
        display: flex;
        align-items: center;
        gap: 5px;
        text-decoration: none;
    }
    </style>
    <div class="top-right-buttons">
        <a class="login-btn" href="/Login" target="_top">
            <i class="fas fa-sign-in-alt"></i> Login
        </a>
        <a href="/Login" target="_top" class="top-right-btn btn-register">
            <i class="fas fa-user-plus"></i> Register
        </a>
        <a href="/Login" target="_top" class="top-right-btn btn-demo">
            <i class="fas fa-play-circle"></i> Demo
        </a>
    </div>
""", unsafe_allow_html=True)

# Add Font Awesome for icons
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">', unsafe_allow_html=True)

# Initialize session state for login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False


# Main content
col1, col2 = st.columns([1, 4])

# Sidebar
with col1:
    st.sidebar.title("🎮 PLAYZONE9")
        
    st.sidebar.markdown('<a class="sidebar-link section" href="/Login" target="_top">Racing Sports</a>', unsafe_allow_html=True)
    st.sidebar.markdown('<a class="sidebar-link" href="/Login" target="_top">Horse Racing</a>', unsafe_allow_html=True)
    st.sidebar.markdown('<a class="sidebar-link" href="/Login" target="_top">Greyhound Racing</a>', unsafe_allow_html=True)
    
    st.sidebar.markdown('<a class="sidebar-link section" href="/Login" target="_top">Others</a>', unsafe_allow_html=True)
    st.sidebar.markdown('<a class="sidebar-link" href="/Login" target="_top">Our Premium Casino</a>', unsafe_allow_html=True)
    st.sidebar.markdown('<a class="sidebar-link" href="/Login" target="_top">Our Virtual</a>', unsafe_allow_html=True)
    st.sidebar.markdown('<a class="sidebar-link" href="/Login" target="_top">Tembo</a>', unsafe_allow_html=True)
    st.sidebar.markdown('<a class="sidebar-link" href="/Login" target="_top">Live Casino</a>', unsafe_allow_html=True)
    st.sidebar.markdown('<a class="sidebar-link" href="/Login" target="_top">Slot Game</a>', unsafe_allow_html=True)
    st.sidebar.markdown('<a class="sidebar-link" href="/Login" target="_top">Fantasy Game</a>', unsafe_allow_html=True)
    
    st.sidebar.markdown('<a class="sidebar-link section" href="/Login" target="_top">All Sports</a>', unsafe_allow_html=True)
    sports = [
        "Politics", "Cricket", "Football", "Tennis", "Table Tennis", "Badminton", 
        "Esoccer", "Basketball", "Volleyball", "Snooker", "Ice Hockey", "FGames", 
        "Futsal", "Handball", "Kabaddi", "Golf", "Rugby League", "Boxing", 
        "Beach Volleyball", "Mixed Martial Arts"
    ]
    for sport in sports:
        st.sidebar.markdown(
            f'<a class="sidebar-link" href="/Login" target="_top">{sport}</a>',
            unsafe_allow_html=True,
        )

# Main content
with col2:
    # Sports Tabs
    st.markdown("""
        <div class="sports-tabs">
            <div class="sport-tab">Cricket</div>
            <div class="sport-tab">Football</div>
            <div class="sport-tab">Tennis</div>
            <div class="sport-tab">Table Tennis</div>
            <div class="sport-tab">Esoccer</div>
            <div class="sport-tab">Horse Racing</div>
            <div class="sport-tab">Greyhound Racing</div>
            <div class="sport-tab">Basketball</div>
            <div class="sport-tab">Wrestling</div>
            <div class="sport-tab">Volleyball</div>
            <div class="sport-tab">Badminton</div>
            <div class="sport-tab">Snooker</div>
            <div class="sport-tab">Darts</div>
            <div class="sport-tab">Boxing</div>
            <div class="sport-tab">Mixed Martial Arts</div>
            <div class="sport-tab">American Football</div>
            <div class="sport-tab">E Games</div>
            <div class="sport-tab">Ice Hockey</div>
            <div class="sport-tab">Fu</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Games Grid with Icons
    st.markdown("### Popular Games")
    games = [
        {"name": "VIP TEENPATTI 1DAY", "value": "20", "icon": "fa-crown"},
        {"name": "MATKA MARKET", "value": "15", "icon": "fa-coins"},
        {"name": "DOLI DANA LIVE", "value": "10", "icon": "fa-gift"},
        {"name": "MOGAMBO", "value": "25", "icon": "fa-dice"},
        {"name": "TEEN PATTI", "value": "18", "icon": "fa-cards"},
        {"name": "LUCKY 6", "value": "12", "icon": "fa-dice-six"},
        {"name": "BEACH ROULETTE", "value": "22", "icon": "fa-compass"},
        {"name": "GOLDEN ROULETTE", "value": "30", "icon": "fa-trophy"},
        {"name": "POISON TEENPATTI ONE DAY", "value": "20", "icon": "fa-skull"},
        {"name": "UNIQUE ROULETTE", "value": "15", "icon": "fa-star"},
        {"name": "MINI SUPER OVER", "value": "10", "icon": "fa-cricket"},
        {"name": "GOAL", "value": "25", "icon": "fa-futbol"}
    ]
    
    # Add custom CSS for game cards with 3 columns
    st.markdown("""
    <style>
    .game-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 15px;
        padding: 10px 0;
    }
    .game-card-link {
        text-decoration: none;
        color: inherit;
        display: block;
    }
    .game-card {
        background: #16213e;
        border-radius: 12px;
        padding: 20px 15px;
        text-align: center;
        transition: all 0.3s ease;
        border: 2px solid #2d4059;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .game-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 15px rgba(0,0,0,0.2);
        border-color: #e94560;
    }
    .game-icon {
        font-size: 36px;
        margin-bottom: 12px;
        color: #e94560;
        background: rgba(233, 69, 96, 0.1);
        width: 70px;
        height: 70px;
        line-height: 70px;
        border-radius: 50%;
        margin: 0 auto 15px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .game-card h4 {
        margin: 0;
        font-size: 14px;
        color: #fff;
        font-weight: 600;
        padding: 0 5px;
    }
    .game-value {
        font-size: 26px;
        font-weight: bold;
        color: #e94560;
        margin-top: 10px;
        background: rgba(233, 69, 96, 0.1);
        padding: 5px 0;
        border-radius: 6px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="game-grid">', unsafe_allow_html=True)
    for game in games:
        st.markdown(f"""
            <a class="game-card-link" href="/Login" target="_top">
                <div class="game-card">
                    <div class="game-icon">
                        <i class="fas {game['icon']}"></i>
                    </div>
                    <h4>{game['name']}</h4>
                    <div class="game-value">{game['value']}</div>
                </div>
            </a>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# WhatsApp Float Button

st.markdown(f"""
    <a href="https://wa.me/{whatsapp_number}" target="_blank" class="whatsapp-float">
        <i class="fab fa-whatsapp"></i>
    </a>
""", unsafe_allow_html=True)

# Add Font Awesome for icons
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">', unsafe_allow_html=True)