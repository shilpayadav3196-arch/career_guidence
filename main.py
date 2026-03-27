import streamlit as st
import pandas as pd
import sqlite3
import joblib
import os
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# -------------------- CONFIG --------------------
st.set_page_config(page_title="AI Career Guidance", layout="wide")

# -------------------- DATABASE --------------------
conn = sqlite3.connect("users.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")

def add_user(u, p):
    c.execute("INSERT INTO users VALUES (?,?)", (u, p))
    conn.commit()

def login_user(u, p):
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (u, p))
    return c.fetchall()

# -------------------- LOAD DATA --------------------
FILE = "final_career_dataset_5000.csv"
data = pd.read_csv(FILE)

# -------------------- TRAIN MODEL --------------------
if not os.path.exists("model.pkl"):

    data.fillna(method="ffill", inplace=True)

    encoders = {}
    for col in data.columns:
        if data[col].dtype == "object":
            le = LabelEncoder()
            data[col] = le.fit_transform(data[col])
            encoders[col] = le

    X = data.drop(["Career", "Sector"], axis=1)
    y = data["Career"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)

    joblib.dump(model, "model.pkl")
    joblib.dump(encoders, "encoders.pkl")
    joblib.dump(accuracy, "accuracy.pkl")

# -------------------- LOAD MODEL --------------------
model = joblib.load("model.pkl")
encoders = joblib.load("encoders.pkl")
accuracy = joblib.load("accuracy.pkl")

# -------------------- SESSION --------------------
if "page" not in st.session_state:
    st.session_state.page = "login"

if "user_input" not in st.session_state:
    st.session_state.user_input = {}

# -------------------- NAVIGATION --------------------
def go(page):
    st.session_state.page = page
    st.rerun()

# -------------------- LOGIN PAGE --------------------
if st.session_state.page == "login":

    st.title("🔐 Login / Sign Up")

    menu = st.radio("", ["Login", "Sign Up"], horizontal=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if menu == "Sign Up":
        if st.button("Register"):
            add_user(username, password)
            st.success("Account Created ✅")

    else:
        if st.button("Login"):
            if login_user(username, password):
                st.success("Login Successful ✅")
                go("dashboard")
            else:
                st.error("Invalid Credentials ❌")

# -------------------- DASHBOARD --------------------
elif st.session_state.page == "dashboard":

    st.title("📊 Dashboard")
    st.success("Welcome! Enter your details 👇")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Name")
        marks = st.slider("Marks (%)", 0, 100)
        iq = st.slider("IQ", 80, 150)

        stage = st.selectbox("Study Stage", [
            "After 10th", "After 12th", "Graduate"
        ])

    with col2:
        interest = st.selectbox("Interest", [
            "AI", "Data Science", "Web Development", "Cyber Security",
            "Finance", "Healthcare", "Marketing", "Law", "Design", "Education"
        ])

        skill = st.selectbox("Skill", [
            "Python", "ML", "HTML", "CSS", "JavaScript",
            "Biology", "Finance", "Communication", "Design"
        ])

        hobby = st.selectbox("Hobby", [
            "Coding", "Reading", "Gaming", "Sports", "Music", "Art"
        ])

        personality = st.selectbox("Personality", [
            "Introvert", "Extrovert", "Ambivert"
        ])

        sector = st.selectbox("Preferred Sector", [
            "Private", "Government", "Startup", "Higher Studies"
        ])

    st.info(f"📊 Model Accuracy: {accuracy*100:.2f}%")

    if st.button("Next ➡"):
        st.session_state.user_input = {
            "Marks": marks,
            "Interest": interest,
            "Skill": skill,
            "Hobby": hobby,
            "Personality": personality,
            "IQ": iq,
            "Sector": sector,
            "Stage": stage,
            "Name": name
        }
        go("result")

# -------------------- RESULT PAGE --------------------
elif st.session_state.page == "result":

    st.title("🎯 Career Result")

    user = st.session_state.user_input

    # Encode
    input_data = []
    cols = ["Marks", "Interest", "Skill", "Hobby", "Personality", "IQ"]

    for col in cols:
        if col in encoders:
            input_data.append(encoders[col].transform([user[col]])[0])
        else:
            input_data.append(user[col])

    pred = model.predict([input_data])[0]
    prob = model.predict_proba([input_data])[0]

    career = encoders["Career"].inverse_transform([pred])[0]

    # Sector logic
    if user["Sector"] == "Government":
        career = "UPSC / Govt Job"
        sector = "Public"
    elif user["Sector"] == "Startup":
        career = "Startup Founder"
        sector = "Private"
    elif user["Sector"] == "Higher Studies":
        career = "M.Tech / MBA / MS"
        sector = "Education"
    else:
        sector = "Private"

    confidence = max(prob) * 100

    st.success(f"👤 {user['Name']}, Recommended Career: {career}")
    st.info(f"🏢 Sector: {sector}")
    st.write(f"📊 Confidence: {confidence:.2f}%")

    # -------------------- FLOW GUIDANCE --------------------
    st.subheader("🧭 Career Path Guidance")

    if user["Stage"] == "After 10th":
        st.write("10th → Choose Stream (Science/Commerce/Arts) → 12th → Degree → Career")
    elif user["Stage"] == "After 12th":
        st.write("12th → Degree / Professional Course → Career")
    else:
        st.write("Graduation → Job / Higher Studies / Startup")

    # -------------------- NAVIGATION --------------------
    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅ Previous"):
            go("dashboard")

    with col2:
        if st.button("🏠 Restart"):
            go("login")