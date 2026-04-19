import streamlit as st

st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #ff758c, #ff7eb3);
}
.block-container {
    max-width: 900px;
    margin: auto;
    padding-top: 2rem;
}
.card {
    background: rgba(255, 255, 255, 0.85);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    text-align: center;
}
h1 { color: #1e293b; }
p, div { color: #334155; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)

st.title("🛠️ Skills")

st.write("Python")
st.progress(75)

st.write("JavaScript")
st.progress(50)

st.write("PHP")
st.progress(70)

st.write("UI/UX Design")
st.progress(80)

st.markdown('</div>', unsafe_allow_html=True)