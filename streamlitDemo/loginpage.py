import streamlit as st
import numpy as np
import csv

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

st.markdown("""
<h1 style="
    text-align: center;
    font-size: 30px;
    font-weight: 650;
    color: #1E3A8A;
">
    LOGIN
</h1>
""", unsafe_allow_html=True)

with open("loginData.csv","a+",newline="") as file1:
    file1.seek(0)
    data=csv.reader(file1)
    users= [row[0] for row in data]
    name=st.text_input("Name")
    password=st.text_input("Password",type="password")
    writer=csv.writer(file1)
    if name and password:
        if name in users:
            st.error("Username not available! Please take another username")
        else:
            writer.writerow([name,password])
            st.success("Login Successfully..")