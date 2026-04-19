import streamlit as st

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #a8edea, #fed6e3);
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

st.title("💻 Projects")

projects = {
    "CabitanClass System": "Student management system with attendance & grades.",
    "Calculator App": "Streamlit-based calculator.",
    "Data Visualization": "Graph analysis using Python."
}

for name, desc in projects.items():
    with st.expander(name):
        st.write(desc)

st.markdown('</div>', unsafe_allow_html=True)