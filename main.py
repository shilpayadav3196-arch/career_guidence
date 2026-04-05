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

# ------------------ ML MODEL ------------------
@st.cache_resource
def load_model():
    file_path = os.path.join(os.getcwd(), "career_data_1000.csv")
    
    if not os.path.exists(file_path):
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

# ------------------ AI RECOMMENDATION ------------------
elif menu == "🤖 AI Recommendation":

    st.markdown("<div class='big-title'>🤖 Smart Career Recommendation</div>", unsafe_allow_html=True)

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

    if st.button("🔍 Get Recommendation"):

        st.markdown("## 🎯 Best Career Option For You")

        try:
            input_data = [[
                le_interest.transform([interest])[0],
                le_skill.transform([skill])[0],
                le_subject.transform([subject])[0],
                le_personality.transform([personality])[0]
            ]]

            prediction = model.predict(input_data)
            career = le_career.inverse_transform(prediction)

            st.success(f"👉 Recommended Career: {career[0]}")
            st.write(f"📊 Model Accuracy: {accuracy*100:.2f}%")

        except:
            st.error("⚠️ Input not matching dataset")

# ------------------ LOGOUT ------------------
elif menu == "🚪 Logout":
    del st.session_state["user"]
    st.rerun()
