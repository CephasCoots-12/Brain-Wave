import streamlit as st
from transformers import pipeline
from memory import save_memory
from scraping import news
from ui import *

st.set_page_config(page_title="BrainWave AI 🔥", page_icon="🧠")

chatbot = pipeline("text-generation", model="gpt2")

show_ui()

st.title("🧠 BrainWave AI - The Future of AI Chatbots")
st.write("Ask Anything with Real-Time Web Scraping + Memory System + Secure Vault 🔐")

user_input = st.text_input("Type your message here...", placeholder="What's on your mind?")
if user_input:
    with st.spinner("BrainWave AI is Thinking..."):
        response = chatbot(user_input, max_length=100, do_sample=True)[0]["generated_text"]
        save_memory(user_input, response)
        st.success("✅ BrainWave AI Answer")
        st.write(response)

st.sidebar.title("🌐 Current Affairs")
st.sidebar.write(news)

st.sidebar.markdown("---")
st.sidebar.caption("BrainWave AI 🔥 | Powered by GPT-2 + RLHF")
