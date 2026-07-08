import streamlit as st

#title and text
st.title('MY FIRST STREAMLIT APP')
st.header('Welcome !! We are thrilled to have you with us..')
st.subheader('Every Great journey starts with a small step')
st.write("Here is My Message-")
st.write('''Every day is a new opportunity to learn something valuable.
Stay focused on your goals and never stop improving.
Small efforts made consistently lead to great success.
Believe in yourself, even when things seem difficult.
Keep smiling, stay positive, and enjoy the journey.
''')

#content divider
st.divider()

st.markdown("**Bold Content** and *Italic Content*")
st.markdown("## This is a heading inside the markdown")

st.divider()

#message box
st.success('This is a success message')
st.error('This is an error message')
st.warning('This is an warning message')
st.info('This is an info message')