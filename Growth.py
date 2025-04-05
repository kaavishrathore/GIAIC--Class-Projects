import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Growth Mindset Challenge",
    page_icon="🌱",
)

# Title
st.title("🌱 Growth Mindset Challenge: Web App with Streamlit")

# Introduction Section
st.subheader("📚 I want to share an idea that can make a big difference in your personal and academic growth—a **growth mindset**.")

# What is a Growth Mindset?
st.header("💡 What is a Growth Mindset?")
st.write("""
A **growth mindset** is the belief that your abilities and intelligence can be developed through hard work, perseverance, and learning from your mistakes.
This concept was popularized by psychologist **Carol Dweck**, and it challenges the idea that our skills are fixed. Instead, it reminds us that every challenge is an opportunity to learn and improve.
""")

# Why Adopt a Growth Mindset
st.header("🚀 Why Adopt a Growth Mindset?")
st.markdown("""
- **Embrace Challenges**: View obstacles as opportunities to learn rather than as setbacks.  
- **Learn from Mistakes**: Understand that making mistakes is a natural part of learning.  
- **Persist Through Difficulties**: Stay determined, even when things get tough.  
- **Celebrate Effort**: Recognize and reward the effort you put into learning.  
- **Keep an Open Mind**: Stay curious and willing to adapt your approach.
""")

# How to Practice a Growth Mindset
st.header("🛠️ How Can You Practice a Growth Mindset?")
st.markdown("""
- **Set Learning Goals**: Focus on developing new skills and understanding concepts.  
- **Reflect on Your Learning**: Think about what you’ve learned from successes and challenges.  
- **Seek Feedback**: Use constructive criticism as a tool for growth.  
- **Stay Positive**: Believe in your ability to grow and support others too.
""")

# Interactive Section - Today's Challenge
st.header("🎯 What's Your Challenge Today?")
user_input = st.text_input("Describe a current challenge you're facing:")

if user_input:
    st.success(f"You're tackling: '{user_input}'. That’s a bold step toward growth—keep going!")

# Reflect on Learning
st.header("🧠 Reflect on Your Learning")
reflection = st.text_area("What lesson or insight have you gained recently?")

if reflection:
    st.success("Awesome! Reflection helps you connect the dots and grow deeper.")

# Celebrate Achievements
st.header("🏆 Celebrate Your Wins")
achievement = st.text_input("Share something you've accomplished recently:")

if achievement:
    st.balloons()
    st.success(f"🎉 Amazing! Every achievement counts: {achievement}")

# Final Message
st.markdown("---")
st.markdown("""
### 🌟 Remember:
Your journey in education isn’t about proving your intelligence—it’s about **developing it**.

By adopting a growth mindset, you empower yourself to:
- Overcome challenges  
- Innovate  
- Continuously improve

Every step you take, whether forward or backward, is part of the learning process.

**Embrace your potential and never stop striving to be better.**

Wishing you all the best on your journey to growth and success! 💪
""")

# Watermark / Signature
st.markdown(
    "<div style='text-align: right; font-size: 12px; color: gray; opacity: 0.6;'>"
    "— Made by <strong>Kaavish Rathore</strong> 🚀"
    "</div>",
    unsafe_allow_html=True
)
