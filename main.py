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

# ------------------ AFTER 10TH (UPDATED) ------------------
elif menu == "🎓 After 10th":
    st.markdown("<div class='big-title'>🎓 Career Options After 10th</div>", unsafe_allow_html=True)

    st.markdown("<div class='section'>📚 Main Options</div>", unsafe_allow_html=True)

    st.markdown("""
### 1️⃣ Intermediate (11th & 12th)
- Science (MPC / BiPC)
- Commerce
- Arts  
👉 Best for higher studies

### 2️⃣ Polytechnic Diploma
- Engineering diploma (Mechanical, Civil, CSE)
👉 Job + lateral entry to B.Tech

### 3️⃣ ITI (Industrial Training)
- Electrician, Fitter, Technician  
👉 Quick job-oriented

### 4️⃣ Paramedical Courses
- Lab Technician, Nursing assistant  
👉 Healthcare field

### 5️⃣ Agriculture
- Farming, Agri science  
👉 Govt + business scope

### 6️⃣ Vocational Courses
- Skill-based training (plumbing, electrician)

### 7️⃣ Creative Fields
- Designing, animation, media

### 8️⃣ Hotel Management
- Hospitality industry jobs

### 9️⃣ Sports
- Athlete, coach, fitness

### 🔟 Defense
- Army, Navy entry

### 1️⃣1️⃣ Business / Freelancing
- Small business
- Online work
👉 Earn early 💰
""")

# ------------------ AFTER 12TH (FULL GUIDE 🔥) ------------------
elif menu == "📘 After 12th":
    st.markdown("<div class='big-title'>📘 OPTIONS AFTER 12TH (FULL GUIDE)</div>", unsafe_allow_html=True)

    st.markdown("<div class='section'>🎯 Higher Studies</div>", unsafe_allow_html=True)

    st.markdown("<div class='sub'>🔬 Science</div>", unsafe_allow_html=True)
    st.markdown("""
**MPC:**
- B.Tech / BE
- B.Sc
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
- CA / CS / CMA  
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
- Railways  
- Police  
- Forest Guard  
""")

    st.markdown("<div class='section'>🛠️ Professional Courses</div>", unsafe_allow_html=True)
    st.markdown("""
💻 IT: Web Dev, AI, Data Science  
🏥 Paramedical  
🎨 Design & Animation  
⚖️ Law  
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
        "Path": ["B.Tech", "Medical", "Govt", "Creative", "Business"],
        "Growth": ["High", "High", "Medium", "High", "Unlimited"]
    })

    st.markdown("<div class='section'>🎯 Best Govt Path</div>", unsafe_allow_html=True)
    st.success("12th → Degree → UPSC / SSC OR Direct SSC / Defense")

    st.markdown("<div class='section'>💡 AI/ML Suggestion</div>", unsafe_allow_html=True)
    st.success("""
👉 12th MPC → B.Tech CSE  
👉 Learn Python + AI/ML  
👉 Jobs: IT / ISRO / DRDO / NIC  
""")

# ------------------ CAREER SECTORS ------------------
elif menu == "💼 Career Sectors":
    st.markdown("<div class='big-title'>💼 Career Sectors</div>", unsafe_allow_html=True)
    st.write("Detailed roadmap already added previously")

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
