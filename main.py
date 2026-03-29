import streamlit as st
import json
import os

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Career Guidance System", page_icon="🎯", layout="wide")

# ------------------ STYLING ------------------
st.markdown("""
<style>
.big-title {font-size:38px !important; font-weight:bold; color:#4CAF50;}
.section {font-size:26px !important; font-weight:bold; margin-top:20px;}
.sub {font-size:20px !important; font-weight:bold; color:#2196F3;}
.text {font-size:18px !important;}
</style>
""", unsafe_allow_html=True)

# ------------------ USER DB ------------------
USER_FILE = "users.json"

def load_users():
    if os.path.exists(USER_FILE):
        return json.load(open(USER_FILE))
    return {}

def save_users(users):
    json.dump(users, open(USER_FILE, "w"))

users = load_users()

# ------------------ LOGIN ------------------
def login():
    st.markdown("<div class='big-title'>🔐 Login / Signup</div>", unsafe_allow_html=True)

    option = st.radio("Choose Option", ["Login", "Signup"])
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if option == "Signup":
        if st.button("Create Account"):
            if user in users:
                st.error("User already exists")
            else:
                users[user] = pwd
                save_users(users)
                st.success("Account created")

    if option == "Login":
        if st.button("Login"):
            if user in users and users[user] == pwd:
                st.session_state["user"] = user
                st.rerun()
            else:
                st.error("Invalid login")

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
    st.markdown("<div class='big-title'>🎯 Career Guidance System</div>", unsafe_allow_html=True)
    st.markdown("<div class='text'>Choose your best career path easily.</div>", unsafe_allow_html=True)

# ------------------ AFTER 10TH ------------------
elif menu == "🎓 After 10th":
    st.markdown("<div class='big-title'>🎓 Career Options After 10th</div>", unsafe_allow_html=True)

    st.markdown("""
- Intermediate (Science / Commerce / Arts)
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
    st.markdown("<div class='big-title'>📘 Options After 12th</div>", unsafe_allow_html=True)
    st.write("Detailed guide already included ✔️")

# ------------------ CAREER SECTORS (SIMPLIFIED ✅) ------------------
elif menu == "💼 Career Sectors":

    st.markdown("<div class='big-title'>💼 Career Sectors (Simple Guide)</div>", unsafe_allow_html=True)

    # -------- GOVERNMENT --------
    st.markdown("<div class='section'>🏛️ Government Jobs</div>", unsafe_allow_html=True)

    st.markdown("""
✔ **UPSC (IAS, IPS)**  
👉 Study → Degree + Current Affairs  
👉 High-level officer jobs  

✔ **Banking (IBPS, SBI)**  
👉 Study → Maths, Reasoning  
👉 Jobs → Bank PO, Clerk  

✔ **Railways (RRB)**  
👉 Study → Basic subjects  
👉 Jobs → Clerk, TC  

✔ **Defense (Army, Navy, Airforce)**  
👉 NDA after 12th  
👉 Discipline + respect  

✔ **SSC Jobs**  
👉 Exams → SSC CGL, CHSL  
👉 Jobs → Govt office jobs  
""")

    # -------- PRIVATE --------
    st.markdown("<div class='section'>🏢 Private Jobs</div>", unsafe_allow_html=True)

    st.markdown("""
✔ **IT Sector 💻**  
👉 Skills → Coding, AI  
👉 Jobs → Developer, Data Scientist  

✔ **Business & Marketing 💼**  
👉 Study → BBA / MBA  
👉 Jobs → Manager, Sales  

✔ **Creative Field 🎨**  
👉 Skills → Design, Animation  
👉 Jobs → UI/UX, Designer  

✔ **Data & Analytics 📊**  
👉 Skills → Python, SQL  
👉 Jobs → Data Analyst  

✔ **Business / Startup 🚀**  
👉 Start your own work  
👉 Unlimited growth  
""")

    # -------- FLOW --------
    st.markdown("<div class='section'>🎯 Simple Career Flow</div>", unsafe_allow_html=True)

    st.info("🏛️ Government → Degree → Exam → Job")
    st.info("🏢 Private → Skills → Job → Growth")

    # -------- STRATEGY --------
    st.markdown("<div class='section'>💡 Best Strategy</div>", unsafe_allow_html=True)

    st.success("""
🔥 Do Degree + Learn Skills  
🔥 Try both Govt + Private  
🔥 Choose based on interest  
""")

# ------------------ AI ------------------
elif menu == "🤖 AI Recommendation":
    st.markdown("<div class='big-title'>🤖 Career Recommendation</div>", unsafe_allow_html=True)

    interest = st.selectbox("Select Interest", ["Technology", "Biology", "Business", "Creative"])

    if st.button("Get Career"):
        st.success(f"Best career for {interest}")

# ------------------ LOGOUT ------------------
elif menu == "🚪 Logout":
    del st.session_state["user"]
    st.rerun()
