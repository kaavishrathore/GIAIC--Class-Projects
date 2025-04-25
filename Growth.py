# Growth Mindset Challenge: Streamlit Web App
# File: growth_mindset_app.py
import streamlit as st
import pandas as pd
import os

DATA_FILE = 'growth_entries.csv'

st.title("🌱 Growth Mindset Journal")
st.write("Reflect on your learning journey and track your growth mindset.")

# Input form for daily reflection
date = st.date_input("Date")
reflection = st.text_area("What did you learn today?", height=150)

if st.button("Save Entry"):
    entry = {'date': date.isoformat(), 'reflection': reflection}
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE)
        df = df.append(entry, ignore_index=True)
    else:
        df = pd.DataFrame([entry])
    df.to_csv(DATA_FILE, index=False)
    st.success("Saved your reflection!")

# Show past entries
if os.path.exists(DATA_FILE):
    st.subheader("Past Reflections")
    df = pd.read_csv(DATA_FILE)
    st.dataframe(df)