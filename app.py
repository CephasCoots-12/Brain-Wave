import streamlit as st
from transformers import pipeline
from memory import save_memory
from vault import *
from scraping import news
from ui import *

st.set_page_config(page_title="BrainWave AI 🔥", page_icon="🧠")

chatbot = pipeline("text-generation", model="gpt2")

show_ui()

user_input = st.text_input("Ask BrainWave AI Anything 🔥")
if user_input:
    response = chatbot(user_input, max_length=100, do_sample=True)[0]["generated_text"]
    save_memory(user_input, response)
    st.write(response)

st.sidebar.subheader("🌐 Current Affairs")
st.sidebar.write(news)
