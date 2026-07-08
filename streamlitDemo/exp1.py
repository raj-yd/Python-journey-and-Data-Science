import streamlit as st

st.markdown("""
<h1 style="
    text-align: center;
    font-size: 60px;
    font-weight: bold;
    color: #1f2a44;
">
    CAR PRICE ANALYSIS
</h1>
""", unsafe_allow_html=True)

st.title("heyyyyyyyyyyyyyyy")
password=st.text_input("Password",type="password")

if st.button("Click me"):
    st.success("Done")

