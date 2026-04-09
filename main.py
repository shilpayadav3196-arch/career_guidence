import streamlit as st
import json, os
import pandas as pd
import plotly.express as px
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Career Guidance", layout="wide")

# ---------------- SESSION ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

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

    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

    model = DecisionTreeClassifier()
    model.fit(X_train,y_train)

    acc = model.score(X_test,y_test)

    return model, le1, le2, le3, le4, le5, acc

model, le1, le2, le3, le4, le5, accuracy = load_model()

# ---------------- STYLE ----------------
st.markdown("""
<style>
.card {
    background:white;
    padding:25px;
    border-radius:18px;
    box-shadow:0 4px 12px rgba(0,0,0,0.1);
    transition:0.3s;
}
.card:hover {transform:translateY(-8px);}
.stButton>button {
    height:180px;width:100%;
    background:transparent;border:none;
}
</style>
""", unsafe_allow_html=True)

page = st.session_state.page

# ---------------- HOME ----------------
if page == "home":
    st.title("🎯 Career Guidance Dashboard")

    col1,col2,col3 = st.columns(3)

    with col1:
        if st.button(" "):
            st.session_state.page="after10"; st.rerun()
        st.markdown("<div class='card'><h3>🎓 After 10th</h3><p>All career options</p></div>",unsafe_allow_html=True)

    with col2:
        if st.button("  "):
            st.session_state.page="after12"; st.rerun()
        st.markdown("<div class='card'><h3>📘 After 12th</h3></div>",unsafe_allow_html=True)

    with col3:
        if st.button("   "):
            st.session_state.page="ai"; st.rerun()
        st.markdown("<div class='card'><h3>🤖 AI Recommendation</h3></div>",unsafe_allow_html=True)

# ---------------- AFTER 10TH ----------------
elif page=="after10":
    st.title("🎓 Career Options After 10th")

    st.markdown("### 📚 Intermediate (11th & 12th)")
    st.write("""
Science (MPC/BiPC), Commerce, Arts  
✔ Leads to Engineering, Medical, Business
""")

    st.markdown("### 🛠️ Polytechnic")
    st.write("Mechanical, Civil, CSE → Early jobs + B.Tech entry")

    st.markdown("### ⚙️ ITI")
    st.write("Electrician, Fitter → Quick jobs")

    st.markdown("### 🎨 Creative Fields")
    st.write("Design, Animation → Freelancing")

    st.markdown("### 💼 Business")
    st.write("Start earning early")

    # -------- GRAPH --------
    df = pd.read_csv("career_data_1000.csv")

    st.subheader("📊 Interest vs Career")
    fig = px.histogram(df, x="interest", color="career")
    st.plotly_chart(fig, use_container_width=True)

    if st.button("⬅ Back"):
        st.session_state.page="home"; st.rerun()

# ---------------- AFTER 12TH ----------------
elif page=="after12":
    st.title("📘 Career Options After 12th")

    st.markdown("### 🔬 Science")
    st.write("B.Tech, MBBS → Engineer, Doctor")

    st.markdown("### 💼 Commerce")
    st.write("B.Com, CA → Accountant")

    st.markdown("### 🎨 Arts")
    st.write("BA, Law → Lawyer")

    st.markdown("### 💻 Skills")
    st.write("AI, Web Dev → Fast jobs")

    df = pd.read_csv("career_data_1000.csv")

    st.subheader("📊 Career Popularity")
    st.plotly_chart(px.bar(df["career"].value_counts()))

    if st.button("⬅ Back"):
        st.session_state.page="home"; st.rerun()

# ---------------- AI ----------------
elif page=="ai":
    st.title("🤖 Smart Recommendation")

    df = pd.read_csv("career_data_1000.csv")

    i = st.selectbox("Interest", df["interest"].unique())
    s = st.selectbox("Skill", df["skill"].unique())
    sub = st.selectbox("Subject", df["subject"].unique())
    p = st.selectbox("Personality", df["personality"].unique())

    if st.button("Predict"):
        data=[[le1.transform([i])[0],le2.transform([s])[0],le3.transform([sub])[0],le4.transform([p])[0]]]
        pred=model.predict(data)
        st.success(le5.inverse_transform(pred)[0])
        st.write(f"Accuracy: {accuracy*100:.2f}%")

    if st.button("⬅ Back"):
        st.session_state.page="home"; st.rerun()
