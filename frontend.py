# frontend.py
import streamlit as st
from backend import ask_gpt   # import your backend function

# =============================
# Streamlit Frontend
# =============================
st.set_page_config(page_title="GenAI Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 GenAI Chatbot")
st.write("Chat with your custom GPT model. Select a model and start chatting!")

# Dropdown for model selection
model_choice = st.selectbox(
    "Choose OpenAI Model:",
    ["gpt-5.6-terra", "gpt-4.1-mini", "gpt-4.1", "gpt-3.5-turbo"]
)

# Maintain chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input box
user_input = st.text_input("You:", placeholder="Type your message here...")

if st.button("Send") and user_input.strip() != "":
    # Get response from GPT with selected model
    bot_response = ask_gpt(model_choice, user_input)

    # Save to chat history
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", bot_response))

# Display chat history
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**🧑 {sender}:** {message}")
    else:
        st.markdown(f"**🤖 {sender}:** {message}")
