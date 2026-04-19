import streamlit as st

st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #ff9a9e, #fad0c4);
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

st.title("📩 Contact Me")

name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")

if st.button("Send"):
    if name and email and message:
        st.success("Message sent successfully! ✅")
    else:
        st.error("Please fill all fields.")

st.markdown("### 🌐 Social Links")
st.write("- GitHub: https://github.com/reginecurimao42-a11y")
st.write("- Facebook: https://facebook.com/regine.curimao")

st.markdown('</div>', unsafe_allow_html=True)