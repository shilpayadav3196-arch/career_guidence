import streamlit as st
import pandas as pd
import os
import json
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ------------------ CONFIG ------------------
st.set_page_config(page_title="Career Guidance", page_icon="🎯", layout="wide")

# ------------------ SESSION ------------------
if "user" not in st.session_state:
    st.session_state.user = None

if "page" not in st.session_state:
    st.session_state.page = "home"

# ------------------ LOGIN SYSTEM ------------------
USER_FILE = "users.json"

def load_users():
    if os.path.exists(USER_FILE):
        return json.load(open(USER_FILE))
    return {}

def save_users(users):
    json.dump(users, open(USER_FILE, "w"))

users = load_users()

def login():
    st.title("🔐 Login / Signup")
    option = st.radio("Choose", ["Login", "Signup"])
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if option == "Signup":
        if st.button("Create Account"):
            if user in users:
                st.error("User exists")
            else:
                users[user] = pwd
                save_users(users)
                st.success("Account created")

    if option == "Login":
        if st.button("Login"):
            if user in users and users[user] == pwd:
                st.session_state.user = user
                st.rerun()
            else:
                st.error("Invalid login")

if not st.session_state.user:
    login()
    st.stop()

# ------------------ MODEL ------------------
@st.cache_resource
def load_model():
    df = pd.read_csv("career_data_1000.csv")

    le1, le2, le3, le4, le5 = LabelEncoder(), LabelEncoder(), LabelEncoder(), LabelEncoder(), LabelEncoder()

    df["interest"] = le1.fit_transform(df["interest"])
    df["skill"] = le2.fit_transform(df["skill"])
    df["subject"] = le3.fit_transform(df["subject"])
    df["personality"] = le4.fit_transform(df["personality"])
    df["career"] = le5.fit_transform(df["career"])

    X = df[["interest", "skill", "subject", "personality"]]
    y = df["career"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    acc = accuracy_score(y_test, model.predict(X_test))

    return model, le1, le2, le3, le4, le5, acc

model, le1, le2, le3, le4, le5, accuracy = load_model()

# ------------------ STYLE ------------------
st.markdown("""
<style>
.card {
    background-color: #ffffff;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    transition: 0.3s;
    height: 180px;
}
.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.2);
}
.tag {
    background: #c62828;
    color: white;
    padding: 5px 12px;
    border-radius: 8px;
    font-size: 12px;
}
.title {
    font-size: 20px;
    font-weight: bold;
    margin-top: 10px;
}
.desc {
    font-size: 14px;
    color: #555;
}
.stButton>button {
    height: 200px;
    width: 100%;
    border-radius: 18px;
    background-color: transparent;
    border: none;
}
</style>
""", unsafe_allow_html=True)

page = st.session_state.page

# ------------------ HOME DASHBOARD ------------------
if page == "home":

    st.markdown("## 🎯 AI Career Guidance Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button(" "):
            st.session_state.page = "after10"
            st.rerun()
        st.markdown("""
        <div class="card">
            <div class="tag">AFTER 10TH</div>
            <div class="title">Career Paths</div>
            <div class="desc">Explore streams, diploma, ITI & skill careers.</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        if st.button("  "):
            st.session_state.page = "after12"
            st.rerun()
        st.markdown("""
        <div class="card">
            <div class="tag">AFTER 12TH</div>
            <div class="title">Higher Studies</div>
            <div class="desc">Engineering, Medical, Commerce & more.</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        if st.button("   "):
            st.session_state.page = "ai"
            st.rerun()
        st.markdown("""
        <div class="card">
            <div class="tag">AI SYSTEM</div>
            <div class="title">Smart Recommendation</div>
            <div class="desc">Get AI-based career suggestions.</div>
        </div>
        """, unsafe_allow_html=True)

    col4, col5, col6 = st.columns(3)

    with col4:
        if st.button("    "):
            st.session_state.page = "analysis"
            st.rerun()
        st.markdown("""
        <div class="card">
            <div class="tag">SKILL ANALYSIS</div>
            <div class="title">Interest Mapping</div>
            <div class="desc">Match skills with careers.</div>
        </div>
        """, unsafe_allow_html=True)

    with col5:
        if st.button("     "):
            st.session_state.page = "sectors"
            st.rerun()
        st.markdown("""
        <div class="card">
            <div class="tag">SECTORS</div>
            <div class="title">Govt vs Private</div>
            <div class="desc">Compare career sectors.</div>
        </div>
        """, unsafe_allow_html=True)

    with col6:
        if st.button("      "):
            st.session_state.page = "insights"
            st.rerun()
        st.markdown("""
        <div class="card">
            <div class="tag">ANALYTICS</div>
            <div class="title">Trend Mapping</div>
            <div class="desc">Dataset-based insights.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.success(f"📊 Model Accuracy: {accuracy*100:.2f}%")

# ------------------ AFTER 10TH ------------------
elif page == "after10":
    st.title("🎓 After 10th")
    df = pd.read_csv("career_data_1000.csv")
    st.bar_chart(df["interest"].value_counts())
    if st.button("⬅ Back"):
        st.session_state.page = "home"
        st.rerun()

# ------------------ AFTER 12TH ------------------
elif page == "after12":
    st.title("📘 After 12th")
    df = pd.read_csv("career_data_1000.csv")
    st.bar_chart(df["subject"].value_counts())
    if st.button("⬅ Back"):
        st.session_state.page = "home"
        st.rerun()

# ------------------ AI ------------------
elif page == "ai":
    st.title("🤖 AI Recommendation")

    df = pd.read_csv("career_data_1000.csv")

    i = st.selectbox("Interest", df["interest"].unique())
    s = st.selectbox("Skill", df["skill"].unique())
    sub = st.selectbox("Subject", df["subject"].unique())
    p = st.selectbox("Personality", df["personality"].unique())

    if st.button("Predict"):
        data = [[le1.transform([i])[0], le2.transform([s])[0], le3.transform([sub])[0], le4.transform([p])[0]]]
        pred = model.predict(data)
        career = le5.inverse_transform(pred)
        st.success(f"🎯 {career[0]}")

    if st.button("⬅ Back"):
        st.session_state.page = "home"
        st.rerun()

# ------------------ ANALYSIS ------------------
elif page == "analysis":
    st.title("🧠 Skill Analysis")
    df = pd.read_csv("career_data_1000.csv")
    st.scatter_chart(df[["interest","skill"]])
    if st.button("⬅ Back"):
        st.session_state.page = "home"
        st.rerun()

# ------------------ SECTORS ------------------
elif page == "sectors":
    st.title("💼 Career Sectors")
    st.write("Government vs Private Jobs")
    if st.button("⬅ Back"):
        st.session_state.page = "home"
        st.rerun()

# ------------------ INSIGHTS ------------------
elif page == "insights":
    st.title("📊 Insights")
    df = pd.read_csv("career_data_1000.csv")
    st.bar_chart(df["career"].value_counts())
    if st.button("⬅ Back"):
        st.session_state.page = "home"
        st.rerun()
