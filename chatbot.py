import os
import streamlit as st
from dotenv import load_dotenv
from langchain.agents import create_agent

load_dotenv()

GROQ_API_KEY = (
    os.getenv("GROQ_API_KEY")
    or st.secrets.get("GROQ_API_KEY")
)

if not GROQ_API_KEY:
    raise RuntimeError(
        "GROQ_API_KEY is missing. Set it in .env file"
    )

# CONFIGURE LLM
model = "groq:llama-3.1-8b-instant"
agent = create_agent(
    model=model,
    tools=[],
    system_prompt=(
        "You are a helpful chat assistant. "
        "Be clear, concise, and polite. "
        "Understand the user's intent and respond directly. "
        "Stay professional and safe."
    ),
)

# CHATBOT RESPONSE FUNCTION
def get_bot_response(user_input, chat_history):
    """Takes user input and chat history, returns updated history."""
    messages = chat_history + [{"role": "user", "content": user_input}]
    result = agent.invoke({"messages": messages})

    # Extract assistant reply
    try:
        reply = result["messages"][-1].content
    except Exception as e:
        reply = f"[Error]: {str(e)}"

    # Update chat history
    chat_history.append({"role": "user", "content": user_input})
    chat_history.append({"role": "assistant", "content": reply})

    return chat_history