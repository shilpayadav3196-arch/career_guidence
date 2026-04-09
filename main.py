import streamlit as st
import json, os
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import plotly.express as px

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Career Guidance System", layout="wide")

# ---------------- SESSION ----------------
if "user" not in st.session_state:
    st.session_state.user = None
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------------- USER DB ----------------
USER_FILE = "users.json"

def load_users():
    if os.path.exists(USER_FILE):
        return json.load(open(USER_FILE))
    return {}

def save_users(users):
    json.dump(users, open(USER_FILE, "w"))

users = load_users()

# ---------------- LOGIN ----------------
def login():
    st.title("🔐 Login / Signup")
    opt = st.radio("Choose", ["Login", "Signup"])
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if opt == "Signup":
        if st.button("Create Account"):
            if user in users:
                st.error("User exists")
            else:
                users[user] = pwd
                save_users(users)
                st.success("Account created")

    if opt == "Login":
        if st.button("Login"):
            if user in users and users[user] == pwd:
                st.session_state.user = user
                st.rerun()
            else:
                st.error("Invalid login")

if not st.session_state.user:
    login()
    st.stop()

# ---------------- MODEL ----------------
@st.cache_resource
def load_model():
    df = pd.read_csv("career_data_1000.csv")

    le1, le2, le3, le4, le5 = LabelEncoder(), LabelEncoder(), LabelEncoder(), LabelEncoder(), LabelEncoder()

    df["interest"] = le1.fit_transform(df["interest"])
    df["skill"] = le2.fit_transform(df["skill"])
    df["subject"] = le3.fit_transform(df["subject"])
    df["personality"] = le4.fit_transform(df["personality"])
    df["career"] = le5.fit_transform(df["career"])

    X = df[["interest","skill","subject","personality"]]
    y = df["career"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    acc = model.score(X_test, y_test)

    return model, le1, le2, le3, le4, le5, acc

model, le1, le2, le3, le4, le5, accuracy = load_model()

# ---------------- STYLE ----------------
st.markdown("""
<style>
.card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    transition: 0.3s;
    height: 180px;
}
.card:hover {
    transform: translateY(-8px);
}
.tag {
    background:#c62828;
    color:white;
    padding:5px 10px;
    border-radius:8px;
    font-size:12px;
}
.title {font-size:20px;font-weight:bold;}
.desc {font-size:14px;color:gray;}
.stButton>button {
    height:200px;width:100%;
    background:transparent;border:none;
}
</style>
""", unsafe_allow_html=True)

page = st.session_state.page

# ---------------- DASHBOARD ----------------
if page == "home":
    st.title("🎯 Career Guidance Dashboard")

    col1,col2,col3 = st.columns(3)

    with col1:
        if st.button(" "):
            st.session_state.page="after10"; st.rerun()
        st.markdown('<div class="card"><div class="tag">AFTER 10TH</div><div class="title">Career Paths</div><div class="desc">All options after 10th</div></div>',unsafe_allow_html=True)

    with col2:
        if st.button("  "):
            st.session_state.page="after12"; st.rerun()
        st.markdown('<div class="card"><div class="tag">AFTER 12TH</div><div class="title">Higher Studies</div></div>',unsafe_allow_html=True)

    with col3:
        if st.button("   "):
            st.session_state.page="ai"; st.rerun()
        st.markdown('<div class="card"><div class="tag">AI</div><div class="title">Smart Recommendation</div></div>',unsafe_allow_html=True)

    col4,col5,col6 = st.columns(3)

    with col4:
        if st.button("    "):
            st.session_state.page="sectors"; st.rerun()
        st.markdown('<div class="card"><div class="tag">SECTORS</div><div class="title">Govt vs Private</div></div>',unsafe_allow_html=True)

    with col5:
        if st.button("     "):
            st.session_state.page="analysis"; st.rerun()
        st.markdown('<div class="card"><div class="tag">ANALYSIS</div><div class="title">Insights</div></div>',unsafe_allow_html=True)

    with col6:
        if st.button("      "):
            st.session_state.page="logout"; st.rerun()
        st.markdown('<div class="card"><div class="tag">EXIT</div><div class="title">Logout</div></div>',unsafe_allow_html=True)

    st.success(f"Model Accuracy: {accuracy*100:.2f}%")

# ---------------- AFTER 10TH ----------------
elif page=="after10":
    st.title("🎓 After 10th")
    st.write("Science, Diploma, ITI, Agriculture, Creative, Defense")

    df=pd.read_csv("career_data_1000.csv")
    st.plotly_chart(px.histogram(df,x="interest",color="career"))

    if st.button("⬅ Back"): st.session_state.page="home"; st.rerun()

# ---------------- AFTER 12TH ----------------
elif page=="after12":
    st.title("📘 After 12th")
    st.write("Engineering, Medical, Commerce, Arts, Govt jobs")

    df=pd.read_csv("career_data_1000.csv")
    st.plotly_chart(px.bar(df["career"].value_counts()))

    if st.button("⬅ Back"): st.session_state.page="home"; st.rerun()

# ---------------- AI ----------------
elif page=="ai":
    st.title("🤖 AI Career Recommendation")

    df=pd.read_csv("career_data_1000.csv")

    i=st.selectbox("Interest",df["interest"].unique())
    s=st.selectbox("Skill",df["skill"].unique())
    sub=st.selectbox("Subject",df["subject"].unique())
    p=st.selectbox("Personality",df["personality"].unique())

    if st.button("Predict"):
        data=[[le1.transform([i])[0],le2.transform([s])[0],le3.transform([sub])[0],le4.transform([p])[0]]]
        pred=model.predict(data)
        st.success(le5.inverse_transform(pred)[0])

    if st.button("⬅ Back"): st.session_state.page="home"; st.rerun()

# ---------------- SECTORS ----------------
elif page=="sectors":
    st.title("💼 Career Sectors")
    st.write("Government vs Private sector details")
    if st.button("⬅ Back"): st.session_state.page="home"; st.rerun()

# ---------------- ANALYSIS ----------------
elif page=="analysis":
    st.title("📊 Insights")
    df=pd.read_csv("career_data_1000.csv")
    st.plotly_chart(px.scatter(df,x="interest",y="skill",color="career"))
    if st.button("⬅ Back"): st.session_state.page="home"; st.rerun()

# ---------------- LOGOUT ----------------
elif page=="logout":
    del st.session_state.user
    st.rerun()
