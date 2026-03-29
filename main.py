import streamlit as st
import json
import os

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Career Guidance System", page_icon="🎯", layout="wide")
# ------------------ LOGO ------------------
st.sidebar.image("logo.png", width=120)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("logo.png", width=150)

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
    st.markdown("<div class='text'>This system helps students choose the best career path after 10th and 12th.</div>", unsafe_allow_html=True)

# ------------------ AFTER 10TH (FULL ELABORATED 🔥) ------------------
elif menu == "🎓 After 10th":

    st.markdown("<div class='big-title'>🎓 Career Options After 10th</div>", unsafe_allow_html=True)

    st.markdown("<div class='section'>📚 1. Intermediate (11th & 12th)</div>", unsafe_allow_html=True)
    st.markdown("""
👉 Most common and best option for higher studies  

Streams:
- 🔬 Science (MPC / BiPC)
- 💼 Commerce
- 🎨 Arts  

✔ Leads to degree courses like Engineering, Medical, Business, etc.
""")

    st.markdown("<div class='section'>🛠️ 2. Polytechnic Diploma</div>", unsafe_allow_html=True)
    st.markdown("""
👉 Engineering diploma after 10th  

Courses:
- Mechanical
- Civil
- Computer Science  

✔ Benefits:
- Early job opportunities  
- Direct entry to B.Tech (2nd year)
""")

    st.markdown("<div class='section'>⚙️ 3. ITI (Industrial Training Institute)</div>", unsafe_allow_html=True)
    st.markdown("""
👉 Skill-based technical training  

Trades:
- Electrician
- Fitter
- Welder  

✔ Quick job opportunities  
✔ Good for hands-on learners
""")

    st.markdown("<div class='section'>🏥 4. Paramedical Courses</div>", unsafe_allow_html=True)
    st.markdown("""
👉 Healthcare support roles  

Courses:
- Lab Technician
- Nursing Assistant  

✔ Stable career in hospitals
""")

    st.markdown("<div class='section'>🌾 5. Agriculture</div>", unsafe_allow_html=True)
    st.markdown("""
👉 Farming and agri-business  

✔ Government jobs + business opportunities
""")

    st.markdown("<div class='section'>🎨 6. Creative Fields</div>", unsafe_allow_html=True)
    st.markdown("""
👉 For creative students  

Options:
- Designing
- Animation
- Media  

✔ Freelancing + job opportunities
""")

    st.markdown("<div class='section'>🏨 7. Hotel Management</div>", unsafe_allow_html=True)
    st.markdown("""
👉 Hospitality industry  

✔ Jobs in hotels, tourism, airlines
""")

    st.markdown("<div class='section'>🏃 8. Sports</div>", unsafe_allow_html=True)
    st.markdown("""
👉 Physical careers  

✔ Athlete, Coach, Trainer
""")

    st.markdown("<div class='section'>🪖 9. Defense</div>", unsafe_allow_html=True)
    st.markdown("""
👉 Army, Navy careers  

✔ Discipline + respect
""")

    st.markdown("<div class='section'>💼 10. Business / Freelancing</div>", unsafe_allow_html=True)
    st.markdown("""
👉 Start early earning  

✔ Online work, small business
""")

# ------------------ AFTER 12TH (FULL ELABORATED 🔥) ------------------
elif menu == "📘 After 12th":

    st.markdown("<div class='big-title'>📘 Career Options After 12th</div>", unsafe_allow_html=True)

    # SCIENCE
    st.markdown("<div class='section'>🔬 Science Stream</div>", unsafe_allow_html=True)

    st.markdown("<div class='sub'>💻 MPC (Maths)</div>", unsafe_allow_html=True)
    st.markdown("""
Courses:
- B.Tech / BE  
- BCA  
- B.Sc  
- Architecture  

Careers:
- Software Engineer  
- AI Engineer  
- Data Scientist  
""")

    st.markdown("<div class='sub'>🏥 BiPC (Biology)</div>", unsafe_allow_html=True)
    st.markdown("""
Courses:
- MBBS  
- BDS  
- Pharmacy  
- Nursing  

Careers:
- Doctor  
- Nurse  
- Pharmacist  
""")

    # COMMERCE
    st.markdown("<div class='section'>💼 Commerce</div>", unsafe_allow_html=True)
    st.markdown("""
Courses:
- B.Com  
- BBA  

Professional:
- CA, CS, CMA  

Careers:
- Accountant  
- Banker  
""")

    # ARTS
    st.markdown("<div class='section'>🎨 Arts</div>", unsafe_allow_html=True)
    st.markdown("""
Courses:
- BA  
- Law  
- Journalism  

Careers:
- Lawyer  
- Teacher  
""")

    # GOVT
    st.markdown("<div class='section'>🏛️ Government Jobs</div>", unsafe_allow_html=True)
    st.markdown("""
- NDA  
- SSC  
- Railways  
- Police  
""")

    # SKILLS
    st.markdown("<div class='section'>💻 Skill Courses</div>", unsafe_allow_html=True)
    st.markdown("""
- AI/ML  
- Web Dev  
- Cyber Security  

✔ Fast job opportunities
""")

    # BUSINESS
    st.markdown("<div class='section'>🚀 Business & Freelancing</div>", unsafe_allow_html=True)
    st.markdown("""
- Startup  
- YouTube  
- Freelancing  
""")

    # SUGGESTION
    st.markdown("<div class='section'>💡 Best Suggestion</div>", unsafe_allow_html=True)
    st.success("""
👉 Choose based on interest  
👉 For AI/ML → B.Tech CSE  
👉 Combine skills + degree  
""")

