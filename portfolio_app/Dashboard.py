import streamlit as st

st.set_page_config(
    page_title="My Portfolio",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    font-family: 'Arial';
}

/* Center container card */
.block-container {
    max-width: 900px;
    margin: auto;
    padding: 2rem;
}

/* Glass card */
.main-card {
    background: rgba(255, 255, 255, 0.08);
    padding: 30px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    text-align: center;
}

/* Titles */
h1, h2, h3 {
    color: #ffffff;
    text-align: justify;
}

/* Text */
p, div {
    color: #e0e0e0;
    text-align: justify;
}

/* Buttons */
.stButton button {
    background-color: #ffffff;
    color: #0f2027;
    border-radius: 12px;
    padding: 8px 18px;
    font-weight: bold;
    border: none;
}

.stButton button:hover {
    background-color: #00c6ff;
    color: white;
}

</style>
""", unsafe_allow_html=True)

st.title("📊Dashboard")

st.write("""
Welcome to my portfolio.

Use the sidebar to navigate:
- Home
- About
- Skills
- Projects
- Contact
""")

st.success("Simple Portfolio Multipage App Using Streamlit")