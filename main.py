import streamlit as st
import json
import os

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Career Guidance System", page_icon="🎯", layout="wide")

# ------------------ CSS ------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #1f1c2c, #928dab);
    color: white;
}

/* Cards */
.card {
    background: rgba(255, 255, 255, 0.1);
    padding: 20px;
    border-radius: 15px;
    backdrop-filter: blur(10px);
    margin: 10px 0;
}

/* Title */
.title {
    font-size: 36px;
    text-align:center;
    font-weight:bold;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(45deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 10px;
    height: 3em;
}

/* -------- LOGIN WHITE THEME -------- */
.login-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 85vh;
}

.login-card {
    background: white;
    padding: 30px 25px;
    border-radius: 15px;
    width: 320px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.25);
}

/* Text */
.login-title {
    text-align: center;
    font-size: 26px;
    font-weight: bold;
    color: #111;
}

.login-sub {
    text-align: center;
    font-size: 13px;
    color: #555;
    margin-bottom: 15px;
}

/* Inputs */
div[data-baseweb="input"] input {
    color: black !important;
}

/* Labels */
label {
    color: black !important;
}

/* Radio */
.stRadio > div {
    justify-content: center;
    color: black;
}

/* Full width button */
.stButton > button {
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# ------------------ USER DATABASE ------------------
USER_FILE = "users.json"

def load_users():
    if os.path.exists(USER_FILE):
        return json.load(open(USER_FILE))
    return {}

def save_users(users):
    json.dump(users, open(USER_FILE, "w"))

users = load_users()

# ------------------ LOGIN FUNCTION ------------------
def login():
    st.markdown("<div class='login-wrapper'>", unsafe_allow_html=True)
    st.markdown("<div class='login-card'>", unsafe_allow_html=True)

    st.markdown("<div class='login-title'>🎯 Career Guidance</div>", unsafe_allow_html=True)
    st.markdown("<div class='login-sub'>Login to continue</div>", unsafe_allow_html=True)

    option = st.radio("", ["Login", "Signup"], horizontal=True)

    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if option == "Signup":
        if st.button("Create Account"):
            if user and pwd:
                users[user] = pwd
                save_users(users)
                st.success("Account created successfully ✅")
            else:
                st.warning("Please fill all fields")

    if option == "Login":
        if st.button("Login"):
            if user in users and users[user] == pwd:
                st.session_state["user"] = user
                st.rerun()
            else:
                st.error("Invalid username or password ❌")

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ AUTH CHECK ------------------
if "user" not in st.session_state:
    login()
    st.stop()

# ------------------ SIDEBAR ------------------
menu = st.sidebar.radio("Menu", [
    "🏠 Home", "🎓 After 10th", "📘 After 12th",
    "💼 Career Sectors", "🤖 AI Recommendation", "🚪 Logout"
])

# ------------------ HOME ------------------
if menu == "🏠 Home":
    st.markdown("<div class='title'>🎯 Career Guidance System</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    col1.markdown("<div class='card'>🎓 50+ Career Options</div>", unsafe_allow_html=True)
    col2.markdown("<div class='card'>💼 Govt + Private Jobs</div>", unsafe_allow_html=True)
    col3.markdown("<div class='card'>🤖 AI Guidance</div>", unsafe_allow_html=True)

# ------------------ AFTER 10TH ------------------
elif menu == "🎓 After 10th":
    st.markdown("<div class='title'>🎓 After 10th Guide</div>", unsafe_allow_html=True)

    options = [
        "Intermediate (Science, Commerce, Arts)",
        "Diploma (Engineering)",
        "ITI (Technical jobs)",
        "Paramedical",
        "Agriculture",
        "Vocational Courses",
        "Creative Fields",
        "Hotel Management",
        "Sports",
        "Defense",
        "Open School",
        "Business"
    ]

    for opt in options:
        st.markdown(f"<div class='card'>• {opt}</div>", unsafe_allow_html=True)

# ------------------ AFTER 12TH ------------------
elif menu == "📘 After 12th":
    st.markdown("<div class='title'>📘 After 12th Full Guide</div>", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["🎯 Studies", "🪖 Govt Jobs", "🛠 Courses", "🚀 Careers"])

    with tab1:
        st.markdown("<div class='card'>Engineering, Medical, BCA, BBA, BA, B.Com</div>", unsafe_allow_html=True)

    with tab2:
        st.markdown("<div class='card'>NDA, SSC, Railways, Police, Banking</div>", unsafe_allow_html=True)

    with tab3:
        st.markdown("<div class='card'>IT Courses, Paramedical, Design, Law</div>", unsafe_allow_html=True)

    with tab4:
        st.markdown("<div class='card'>Freelancing, Business, YouTube, Sports</div>", unsafe_allow_html=True)

# ------------------ CAREER SECTOR ------------------
elif menu == "💼 Career Sectors":
    st.markdown("<div class='title'>💼 Career Sectors</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    col1.markdown("<div class='card'>🏛 Govt Jobs<br>UPSC, Banking, Railways, SSC</div>", unsafe_allow_html=True)
    col2.markdown("<div class='card'>🏢 Private Jobs<br>IT, Marketing, Finance</div>", unsafe_allow_html=True)

# ------------------ AI RECOMMEND ------------------
elif menu == "🤖 AI Recommendation":
    st.markdown("<div class='title'>🤖 Career Recommendation</div>", unsafe_allow_html=True)

    interest = st.selectbox("Select your interest", ["Technology", "Biology", "Business", "Creative"])

    if st.button("Get Recommendation"):
        st.balloons()
        st.success(f"🎯 Best career for {interest}: Coming Soon (ML Model)")

# ------------------ LOGOUT ------------------
elif menu == "🚪 Logout":
    del st.session_state["user"]
    st.rerun()
