import streamlit as st
import json
import os

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Career Guidance System", page_icon="🎯", layout="wide")

# ------------------ PREMIUM CSS ------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #1f1c2c, #928dab);
    color: white;
}
.card {
    background: rgba(255, 255, 255, 0.1);
    padding: 20px;
    border-radius: 15px;
    backdrop-filter: blur(10px);
    margin: 10px 0;
}
.title {
    font-size: 36px;
    text-align:center;
    font-weight:bold;
}
.stButton>button {
    background: linear-gradient(45deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 10px;
}
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
    st.markdown("<div class='title'>🔐 Login System</div>", unsafe_allow_html=True)

    option = st.radio("", ["Login", "Signup"])
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if option == "Signup":
        if st.button("Create Account"):
            users[user] = pwd
            save_users(users)
            st.success("Account created")

    if option == "Login":
        if st.button("Login"):
            if user in users and users[user] == pwd:
                st.session_state["user"] = user
                st.rerun()
            else:
                st.error("Invalid")

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
    st.markdown("<div class='title'>🎯 Career Guidance System</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    col1.markdown("<div class='card'>🎓 50+ Career Options</div>", unsafe_allow_html=True)
    col2.markdown("<div class='card'>💼 Govt + Private Jobs</div>", unsafe_allow_html=True)
    col3.markdown("<div class='card'>🤖 AI Guidance</div>", unsafe_allow_html=True)

# ------------------ AFTER 10TH ------------------
elif menu == "🎓 After 10th":
    st.markdown("<div class='title'>🎓 After 10th Guide</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>1️⃣ Intermediate (Science, Commerce, Arts)</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>2️⃣ Diploma (Engineering fields)</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>3️⃣ ITI (Technical jobs)</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>4️⃣ Paramedical (Healthcare)</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>5️⃣ Agriculture</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>6️⃣ Vocational Courses</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>7️⃣ Creative Fields</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>8️⃣ Hotel Management</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>9️⃣ Sports</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>🔟 Defense</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>1️⃣1️⃣ Open School</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>1️⃣2️⃣ Business</div>", unsafe_allow_html=True)

# ------------------ AFTER 12TH ------------------
elif menu == "📘 After 12th":
    st.markdown("<div class='title'>📘 After 12th Full Guide</div>", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["🎯 Studies", "🪖 Govt Jobs", "🛠 Courses", "🚀 Careers"])

    with tab1:
        st.markdown("<div class='card'>Engineering, Medical, BCA, BBA, BA</div>", unsafe_allow_html=True)

    with tab2:
        st.markdown("<div class='card'>NDA, SSC, Railways, Police</div>", unsafe_allow_html=True)

    with tab3:
        st.markdown("<div class='card'>IT, Paramedical, Design, Law</div>", unsafe_allow_html=True)

    with tab4:
        st.markdown("<div class='card'>Freelancing, Business, YouTube</div>", unsafe_allow_html=True)

# ------------------ CAREER SECTOR ------------------
elif menu == "💼 Career Sectors":
    st.markdown("<div class='title'>💼 Career Sectors</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    col1.markdown("<div class='card'>🏛 Govt Jobs<br>UPSC, Banking, Railways</div>", unsafe_allow_html=True)
    col2.markdown("<div class='card'>🏢 Private Jobs<br>IT, Marketing</div>", unsafe_allow_html=True)

# ------------------ AI RECOMMEND ------------------
elif menu == "🤖 AI Recommendation":
    st.markdown("<div class='title'>🤖 Career Recommendation</div>", unsafe_allow_html=True)

    interest = st.selectbox("Interest", ["Technology", "Biology", "Business", "Creative"])

    if st.button("Get Career"):
        st.balloons()
        st.success("Best career generated!")

# ------------------ LOGOUT ------------------
elif menu == "🚪 Logout":
    del st.session_state["user"]
    st.rerun()
