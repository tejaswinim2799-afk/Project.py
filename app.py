import streamlit as st
st.title("This is my first app")
BRANCH=st.selectbox("Select your branch",["CSE","ECE","MECH","CIVIL"])
st.write("You have selected",BRANCH)
skills=st.multiselect("Select your skills",["Python","Java","C++","HTML","CSS"])
st.write("Your skills are",skills)
gender=st.radio("Select your gender",["Male","  Female ","Other"])
st.write("You have selected",gender)
experience=st.slider("Select your experience in years",0,10,1)
st.write("Your experience is",experience,"years")
marks=st.slider("Enter your marks",0,100)
st.write("Your marks are",marks)
file=st.file_uploader("Upload your resume",type=["pdf"])
date=st.date_input("Select your date of birth", key="dob1")
st.write("Your date of birth is",date)
spin = st.spinner("Loading...")
with spin:
    import time
    time.sleep(5)
    st.success("Done!")
date = st.date_input("Select your date of birth")
st.write("Your date of birth is",date)
color=st.color_picker("Pick your favorite color")
st.write("Your favorite color is",color)
dark_mode=st.toggle("Dark mode")
if dark_mode:
    st.write("Dark mode is on")
else:
    st.write("Dark mode is off")