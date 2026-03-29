import streamlit as st
import json, os
from sklearn.tree import DecisionTreeClassifier
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Career Guidance", layout="wide")

# ------------------ PREMIUM LIGHT UI ------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fbc2eb, #a6c1ee);
    color: #222;
}
.title {
    font-size: 36px;
    font-weight: bold;
    text-align:center;
}
.card {
    background: rgba(255,255,255,0.7);
    padding:20px;
    border-radius:15px;
    margin:10px 0;
}
.stButton>button {
    background: linear-gradient(45deg, #ff9a9e, #89f7fe);
    border-radius:10px;
    color:black;
}
</style>
""", unsafe_allow_html=True)

# ------------------ USER AUTH ------------------
USER_FILE = "users.json"

def load_users():
    return json.load(open(USER_FILE)) if os.path.exists(USER_FILE) else {}

def save_users(users):
    json.dump(users, open(USER_FILE, "w"))

users = load_users()

def login():
    st.markdown("<div class='title'>🔐 Login</div>", unsafe_allow_html=True)
    option = st.radio("", ["Login", "Signup"])
    u = st.text_input("Username")
    p = st.text_input("Password", type="password")

    if option == "Signup":
        if st.button("Create"):
            users[u] = p
            save_users(users)
            st.success("Account created")

    if option == "Login":
        if st.button("Login"):
            if u in users and users[u] == p:
                st.session_state["user"] = u
                st.rerun()
            else:
                st.error("Invalid login")

if "user" not in st.session_state:
    login()
    st.stop()

# ------------------ SIDEBAR ------------------
menu = st.sidebar.radio("Menu", [
    "🏠 Home","🎓 After 10th","📘 After 12th",
    "💼 Career Sectors","🤖 AI Recommendation",
    "💬 Chatbot","📄 Download Report","🚪 Logout"
])

# ------------------ ML MODEL ------------------
X = [
    [1,0,0],[0,1,0],[0,0,1]
]
y = ["Engineer","Doctor","Business"]

model = DecisionTreeClassifier()
model.fit(X,y)

# ------------------ HOME ------------------
if menu == "🏠 Home":
    st.markdown("<div class='title'>🎯 Career Guidance System</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>🎓 50+ Career Options Available</div>", unsafe_allow_html=True)

# ------------------ AFTER 10TH ------------------
elif menu == "🎓 After 10th":
    st.markdown("<div class='title'>After 10th Options</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>Science, Diploma, ITI, Paramedical, Business, Creative Fields</div>", unsafe_allow_html=True)

# ------------------ AFTER 12TH ------------------
elif menu == "📘 After 12th":
    st.markdown("<div class='title'>After 12th Guide</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>🎯 Engineering, Medical, BBA, BA, Law</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>🪖 NDA, SSC, Railways, Police</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>🛠 IT, Design, Healthcare</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>🚀 Freelancing, Business, YouTube</div>", unsafe_allow_html=True)

# ------------------ CAREER SECTOR ------------------
elif menu == "💼 Career Sectors":
    st.markdown("<div class='title'>Career Sectors</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>🏛 Govt + 🏢 Private Jobs</div>", unsafe_allow_html=True)

# ------------------ AI RECOMMENDATION ------------------
elif menu == "🤖 AI Recommendation":
    st.markdown("<div class='title'>AI Career Predictor</div>", unsafe_allow_html=True)

    interest = st.selectbox("Select Interest", ["Technology","Biology","Business"])

    if st.button("Predict Career"):
        if interest == "Technology":
            pred = model.predict([[1,0,0]])[0]
        elif interest == "Biology":
            pred = model.predict([[0,1,0]])[0]
        else:
            pred = model.predict([[0,0,1]])[0]

        st.success(f"Best Career: {pred}")
        st.session_state["career"] = pred

# ------------------ CHATBOT ------------------
elif menu == "💬 Chatbot":
    st.markdown("<div class='title'>AI Chatbot</div>", unsafe_allow_html=True)

    user_input = st.text_input("Ask something")

    if user_input:
        if "engineering" in user_input.lower():
            st.write("👉 You can choose B.Tech in CSE, AI, Mechanical.")
        elif "medical" in user_input.lower():
            st.write("👉 Options: MBBS, BDS, Nursing.")
        else:
            st.write("👉 Try asking about careers like engineering, business, medical.")

# ------------------ PDF REPORT ------------------
elif menu == "📄 Download Report":
    st.markdown("<div class='title'>Download Career Report</div>", unsafe_allow_html=True)

    if st.button("Generate PDF"):
        doc = SimpleDocTemplate("career_report.pdf")
        styles = getSampleStyleSheet()

        career = st.session_state.get("career", "Not selected")

        content = [
            Paragraph("Career Guidance Report", styles["Title"]),
            Paragraph(f"Recommended Career: {career}", styles["Normal"])
        ]

        doc.build(content)

        with open("career_report.pdf", "rb") as f:
            st.download_button("Download PDF", f, file_name="career_report.pdf")

# ------------------ LOGOUT ------------------
elif menu == "🚪 Logout":
    del st.session_state["user"]
    st.rerun()
