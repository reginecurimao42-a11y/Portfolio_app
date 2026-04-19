import streamlit as st

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Portfolio",
    page_icon="🏠",
    layout="centered"
)

# =========================
# GLOBAL DESIGN (BACKGROUND + STYLE)
# =========================
st.markdown("""
<style>

/* 🌈 LIGHT GRADIENT BACKGROUND (NOT BLACK) */
.stApp {
    background: linear-gradient(to right, #667eea, #764ba2);
}

/* CENTER CONTAINER */
.block-container {
    max-width: 900px;
    margin: auto;
    padding-top: 2rem;
}

/* WHITE CARD */
.card {
    background: rgba(255, 255, 255, 0.92);
    padding: 35px;
    border-radius: 20px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    text-align: center;
}

/* TITLE STYLE */
h1 {
    color: #1e293b;
    font-weight: 700;
}

/* TEXT STYLE */
p, div {
    color: #334155;
    text-align: center;
}

/* IMAGE STYLE */
img {
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# CARD START
# =========================
st.markdown('<div class="card">', unsafe_allow_html=True)

# CONTENT
st.title("🏠 Welcome")
st.header("Hi, I'm Regine 👋")

st.write("Aspiring Developer and Designer")

# =========================
# CENTERED LARGE IMAGE
# =========================
col1, col2, col3 = st.columns([1,4,1])

with col2:
    st.image("images/profile.jpg", use_container_width=True)

st.write("""
This is my portfolio website built using Streamlit.
It showcases my skills, projects, and contact information.
""")

# =========================
# END CARD
# =========================
st.markdown('</div>', unsafe_allow_html=True)