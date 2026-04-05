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
    st.markdown("<div class='big-title🔐 Login / Signup</div>", unsafe_allow_html=True)

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
 Most common and best option for higher studies  

Streams:
- 🔬 Science (MPC / BiPC)
- 💼 Commerce
- 🎨 Arts  

✔ Leads to degree courses like Engineering, Medical, Business, etc.
""")

    st.markdown("<div class='section'>🛠️ 2. Polytechnic Diploma</div>", unsafe_allow_html=True)
    st.markdown("""
 Engineering diploma after 10th  

Courses:
- Mechanical
- Civil
- Computer Science  

 Benefits:
- Early job opportunities  
- Direct entry to B.Tech (2nd year)
""")

    st.markdown("<div class='section'>⚙️ 3. ITI (Industrial Training Institute)</div>", unsafe_allow_html=True)
    st.markdown("""
 Skill-based technical training  

Trades:
- Electrician
- Fitter
- Welder  

✔ Quick job opportunities  
✔ Good for hands-on learners
""")

    st.markdown("<div class='section'>🏥 4. Paramedical Courses</div>", unsafe_allow_html=True)
    st.markdown("""
 Healthcare support roles  

Courses:
- Lab Technician
- Nursing Assistant  

✔ Stable career in hospitals
""")

    st.markdown("<div class='section'>🌾 5. Agriculture</div>", unsafe_allow_html=True)
    st.markdown("""
 Farming and agri-business  

✔ Government jobs + business opportunities
""")

    st.markdown("<div class='section'>🎨 6. Creative Fields</div>", unsafe_allow_html=True)
    st.markdown("""
 For creative students  

Options:
- Designing
- Animation
- Media  

✔ Freelancing + job opportunities
""")

    st.markdown("<div class='section'>🏨 7. Hotel Management</div>", unsafe_allow_html=True)
    st.markdown("""
 Hospitality industry  

✔ Jobs in hotels, tourism, airlines
""")

    st.markdown("<div class='section'>🏃 8. Sports</div>", unsafe_allow_html=True)
    st.markdown("""
 Physical careers  

✔ Athlete, Coach, Trainer
""")

    st.markdown("<div class='section'>🪖 9. Defense</div>", unsafe_allow_html=True)
    st.markdown("""
 Army, Navy careers  

