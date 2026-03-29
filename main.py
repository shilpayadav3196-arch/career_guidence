import streamlit as st
import json
import os
import time

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Career Guidance System", page_icon="🎯", layout="wide")

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

# ------------------ AUTH CHECK ------------------
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
    st.write("This system helps students choose the best career path based on their interests.")

# ------------------ AFTER 10TH ------------------
elif menu == "🎓 After 10th":
    st.title("🎓 Career Options After 10th (Complete Guide)")

    st.header("1️⃣ Intermediate (11th & 12th)")
    st.write("Streams: Science, Commerce, Arts")
    st.success("Best for long-term careers")

    st.header("2️⃣ Polytechnic Diploma")
    st.write("Fields: Mechanical, Civil, AI, Electronics")

    st.header("3️⃣ ITI")
    st.write("Trades: Electrician, CNC, AC Technician")

    st.header("4️⃣ Paramedical Courses")
    st.write("MLT, X-Ray, Dialysis Technician")

    st.header("5️⃣ Agriculture")
    st.write("Diploma in Agriculture, Fisheries")

    st.header("6️⃣ Vocational Courses")
    st.write("Retail, Tourism, Food Processing")

    st.header("7️⃣ Creative Fields")
    st.write("Animation, UI/UX, Fashion Design")

    st.header("8️⃣ Hotel Management")
    st.write("Hotel, Catering, Culinary Arts")

    st.header("9️⃣ Sports")
    st.write("Athlete, Coach, Trainer")

    st.header("🔟 Defense")
    st.write("Army, Navy, Sainik Schools")

    st.header("1️⃣1️⃣ Open Schooling")
    st.write("NIOS")

    st.header("1️⃣2️⃣ Business")
    st.write("Startups, Freelancing")

    st.header("📊 Comparison Table")
    st.table({
        "Path": ["Intermediate", "Diploma", "ITI", "Paramedical"],
        "Duration": ["2 yrs", "3 yrs", "1–2 yrs", "1–3 yrs"],
        "Growth": ["High", "High", "Medium", "High"]
    })

    st.header("💡 Best Path for AI/ML")
    st.success("10th → Science → B.Tech → AI Job")

# ------------------ AFTER 12TH ------------------
elif menu == "📘 After 12th":
    st.title("📘 Career Options After 12th")

    stream = st.selectbox("Choose Stream", ["Science", "Commerce", "Arts"])

    if stream == "Science":
        st.write("Engineering, MBBS, Data Science, AI")

    elif stream == "Commerce":
        st.write("CA, B.Com, MBA, Banking")

    elif stream == "Arts":
        st.write("UPSC, Law, Journalism")

# ------------------ CAREER SECTORS ------------------
elif menu == "💼 Career Sectors":
    st.title("💼 Public vs Private Sector")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🏛️ Government Jobs")
        st.write("UPSC, Banking, Railways, Defense")

    with col2:
        st.subheader("🏢 Private Jobs")
        st.write("Software, Data Science, Marketing")

# ------------------ AI RECOMMENDATION ------------------
elif menu == "🤖 AI Recommendation":
    st.title("🤖 Career Recommendation")

    interest = st.selectbox("Interest", ["Technology", "Biology", "Business", "Arts"])

    if st.button("Get Recommendation"):
        if interest == "Technology":
            st.success("AI Engineer / Developer")

        elif interest == "Biology":
            st.success("Doctor / Healthcare")

        elif interest == "Business":
            st.success("CA / MBA")

        else:
            st.success("UPSC / Law")

# ------------------ LOGOUT ------------------
elif menu == "🚪 Logout":
    del st.session_state["user"]
    st.rerun()
