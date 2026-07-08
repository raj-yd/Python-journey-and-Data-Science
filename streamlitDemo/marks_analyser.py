import streamlit as st
import numpy as np

st.set_page_config(page_title = 'Marks Analyzer', page_icon = '[]', layout='wide')

st.title('Student Marks Analyzer')
st.write('This is demonstration of Python, NumPy, and Streamlit')

st.sidebar.title('Settings')
n_students = st.sidebar.slider('Number os Students', 10, 100, 30)
passing_marks = st.sidebar.slider('Passing Marks', 30, 50, 40)

np.random.seed(st.sidebar.number_input('Randmom Seed', value = 42))

marks = np.random.randint(25, 100, n_students)

st.divider()

#generating columns in streamlit
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric('Average', f'{np.mean(marks):.1f}')
col2.metric('Highest', f'{np.max(marks)}')
col3.metric('Lowest', f'{np.min(marks)}')
col4.metric('Passed', f'{np.sum(marks >= passing_marks)}')
col5.metric('Failed', f'{np.sum(marks < passing_marks)}')

st.divider()

left, right = st.columns(2)

with left:
    st.subheader('Marks Distribution')
    st.bar_chart(marks)

with right:
    st.subheader('Analysis')
    st.write(f'**Total Students:** {n_students}')
    st.write(f'**Pass Percentage** ' f'{np.mean(marks>=passing_marks)*100:.1f}%')

st.divider()
st.subheader('Filter students')
min_m, max_m = st.select_slider(
    'Select marks range',
    options = list(range(0,101)),
    value = (passing_marks, 100)
)

#fileration in student marksheet
filtered = marks[(marks >= min_m) & (marks <= max_m)]
st.write(f'Students with marks in between:' f'{min_m} and {max_m}: **{len(filtered)}**')
st.write(filtered)