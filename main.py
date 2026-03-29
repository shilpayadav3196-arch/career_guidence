import streamlit as st
import json
import os
import time

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Career Guidance System", page_icon="🎯", layout="wide")

# ------------------ SIMPLE USER DATABASE ------------------
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
def typing_animation(text):
    placeholder = st.empty()
    for i in range(len(text) + 1):
        placeholder.markdown(f"### {text[:i]}")
        time.sleep(0.02)

# ------------------ LOGIN / SIGNUP ------------------
def login_signup():
    st.title("🔐 Login / Signup")

    option = st.radio("Select Option", ["Login", "Signup"])

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
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid credentials")

# ------------------ MAIN APP ------------------
if "user" not in st.session_state:
    login_signup()
    st.stop()

# ------------------ SIDEBAR ------------------
st.sidebar.title(f"👋 Welcome {st.session_state['user']}")

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
    typing_animation("🎯 AI Career Guidance System")

    st.write("""
    This system helps students choose the best career path based on their interests.
    """)

# ------------------ AFTER 10TH ------------------
elif menu == "🎓 After 10th":
    st.title("🎓 Career Options After 10th")

    st.subheader("1️⃣ Intermediate (11th & 12th)")

    st.markdown("### 🔬 Science Stream")
    st.write("""
    Subjects: Physics, Chemistry, Maths/Biology

    Careers:
    - Engineering (B.Tech)
    - AI/ML, Data Science
    - NDA
    - MBBS, BDS, Pharmacy

    Skills: Logical thinking, problem solving
    """)

    st.markdown("### 💼 Commerce Stream")
    st.write("""
    Careers:
    - CA, CS
    - BBA, MBA
    - Banking & Finance
    """)

    st.markdown("### 🎨 Arts Stream")
    st.write("""
    Careers:
    - UPSC (IAS, IPS)
    - Lawyer
    - Journalism
    """)

    st.subheader("2️⃣ Diploma")
    st.write("Mechanical, Civil, Computer Engineering")

    st.subheader("3️⃣ ITI")
    st.write("Electrician, Fitter, Mechanic")

    st.subheader("4️⃣ Skill Courses")
    st.write("Digital Marketing, Web Dev, Animation")

    st.subheader("5️⃣ Defense")
    st.write("Army, Navy, Air Force")

# ------------------ AFTER 12TH ------------------
elif menu == "📘 After 12th":
    st.title("📘 Career Options After 12th")

    stream = st.selectbox("Choose Stream", ["Science", "Commerce", "Arts"])

    if stream == "Science":
        st.write("""
        - Engineering (CSE, AI/ML)
        - MBBS
        - Data Science
        - Cyber Security
        """)

    elif stream == "Commerce":
        st.write("""
        - CA
        - B.Com
        - MBA
        - Banking
        """)

    elif stream == "Arts":
        st.write("""
        - UPSC
        - Law
        - Journalism
        """)

# ------------------ CAREER SECTORS ------------------
elif menu == "💼 Career Sectors":
    st.title("💼 Public vs Private Sector")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🏛️ Government Jobs")
        st.write("""
        - UPSC (IAS, IPS)
        - Banking (SBI, RBI)
        - Railways
        - Defense (Army/Navy)
        """)

    with col2:
        st.subheader("🏢 Private Jobs")
        st.write("""
        - Software Engineer
        - Data Scientist
        - Digital Marketing
        - Business Jobs
        """)

# ------------------ AI RECOMMENDATION ------------------
elif menu == "🤖 AI Recommendation":
    st.title("🤖 Career Recommendation")

    interest = st.selectbox("Your Interest", ["Technology", "Biology", "Business", "Arts"])
    skill = st.selectbox("Your Skill Level", ["High", "Medium", "Low"])

    if st.button("Get Recommendation"):
        if interest == "Technology":
            st.success("👉 Recommended: AI Engineer / Software Developer")

        elif interest == "Biology":
            st.success("👉 Recommended: Doctor / Pharmacy")

        elif interest == "Business":
            st.success("👉 Recommended: CA / MBA")

        else:
            st.success("👉 Recommended: UPSC / Law")

# ------------------ LOGOUT ------------------
elif menu == "🚪 Logout":
    del st.session_state["user"]
    st.rerun()
