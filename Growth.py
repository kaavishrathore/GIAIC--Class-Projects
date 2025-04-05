# Importing
import streamlit as st

st.set_page_config(page_title= "growth mindset project", project_icon="★")
st.title("Growth Mindset Challengy: Web App with Streamlit")

st.header("🚀 Welcome to Your Growth Journey!")
st.write("Embrance challenges, learn from mistakes, and unlock your full potential. This Ai-powered app helps you build a growth mindset with reflection, challenges, and achievements!")

#quotes section
st.header("💡Today's Growth Mindset Quote")
st.write("Success is not final, failure is not fatal: it is the courage to continue that courts.- Winston Churchill")

st.header("What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")

#condition
if user_input:
    st.success(f" you're facing : {user_input}. Keep pushing forward towards your goal!")
else:
    st.warning("Tell us about your challenge to get started")

#reflexing:
st.header("Reflect on Your Learning")
reflection = st.text_area("Write your reflections here:")

if reflection:
    st.success(f"Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflection on past experience help you grow! Share your difficulties")

#achievements
               