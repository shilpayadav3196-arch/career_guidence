import streamlit as st
import json
import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

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
        if st.button("Create Account", key="signup_btn"):
            if user in users:
                st.error("User already exists")
            else:
                users[user] = pwd
                save_users(users)
                st.success("Account created")

    if option == "Login":
        if st.button("Login", key="login_btn"):
            if user in users and users[user] == pwd:
                st.session_state["user"] = user
                st.rerun()
            else:
                st.error("Invalid login")

if "user" not in st.session_state:
    login()
    st.stop()

# ------------------ ML MODEL ------------------
@st.cache_resource
def load_model():
    file_path = "career_data_1000.csv"

    if not os.path.exists(file_path):
        st.write("Available files:", os.listdir())
        st.error("❌ Dataset file not found. Upload career_data_1000.csv to GitHub.")
        st.stop()

    df = pd.read_csv(file_path)

    le_interest = LabelEncoder()
    le_skill = LabelEncoder()
    le_subject = LabelEncoder()
    le_personality = LabelEncoder()
    le_career = LabelEncoder()

    df["interest"] = le_interest.fit_transform(df["interest"])
    df["skill"] = le_skill.fit_transform(df["skill"])
    df["subject"] = le_subject.fit_transform(df["subject"])
    df["personality"] = le_personality.fit_transform(df["personality"])
    df["career"] = le_career.fit_transform(df["career"])

    X = df[["interest", "skill", "subject", "personality"]]
    y = df["career"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)

    return model, le_interest, le_skill, le_subject, le_personality, le_career, accuracy


model, le_interest, le_skill, le_subject, le_personality, le_career, accuracy = load_model()

# ------------------ SIDEBAR ------------------
menu = st.sidebar.radio("Menu", [
    "🏠 Home", "🎓 After 10th", "📘 After 12th",
    "💼 Career Sectors", "🤖 AI Recommendation", "🚪 Logout"
])
# ------------------ HOME ------------------
if menu == "🏠 Home":
    st.markdown("<div class='big-title'>🎯 Career Guidance System</div>", unsafe_allow_html=True)
    st.markdown("<div class='text'>This system helps students choose the best career path.</div>", unsafe_allow_html=True)


# ------------------ AFTER 10TH  ------------------
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

# ------------------ AFTER 12TH ------------------
elif menu == "📘 After 12th":

    st.markdown("<div class='big-title'>📘 Career Options After 12th</div>", unsafe_allow_html=True)

 
    # ------------------ CONTENT ------------------

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
# ------------------ AI ------------------
elif menu == "ai":

    st.title("🤖 AI Career Recommendation")

    df = pd.read_csv("career_data_1000.csv")

    interest = st.selectbox("Interest", df["interest"].unique())
    skill = st.selectbox("Skill", df["skill"].unique())
    subject = st.selectbox("Subject", df["subject"].unique())
    personality = st.selectbox("Personality", df["personality"].unique())

    if st.button("Predict"):

        input_data = [[
            le_interest.transform([interest])[0],
            le_skill.transform([skill])[0],
            le_subject.transform([subject])[0],
            le_personality.transform([personality])[0]
        ]]

        pred = model.predict(input_data)
        career = le_career.inverse_transform(pred)

        st.success(f"🎯 Recommended Career: {career[0]}")
        st.write(f"📊 Accuracy: {accuracy*100:.2f}%")

    if st.button("⬅ Back"):
        st.session_state.page = "home"
        st.rerun()
    interest = st.selectbox("🎯 Interest", [
        "Technology","Medical","Business","Creative","Government Jobs",
        "Teaching","Defense","Sports","Agriculture","Hospitality"
    ])

    skill = st.selectbox("⚡ Skill", [
        "Problem Solving","Communication","Creativity","Leadership",
        "Physical Fitness","Analytical Thinking","Practical"
    ])

    subject = st.selectbox("📚 Subject", [
        "Maths","Biology","Computer Science","Commerce","Arts","None"
    ])

    personality = st.selectbox("🧠 Personality", [
        "Analytical","Creative","Social","Leader","Practical"
    ])

    salary = st.selectbox("💰 Expected Salary Level", [
        "High Salary","Moderate","Stable Income"
    ])

    location_pref = st.radio("🌍 Work Preference", [
        "Work in India","Abroad","Remote Work"
    ])

    study_pref = st.radio("📖 Study Preference", [
        "Long-term study (5+ years)",
        "Short-term (1-3 years)",
        "Skill-based courses"
    ])

    # ✅ FIXED BUTTON
    if st.button("🔍 Get Recommendation", key="predict_btn"):

        st.markdown("## 🎯 Best Career Options For You")

        try:
            input_data = [[
                le_interest.transform([interest])[0],
                le_skill.transform([skill])[0],
                le_subject.transform([subject])[0],
                le_personality.transform([personality])[0]
            ]]

            prediction = model.predict(input_data)
            career = le_career.inverse_transform(prediction)

            st.success(f"🎯 Recommended Career: {career[0]}")
            st.write(f"📊 Model Accuracy: {accuracy*100:.2f}%")

        except:
            st.error("⚠️ Input not matching dataset")
# ------------------ ANALYSIS ------------------
elif menu == "analysis":

    st.title("🧠 Skill Analysis")

    df = pd.read_csv("career_data_1000.csv")

    st.subheader("📊 Interest vs Skill")
    st.scatter_chart(df[["interest", "skill"]])

    st.subheader("📊 Personality Distribution")
    st.bar_chart(df["personality"].value_counts())

    if st.button("⬅ Back"):
        st.session_state.page = "home"
        st.rerun()

# ------------------ SECTORS ------------------
elif menu == "sectors":

    st.title("💼 Career Sectors")

    st.write("""
    🏛️ Government: UPSC, Banking, Railways  
    🏢 Private: IT, Marketing, Finance  
    """)

    if st.button("⬅ Back"):
        st.session_state.page = "home"
        st.rerun()

# ------------------ INSIGHTS ------------------
elif menu == "insights":

    st.title("📊 Career Insights")

    df = pd.read_csv("career_data_1000.csv")

    st.subheader("📊 Career Distribution")
    st.bar_chart(df["career"].value_counts())

    st.subheader("📊 Subjects")
    st.bar_chart(df["subject"].value_counts())

    st.subheader("📊 Skills")
    st.bar_chart(df["skill"].value_counts())

    if st.button("⬅ Back"):
        st.session_state.page = "home"
        st.rerun()
        # -------- EXTRA FEATURES --------
        st.markdown("### 💡 Smart Suggestions")

        if salary == "High Salary":
            st.warning("💰 Focus on IT, AI, Data Science, Management")

        if study_pref == "Short-term (1-3 years)":
            st.warning("⏳ Try skill-based courses")

        if location_pref == "Abroad":
            st.warning("🌍 Prepare for IELTS/GRE")

        if skill == "Communication":
            st.warning("🗣️ Marketing, HR, Teaching are great options")

        st.markdown("### 📊 Recommendation Confidence")
        st.progress(85)
        st.write("🔍 Confidence Level: High")

        st.success("✅ Tip: Choose career based on Interest + Skills + Future Demand")
        
        

# ------------------ LOGOUT ------------------
elif menu == "🚪 Logout":
    del st.session_state["user"]
    st.rerun()                   
