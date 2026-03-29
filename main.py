import streamlit as st
import json
import os
import time

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Career Guidance System", page_icon="🎯", layout="wide")

# ------------------ CUSTOM STYLING ------------------
st.markdown("""
<style>
.big-title {font-size:40px !important; font-weight:bold; color:#4CAF50;}
.section {font-size:26px !important; font-weight:bold; margin-top:20px;}
.sub {font-size:20px !important; font-weight:bold; color:#2196F3;}
.text {font-size:18px !important;}
</style>
""", unsafe_allow_html=True)

# ------------------ USER DATABASE ------------------
USER_FILE = "users.json"

def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f)

users = load_users()

# ------------------ ANIMATION ------------------
def show_title(text):
    st.markdown(f"<div class='big-title'>{text}</div>", unsafe_allow_html=True)

# ------------------ LOGIN ------------------
def login_signup():
    st.markdown("""
    <style>
    .login-box {
        background-color: #1e1e2f;
        padding: 40px;
        border-radius: 15px;
        box-shadow: 0px 0px 20px rgba(0,0,0,0.3);
    }
    .title {
        text-align:center;
        font-size:30px;
        font-weight:bold;
        color:#4CAF50;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='title'>🎯 Career Guidance Login</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.markdown("<div class='login-box'>", unsafe_allow_html=True)

        option = st.radio("", ["Login", "Signup"])

        username = st.text_input("👤 Username")
        password = st.text_input("🔑 Password", type="password")

        if option == "Signup":
            if st.button("🚀 Create Account", use_container_width=True):
                if username in users:
                    st.error("User already exists!")
                else:
                    users[username] = password
                    save_users(users)
                    st.success("Account created!")

        if option == "Login":
            if st.button("🔓 Login", use_container_width=True):
                if username in users and users[username] == password:
                    st.session_state["user"] = username
                    st.rerun()
                else:
                    st.error("Invalid credentials")

        st.markdown("</div>", unsafe_allow_html=True)
# ------------------ AUTH ------------------
if "user" not in st.session_state:
    login_signup()
    st.stop()

# ------------------ SIDEBAR ------------------
st.sidebar.title(f"👋 {st.session_state['user']}")
menu = st.sidebar.radio("Menu", [
    "🏠 Home",
    "🎓 After 10th",
    "📘 After 12th",
    "💼 Career Sectors",
    "🤖 AI Recommendation",
    "🚪 Logout"
])

# ------------------ HOME ------------------
if menu == "🏠 Home":
    show_title("🎯 AI Career Guidance System")
    st.markdown("<div class='text'>Helping students choose the best career path based on interests and goals.</div>", unsafe_allow_html=True)

# ------------------ AFTER 10TH ------------------
elif menu == "🎓 After 10th":
    show_title("🎓 Career Options After 10th")
    st.info("Choose based on Interest + Time + Career Goals")

    st.markdown("<div class='section'>Streams & Paths</div>", unsafe_allow_html=True)

    st.markdown("""
- Intermediate (Science, Commerce, Arts)
- Polytechnic Diploma
- ITI
- Paramedical Courses
- Agriculture
- Vocational Courses
- Creative Fields
- Hotel Management
- Sports
- Defense
- Business / Freelancing
""")

# ------------------ AFTER 12TH ------------------
elif menu == "📘 After 12th":
    show_title("📘 Career Options After 12th (FULL GUIDE)")

    st.markdown("<div class='section'>🎯 Higher Studies</div>", unsafe_allow_html=True)

    st.markdown("<div class='sub'>🔬 Science Students</div>", unsafe_allow_html=True)
    st.markdown("""
**MPC:**
- B.Tech (CSE, AI, Mechanical, Civil)
- BCA
- NDA

**BiPC:**
- MBBS
- BDS
- Pharmacy
- Nursing
- Biotechnology
""")

    st.markdown("<div class='sub'>💼 Commerce</div>", unsafe_allow_html=True)
    st.markdown("""
- B.Com
- BBA
- CA, CS, CMA
- Banking & Finance
""")

    st.markdown("<div class='sub'>🎨 Arts</div>", unsafe_allow_html=True)
    st.markdown("""
- BA
- LLB
- Journalism
- Psychology
""")

    st.markdown("<div class='section'>🪖 Government Jobs</div>", unsafe_allow_html=True)
    st.markdown("""
- NDA (Army/Navy/Airforce)
- SSC CHSL / MTS
- Railways (TC, Clerk)
- Police Jobs
- Forest Guard, Post Office
""")

    st.markdown("<div class='section'>🛠️ Professional Courses</div>", unsafe_allow_html=True)
    st.markdown("""
- IT: Web Dev, Data Science, Cyber Security
- Paramedical
- Hotel Management
- Animation & Design
- Law (LLB)
""")

    st.markdown("<div class='section'>🚀 Alternative Careers</div>", unsafe_allow_html=True)
    st.markdown("""
- Business / Startup
- Freelancing
- Content Creation
- Sports
""")

    st.markdown("<div class='section'>📊 Comparison</div>", unsafe_allow_html=True)
    st.table({
        "Path": ["B.Tech", "Medical", "Govt Jobs", "Creative", "Business"],
        "Growth": ["Very High", "Very High", "Medium", "High", "Unlimited"],
        "Difficulty": ["High", "Very High", "Medium", "Skill-based", "Risky"]
    })

    st.markdown("<div class='section'>🎯 Smart Government Path</div>", unsafe_allow_html=True)
    st.success("""
12th → Graduation → UPSC / SSC  
OR  
12th → SSC / Defense  
OR  
12th → Degree → Banking / Railways
""")

# ------------------ CAREER SECTORS ------------------
elif menu == "💼 Career Sectors":
    show_title("💼 Career Sectors")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🏛️ Government")
        st.write("UPSC, Banking, Railways, Defense")

    with col2:
        st.subheader("🏢 Private")
        st.write("Software, Marketing, Business, Design")

# ------------------ AI RECOMMENDATION ------------------
elif menu == "🤖 AI Recommendation":
    show_title("🤖 Career Recommendation")

    interest = st.selectbox("Select Interest", [
        "Technology", "Biology", "Business", "Arts", "Creative", "Sports"
    ])

    if st.button("Get Recommendation"):
        if interest == "Technology":
            st.success("Software, AI, Data Science")

        elif interest == "Biology":
            st.success("Doctor, Pharmacy, Healthcare")

        elif interest == "Business":
            st.success("CA, MBA, Entrepreneurship")

        elif interest == "Creative":
            st.success("Design, Animation, Media")

        elif interest == "Sports":
            st.success("Athlete, Coach")

        else:
            st.success("UPSC, Law, Govt Jobs")

# ------------------ LOGOUT ------------------
elif menu == "🚪 Logout":
    del st.session_state["user"]
    st.rerun()
