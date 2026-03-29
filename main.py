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
### 1️⃣ Intermediate
Science / Commerce / Arts → Best for higher studies

### 2️⃣ Polytechnic Diploma
Engineering diploma → Job + B.Tech entry

### 3️⃣ ITI
Technical skills → Quick jobs

### 4️⃣ Paramedical
Healthcare support roles

### 5️⃣ Agriculture
Farming + govt opportunities

### 6️⃣ Vocational Courses
Skill-based careers

### 7️⃣ Creative Fields
Design, media, animation

### 8️⃣ Hotel Management
Hospitality industry

### 9️⃣ Sports
Athlete / coach

### 🔟 Defense
Army, Navy

### 1️⃣1️⃣ Business / Freelancing
Earn early 💰
""")

# ------------------ AFTER 12TH ------------------
elif menu == "📘 After 12th":
    st.markdown("<div class='big-title'>📘 OPTIONS AFTER 12TH</div>", unsafe_allow_html=True)

    st.markdown("🎯 Covers Higher Studies, Govt Jobs, Skills & Business")

# ------------------ CAREER SECTORS (FULL UPDATED 🔥) ------------------
elif menu == "💼 Career Sectors":

    st.markdown("<div class='big-title'>💼 Career Sectors – Complete Guide</div>", unsafe_allow_html=True)

    # GOVERNMENT
    st.markdown("<div class='section'>🏛️ GOVERNMENT SECTOR</div>", unsafe_allow_html=True)

    st.markdown("""
### 1️⃣ UPSC (IAS, IPS, IFS)
📚 Study:
- Graduation (any degree)
- History, Geography, Polity, Economy, Current Affairs

📝 Exams:
- Prelims → Mains → Interview

🧠 Skills:
- Reading, Writing, Analysis
""")

    st.markdown("""
### 2️⃣ Banking Sector
📚 Study:
- Any Degree
- Maths, Reasoning, English

📝 Exams:
- IBPS PO / Clerk
- SBI PO
""")

    st.markdown("""
### 3️⃣ Railways
📚 Study:
- 12th / Degree

📝 Exams:
- RRB NTPC, Group D

👉 Jobs:
- Clerk, TC, Station Master
""")

    st.markdown("""
### 4️⃣ Defense
📚 Study:
- 12th Science

📝 Exams:
- NDA, CDS

🧠 Skills:
- Fitness, discipline
""")

    st.markdown("""
### 5️⃣ SSC Jobs
📚 Study:
- Graduation

📝 Exams:
- SSC CGL, CHSL

👉 Jobs:
- Income Tax Officer, Clerk
""")

    # PRIVATE
    st.markdown("<div class='section'>🏢 PRIVATE SECTOR</div>", unsafe_allow_html=True)

    st.markdown("""
### 💻 IT Sector
- B.Tech / BCA
- Python, AI, Web Dev
👉 Jobs: Developer, Data Scientist
""")

    st.markdown("""
### 📢 Marketing
- BBA → MBA
👉 Jobs: Manager, Analyst
""")

    st.markdown("""
### 💼 Business
- Startup / Online business
👉 Unlimited growth
""")

    st.markdown("""
### 🎨 Creative
- Design, Animation
👉 UI/UX jobs
""")

    st.markdown("""
### 📊 Data Field
- Python, SQL
👉 Data Analyst
""")

    # FLOW
    st.markdown("<div class='section'>🎯 Career Flow</div>", unsafe_allow_html=True)
    st.info("Government → Degree → Exam → Job")
    st.info("Private → Skills → Job → Growth")

    # STRATEGY
    st.markdown("<div class='section'>💡 Smart Strategy</div>", unsafe_allow_html=True)
    st.success("""
🔥 B.Tech → Job + Govt prep  
🔥 BA/B.Com → UPSC focus  
🔥 AI/ML → High demand  
""")

    # FINAL ADVICE
    st.markdown("<div class='section'>🚀 Final Advice</div>", unsafe_allow_html=True)
    st.warning("""
✔ Govt = Stability + patience  
✔ Private = Skills + growth  
✔ Business = Risk + high reward  
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
