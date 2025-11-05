import streamlit as st
from chatbot import get_bot_response

# PAGE SETUP
st.set_page_config(page_title="Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 Chatbot")
st.markdown("Chat naturally with an assistant powered by **LangChain** and **Groq LLM**.")

# CHAT MEMORY
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# DISPLAY CHAT HISTORY
for message in st.session_state.chat_history:
    role = message["role"]
    content = message["content"]
    with st.chat_message(role):
        st.markdown(content)

# INPUT BOX
prompt = st.chat_input("Type your message…")

if prompt:
    # show the user's message
    with st.chat_message("user"):
        st.markdown(prompt)

    # update history via your bot function
    st.session_state.chat_history = get_bot_response(
        prompt.strip(), st.session_state.chat_history
    )

    # render the assistant message 
    last = st.session_state.chat_history[-1] if st.session_state.chat_history else None
    if last and last.get("role") == "assistant":
        with st.chat_message("assistant"):
            st.markdown(last.get("content", ""))

# FOOTER
st.markdown("---")
st.caption("Built with ❤️ © Asish Kumar Gupta")
