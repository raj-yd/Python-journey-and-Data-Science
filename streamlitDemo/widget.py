import streamlit as st
import numpy as np
# st.markdown("""
# <style>
#             """)
st.title("Interactive Widget Demonstration")

#Text input
name=st.text_input("Your Name?")
if name:
    st.text(f'Hello, {name} Wecome \n Very Goodafternoon')  #st.text(f'Hello, {name} Wecome \n Very Goodafternoon')  isme \n kam nhi kar raha text me karega

st.divider()
age=st.number_input("Your Age?",min_value=1,max_value=100,value=25)
st.divider()

#slider
marks=st.slider('Your Marks?',min_value=0,max_value=100,value=75)
if marks>=80:
    st.success(f'Great! You scored {marks} , Grade - A')
elif marks>=60:
    st.info(f'You scored {marks} , Grade - B')
elif marks>=33:
    st.warning(f'You scored {marks} Work hard for better outcome, Grade - C')
else:
    st.error(f"Shit! You scored {marks}, FAil")

st.divider()

#dropdown menu
subject=st.selectbox("Select your favorite subject",["English","Python","JAVA","ML","AI"])
st.divider()

#checkbox
agree=st.checkbox("Do you agree with terms and conditions..")
if agree:
    st.success("Tankyou!! for agreeing")
    st.divider()

#radio button
gender=st.radio("Gender?",["Male","Female","Other"])
st.write(f"Selected : {gender}")

#multiselection
skills=st.multiselect("Your Skills",["Python","NumPy","Pandas","Data Science","SQL"])
if skills:
    st.write(f"You selected {len(skills)} Skills , Skills={', '.join(skills)}")

#button
if st.button("Clickme"):
    # st.toast("Small pop up in corner")
    st.balloons()
    st.success("You clicked this button")
