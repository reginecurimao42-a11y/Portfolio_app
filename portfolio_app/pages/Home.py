import streamlit as st

st.set_page_config(
    page_title="Portfolio",
    page_icon="🏠",
    layout="centered"
)

st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #667eea, #764ba2);
}

.block-container {
    max-width: 900px;
    margin: auto;
    padding-top: 2rem;
}

.card {
    background: rgba(255, 255, 255, 0.92);
    padding: 35px;
    border-radius: 20px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    text-align: center;
}

h1 {
    color: #1e293b;
    font-weight: 700;
}

p, div {
    color: #334155;
    text-align: center;
}

img {
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)


st.markdown('<div class="card">', unsafe_allow_html=True)

st.title("🏠 Welcome")
st.header("Hi, I'm Regine 👋")

st.write("Aspiring Developer and Designer")


col1, col2, col3 = st.columns([1,4,1])

with col2:
    st.image("portfolio_app/images/profile.jpg", use_container_width=True)

st.write("""
This is my portfolio website built using Streamlit.
It showcases my skills, projects, and contact information.
""")


st.markdown('</div>', unsafe_allow_html=True)
