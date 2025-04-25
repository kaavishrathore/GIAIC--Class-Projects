import streamlit as st
import random

def main():
    st.set_page_config(page_title="Growth Mindset Challenge", layout="centered")

    st.title("🌱 Growth Mindset Challenge")

    st.header("💭 Growth Mindset Kya Hai?")
    st.markdown("""
    Growth mindset ka matlab hai ke hum mehnat aur seekhne se behtar ban saktay hain.  
    Har challenge ek naya moka hota hai seekhne ka.
    """)

    st.header("🚀 Growth Mindset Kyun Zaroori Hai?")
    st.markdown("""
    - **Challenge se daro nahi, seekho.**  
    - **Galtiyan sab karte hain, unse sabaq lo.**  
    - **Mushkil waqt mein himmat na haro.**  
    - **Koshish ki qadr karo, sirf result ki nahi.**  
    - **Naye ideas ke liye khula zehan rakho.**
    """)

    st.header("🧠 Apne Learning Habit Dekho")
    question1 = st.radio("Kya aap challenge ko seekhne ka moka samajhtay hain?", ["Haan", "Kabhi Kabhi", "Nahi"])
    question2 = st.slider("Aap kitni dafa feedback lete ho?", 1, 5, 3, help="1: Kabhi nahi, 5: Rozana")
    question3 = st.text_input("Aik cheez batayein jisme aap behtar banna chahtay hain:")

    st.header("💬 Motivation")
    quotes = [
        "“Acha kaam dil se karo.” – Steve Jobs",
        "“Galti ka matlab hai ke tum try kar rahe ho.”",
        "“Asli himmat to chalte rehne mein hai.” – Churchill"
    ]
    st.success(random.choice(quotes))

    st.header("🎯 Apna Goal Likho")
    goal = st.text_input("Apna aik goal likho (jo seekhna ya behtar banana ho):")
    if goal:
        st.info(f"📌 Tumhara Goal: {goal}")

    st.header("📢 Share Karna Chahtay Ho?")
    if st.button("✅ Apni Commitment Share Karo"):
        st.balloons()
        st.success("Shabash! Tumne growth mindset ki taraf pehla qadam utha liya hai.")

    st.markdown("---")
    st.caption("Yeh app Streamlit se banaya gaya hai | Good Luck! 🚀")

if __name__ == "__main__":
    main()