# ------------------ CAREER SECTORS ------------------
elif menu == "💼 Career Sectors":
    st.markdown("<div class='big-title'>💼 Career Sectors</div>", unsafe_allow_html=True)
    st.write("Simple explanation provided in previous section")

# ------------------ AI ------------------
elif menu == "🤖 AI Recommendation":

    st.markdown("<div class='big-title'>🤖 Smart Career Recommendation</div>", unsafe_allow_html=True)

    st.markdown("### 🧠 Tell us about yourself")

    # -------- INTEREST --------
    interest = st.selectbox("🎯 Select Your Interest", [
        "Technology 💻",
        "Medical 🏥",
        "Business 💼",
        "Creative 🎨",
        "Government Jobs 🏛️",
        "Teaching 📚",
        "Defense 🪖",
        "Sports 🏃",
        "Agriculture 🌾",
        "Hospitality 🏨"
    ])

    # -------- SKILL LEVEL --------
    skill = st.selectbox("⚡ Your Strength", [
        "Problem Solving",
        "Communication",
        "Creativity",
        "Leadership",
        "Physical Fitness",
        "Analytical Thinking"
    ])

    # -------- WORK STYLE --------
    work_style = st.radio("💼 Preferred Work Style", [
        "High Salary Job 💰",
        "Government Job 🏛️",
        "Business / Startup 🚀",
        "Work-Life Balance 😊"
    ])

    # -------- RECOMMEND BUTTON --------
    if st.button("🔍 Get Recommendation"):

        st.markdown("## 🎯 Best Career Options For You")

        # -------- LOGIC --------
        if "Technology" in interest:
            st.success("💻 Best Options: B.Tech (CSE, AI), BCA")
            st.info("👉 Careers: Software Engineer, AI Engineer, Data Scientist")

        elif "Medical" in interest:
            st.success("🏥 Best Options: MBBS, BDS, Pharmacy")
            st.info("👉 Careers: Doctor, Pharmacist, Nurse")

        elif "Business" in interest:
            st.success("💼 Best Options: BBA, B.Com, MBA")
            st.info("👉 Careers: Manager, Entrepreneur, Analyst")

        elif "Creative" in interest:
            st.success("🎨 Best Options: Design, Animation, Media")
            st.info("👉 Careers: Graphic Designer, UI/UX Designer")

        elif "Government" in interest:
            st.success("🏛️ Best Path: Degree + UPSC / SSC")
            st.info("👉 Careers: IAS, IPS, Govt Officer")

        elif "Teaching" in interest:
            st.success("📚 Best Options: BA/B.Sc + B.Ed")
            st.info("👉 Careers: Teacher, Lecturer")

        elif "Defense" in interest:
            st.success("🪖 Best Path: NDA, CDS")
            st.info("👉 Careers: Army, Navy, Airforce")

        elif "Sports" in interest:
            st.success("🏃 Best Options: Sports Academy")
            st.info("👉 Careers: Athlete, Coach")

        elif "Agriculture" in interest:
            st.success("🌾 Best Options: B.Sc Agriculture")
            st.info("👉 Careers: Agri Officer, Farming Business")

        elif "Hospitality" in interest:
            st.success("🏨 Best Options: Hotel Management")
            st.info("👉 Careers: Hotel Manager, Tourism")

        # -------- EXTRA SUGGESTION --------
        st.markdown("### 💡 Smart Suggestion")

        if work_style == "Government Job 🏛️":
            st.warning("👉 Focus on Government Exams + Degree")

        elif work_style == "Business / Startup 🚀":
            st.warning("👉 Learn skills + Start small business")

        elif work_style == "High Salary Job 💰":
            st.warning("👉 Choose IT / AI / Management fields")

        elif work_style == "Work-Life Balance 😊":
            st.warning("👉 Consider stable jobs like Teaching / Govt")
# ------------------ LOGOUT ------------------
elif menu == "🚪 Logout":
    del st.session_state["user"]
    st.rerun()
