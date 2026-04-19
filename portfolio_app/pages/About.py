import streamlit as st

st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #43e97b, #38f9d7);
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
    backdrop-filter: blur(6px);
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    text-align: center;
}

h1 { color: #1e293b; }
p, div { color: #334155; text-align: center; }

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)

st.title("👤 About Me")

st.write("I am a student and I enjoy solving problems and creating simple designs.")

st.subheader("🎓 Education")
st.write("BS Computer Science")

st.subheader("🎯 Goals")
st.write("Become a Developer")

st.markdown('</div>', unsafe_allow_html=True)