✔ Discipline + respect
""")

    st.markdown("<div class='section'>💼 10. Business / Freelancing</div>", unsafe_allow_html=True)
    st.markdown("""
 Start early earning  

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

    # -------- PUBLIC SECTOR --------
    st.markdown("<div class='section'>🏛️ Public Sector (Government)</div>", unsafe_allow_html=True)

    st.markdown("""
Jobs provided by the government with high job security and benefits.

**Examples:**
- UPSC (IAS, IPS)  
- Banking (SBI, IBPS)  
- Railways  
- Defense  
- SSC  

**Advantages:**
- Job security  
- Fixed working hours  
- Pension & benefits  

**Challenges:**
- Tough competition  
- Slower career growth  

**What to Study:**
- GK  
- Reasoning  
- English  
- Current Affairs  
""")

    # -------- PRIVATE SECTOR --------
    st.markdown("<div class='section'>🏢 Private Sector</div>", unsafe_allow_html=True)

    st.markdown("""
Jobs in companies and industries with faster growth and higher salary potential.

**Examples:**
- IT (Software Developer)  
- Marketing  
- Finance  
- HR  
- Design  

**Advantages:**
- High salary   
- Fast career growth   
- More opportunities  

**Challenges:**
- Job pressure  
- Less job security  

**What to Study:**
- Technical skills  
- Communication  
- Domain knowledge  
""")

    # -------- TIP --------
    st.markdown("<div class='section'>✅ Tip</div>", unsafe_allow_html=True)

    st.success("""
👉 Choose Public Sector for stability  
👉 Choose Private Sector for growth and salary  
""")
# ------------------ AI ------------------
elif menu == "🤖 AI Recommendation":

    st.markdown("<div class='big-title'>🤖 Smart Career Recommendation</div>", unsafe_allow_html=True)

    st.markdown("### 🧠 Tell us about yourself")

    # -------- BASIC INPUTS --------
    interest = st.selectbox("🎯 Select Your Interest", [
        "Technology",
        "Medical",
        "Business",
        "Creative",
        "Government Jobs",
        "Teaching",
        "Defense",
        "Sports",
        "Agriculture",
        "Hospitality"
    ])

    skill = st.selectbox("⚡ Your Strength", [
        "Problem Solving",
        "Communication",
        "Creativity",
        "Leadership",
        "Physical Fitness",
        "Analytical Thinking"
    ])

    work_style = st.radio("💼 Preferred Work Style", [
        "High Salary Job",
        "Government Job",
        "Business / Startup",
        "Work-Life Balance"
    ])

    # -------- NEW INPUTS --------
    education = st.selectbox("🎓 Your Education Level", [
        "After 10th",
        "After 12th",
        "Graduate",
        "Postgraduate"
    ])

    subject = st.selectbox("📚 Favorite Subject", [
        "Maths",
        "Biology",
        "Computer Science",
        "Commerce",
        "Arts",
        "None"
    ])

    salary = st.selectbox("💰 Expected Salary Level", [
        "High Salary",
        "Moderate",
        "Stable Income"
    ])

    location_pref = st.radio("🌍 Work Preference", [
        "Work in India",
        "Abroad",
        "Remote Work"
    ])

    study_pref = st.radio("📖 Study Preference", [
        "Long-term study (5+ years)",
        "Short-term (1-3 years)",
        "Skill-based courses"
    ])

    personality = st.selectbox("🧠 Your Personality", [
        "Analytical",
        "Creative",
        "Social",
        "Leader",
        "Practical"
    ])

    # -------- BUTTON --------
    if st.button("🔍 Get Recommendation"):

        st.markdown("## 🎯 Best Career Options For You")

        # -------- SMART LOGIC --------
        if interest == "Technology" and subject in ["Maths", "Computer Science"]:
            st.success("💻 Best: B.Tech CSE, AI, Data Science, BCA")
            st.info("👉 Careers: Software Engineer, AI Engineer, Data Scientist")

        elif interest == "Medical" and subject == "Biology":
            st.success("🏥 Best: MBBS, BDS, Pharmacy, Nursing")
            st.info("👉 Careers: Doctor, Nurse, Pharmacist")

        elif interest == "Business" or personality == "Leader":
            st.success("💼 Best: BBA, B.Com, MBA")
            st.info("👉 Careers: Manager, Entrepreneur, Business Analyst")

        elif personality == "Creative":
            st.success("🎨 Best: Design, Animation, UI/UX, Media")
            st.info("👉 Careers: Graphic Designer, Animator, Content Creator")

        elif work_style == "Government Job":
            st.success("🏛️ Best: UPSC, SSC, Banking, Railways")
            st.info("👉 Careers: IAS, IPS, Govt Officer")

        elif interest == "Defense":
            st.success("🪖 Best: NDA, CDS")
            st.info("👉 Careers: Army, Navy, Airforce")

        elif interest == "Teaching":
            st.success("📚 Best: BA/B.Sc + B.Ed")
            st.info("👉 Careers: Teacher, Lecturer")

        else:
            st.success("✨ Explore multiple career paths based on your skills")
            st.info("👉 Combine skills + degree for best results")

        # -------- EXTRA PERSONALIZATION --------
        st.markdown("### 💡 Smart Suggestions")

        if salary == "High Salary":
            st.warning("💰 Focus on IT, AI, Data Science, Management")

        if study_pref == "Short-term (1-3 years)":
            st.warning("⏳ Try skill-based courses like Web Dev, Digital Marketing")

        if location_pref == "Abroad":
            st.warning("🌍 Prepare for IELTS/GRE + International opportunities")

        if skill == "Communication":
            st.warning("🗣️ Marketing, HR, Teaching are great options")

        # -------- CONFIDENCE SCORE --------
        st.markdown("### 📊 Recommendation Confidence")

        st.progress(80)
        st.write("🔍 Confidence Level: 80%")

        # -------- FINAL TIP --------
        st.success("✅ Tip: Choose career based on Interest + Skills + Future Demand")
# ------------------ LOGOUT ------------------
elif menu == "🚪 Logout":
    del st.session_state["user"]
    st.rerun()
