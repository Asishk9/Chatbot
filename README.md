# Chatbot

A simple AI chatbot built with **LangChain**, **Groq LLM**, and **Streamlit**.  
It provides a clean ChatGPT-like interface where users can chat naturally with a Groq-powered assistant.

🚀 **Try the chatbot here:**  
👉 https://chatbot-asishk9.streamlit.app


## ⚙️ Setup Instructions

### 1️⃣ Clone this repository
git clone https://github.com/asishk9/chatbot.git
cd chatbot

### 2️⃣ Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate

### 3️⃣ Install dependencies
pip install -r requirements.txt

### 4️⃣ Add your Groq API key
Create a file named .env in the project root
GROQ_API_KEY=your_groq_api_key

### 5️⃣ Run the chatbot
streamlit run app.py
