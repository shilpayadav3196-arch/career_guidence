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

# ------------------ AFTER 12TH (FULL UPDATED 🔥) ------------------
elif menu == "📘 After 12th":
    st.markdown("<div class='big-title'>🎓 OPTIONS AFTER 12TH (COMPLETE LIST)</div>", unsafe_allow_html=True)

    st.markdown("<div class='section'>🔬 Science Stream</div>", unsafe_allow_html=True)
    st.markdown("""
**MPC:**
- B.Tech / BE, BCA, B.Sc, B.Arch  
👉 Careers: Software Engineer, AI Engineer  

**BiPC:**
- MBBS, BDS, Pharmacy, Nursing  
👉 Careers: Doctor, Nurse  

**Both:**
- Biotechnology, Biomedical  
""")

    st.markdown("<div class='section'>💼 Commerce</div>", unsafe_allow_html=True)
    st.markdown("""
- B.Com, BBA, BBM  
- CA, CS, CMA  
👉 Careers: Accountant, Banker  
""")

    st.markdown("<div class='section'>🎨 Arts</div>", unsafe_allow_html=True)
    st.markdown("""
- BA, LLB, Journalism  
👉 Careers: Lawyer, Teacher  
""")

    st.markdown("<div class='section'>🏛️ Government Jobs</div>", unsafe_allow_html=True)
    st.markdown("""
- NDA, SSC CHSL, Railways, Police  
- Forest Guard, Post Office  
""")

    st.markdown("<div class='section'>🛠️ Professional Courses</div>", unsafe_allow_html=True)
    st.markdown("""
- Polytechnic, Paramedical  
- Hotel Management, Aviation  
""")

    st.markdown("<div class='section'>💻 Skill Courses</div>", unsafe_allow_html=True)
    st.markdown("""
- Web Dev, AI/ML, Cyber Security  
👉 Fast jobs + freelancing  
""")

    st.markdown("<div class='section'>🎨 Creative Careers</div>", unsafe_allow_html=True)
    st.markdown("""
- Animation, UI/UX, Film  
""")

    st.markdown("<div class='section'>💼 Business & Freelancing</div>", unsafe_allow_html=True)
    st.markdown("""
- Startup, YouTube, Coding  
""")

    st.markdown("<div class='section'>📊 Comparison</div>", unsafe_allow_html=True)
    st.table({
        "Path": ["Engineering", "Medical", "Govt", "Skills", "Business"],
        "Growth": ["High", "High", "High", "Medium", "Unlimited"]
    })

    st.markdown("<div class='section'>🎯 Best Path</div>", unsafe_allow_html=True)
    st.success("""
💻 Tech → B.Tech  
🏥 Medical → MBBS  
💼 Business → BBA  
🏛️ Govt → Degree + Exams  
""")

    st.markdown("<div class='section'>💡 Personal Suggestion</div>", unsafe_allow_html=True)
    st.success("""
👉 12th MPC → B.Tech CSE  
👉 Learn AI/ML  
👉 Jobs: IT / ISRO / DRDO  
""")

# ------------------ CAREER SECTORS ------------------
elif menu == "💼 Career Sectors":
    st.markdown("<div class='big-title'>💼 Career Sectors</div>", unsafe_allow_html=True)
    st.write("Full detailed roadmap already added")

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
