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

# ------------------ TITLE ------------------
def show_title(text):
    st.markdown(f"<div class='big-title'>{text}</div>", unsafe_allow_html=True)

# ------------------ LOGIN ------------------
def login_signup():
    show_title("🔐 Login / Signup")

    option = st.radio("Choose Option", ["Login", "Signup"])
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if option == "Signup":
        if st.button("Create Account"):
            if username in users:
                st.error("User already exists!")
            else:
                users[username] = password
                save_users(users)
                st.success("Account created successfully!")

    if option == "Login":
        if st.button("Login"):
            if username in users and users[username] == password:
                st.session_state["user"] = username
                st.rerun()
            else:
                st.error("Invalid credentials")

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

    st.markdown("<div class='sub'>🔬 Science</div>", unsafe_allow_html=True)
    st.markdown("""
- B.Tech, BCA, NDA  
- MBBS, BDS, Pharmacy  
""")

    st.markdown("<div class='sub'>💼 Commerce</div>", unsafe_allow_html=True)
    st.markdown("""
- B.Com, BBA  
- CA, CS, CMA  
""")

    st.markdown("<div class='sub'>🎨 Arts</div>", unsafe_allow_html=True)
    st.markdown("""
- BA, LLB  
- Journalism, Psychology  
""")

# ------------------ CAREER SECTORS (UPDATED 🔥) ------------------
elif menu == "💼 Career Sectors":
    show_title("💼 Career Sectors – Detailed Roadmap")

    # -------- GOVERNMENT --------
    st.markdown("<div class='section'>🏛️ GOVERNMENT SECTOR</div>", unsafe_allow_html=True)

    st.markdown("### 1️⃣ UPSC (IAS, IPS, IFS)")
    st.markdown("""
📚 Study: Graduation + History, Polity, Economy  
📝 Exams: Prelims → Mains → Interview  
🧠 Skills: Reading, Writing, Analysis  
""")

    st.markdown("### 2️⃣ Banking (IBPS, SBI)")
    st.markdown("""
📚 Study: Maths, Reasoning, English  
📝 Exams: IBPS PO / Clerk  
🧠 Skills: Speed + Accuracy  
""")

    st.markdown("### 3️⃣ Railways")
    st.markdown("""
📚 Study: Maths, Science, GK  
📝 Exams: RRB NTPC, Group D  
👉 Jobs: Clerk, TC, Station Master  
""")

    st.markdown("### 4️⃣ Defense")
    st.markdown("""
📚 Study: 12th Science  
📝 Exams: NDA, CDS  
🧠 Skills: Fitness, Discipline  
""")

    st.markdown("### 5️⃣ SSC Jobs")
    st.markdown("""
📚 Study: Maths, Reasoning, English  
📝 Exams: SSC CGL, CHSL  
👉 Jobs: Income Tax Officer, Clerk  
""")

    # -------- PRIVATE --------
    st.markdown("<div class='section'>🏢 PRIVATE SECTOR</div>", unsafe_allow_html=True)

    st.markdown("### 💻 IT Sector")
    st.markdown("""
📚 B.Tech / BCA  
Skills: Python, AI, Web Dev  
Jobs: Developer, Data Scientist  
🔥 High demand  
""")

    st.markdown("### 📢 Marketing")
    st.markdown("""
📚 BBA → MBA  
Skills: Communication, Sales  
Jobs: Marketing Manager  
""")

    st.markdown("### 💼 Business")
    st.markdown("""
Skills: Planning, Finance  
👉 Startup / Online business  
💰 Unlimited growth  
""")

    st.markdown("### 🎨 Creative")
    st.markdown("""
Skills: Design, Animation  
Jobs: UI/UX, Designer  
""")

    st.markdown("### 📊 Data Field")
    st.markdown("""
Skills: Python, SQL  
Jobs: Data Analyst  
""")

    # -------- FLOW --------
    st.markdown("<div class='section'>🎯 Career Flow</div>", unsafe_allow_html=True)
    st.info("Government: Degree → Exam → Job")
    st.info("Private: Skills → Job → Growth")

    # -------- STRATEGY --------
    st.markdown("<div class='section'>💡 Best Strategy</div>", unsafe_allow_html=True)

    st.success("""
🔥 B.Tech → Job + Govt Prep  
🔥 BA/B.Com → UPSC/SSC  
🔥 AI/ML → High demand career  
""")

# ------------------ AI RECOMMEND ------------------
elif menu == "🤖 AI Recommendation":
    show_title("🤖 Career Recommendation")

    interest = st.selectbox("Select Interest", [
        "Technology", "Biology", "Business", "Creative", "Sports"
    ])

    if st.button("Get Recommendation"):
        st.success(f"Best career for {interest} 🎯")

# ------------------ LOGOUT ------------------
elif menu == "🚪 Logout":
    del st.session_state["user"]
    st.rerun()
