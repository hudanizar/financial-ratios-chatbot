
import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(__file__))

from chatbot_core import handle_query, init_session

st.set_page_config(page_title="Financial Ratios Chatbot", layout="centered")
st.title("🤖 Financial Ratios Chatbot")

init_session(st.session_state)

st.markdown("""
Type a question or command below. For example:
- "What is ROE?"
- "Help me calculate Current Ratio"
- "Quiz me on Profitability Ratios"
- "Translate into Malay"
- "I’m new"
""")

user_input = st.text_input("💬 Your Question or Command:")

if user_input:
    response = handle_query(user_input, st.session_state)
    st.session_state.history.append((user_input, response))
    st.markdown("---")

if st.session_state.get("history"):
    st.subheader("🧾 Chat History")
    for user_q, bot_r in reversed(st.session_state.history):
        st.markdown(f"**You:** {user_q}")
        st.markdown(f"**Bot:** {bot_r}")
        st.markdown("---")
