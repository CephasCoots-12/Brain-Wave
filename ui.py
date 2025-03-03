import streamlit as st

def show_ui():
    st.title("🧠 BrainWave AI")
    st.markdown("### The Most Intelligent AI Chatbot")
    st.markdown("---")
    st.sidebar.title("⚙️ BrainWave AI Menu")
    st.sidebar.markdown("🔍 **Current Affairs**")
    st.sidebar.markdown("🔒 **Vault Security**")
    st.sidebar.markdown("💪 **AI Power Chatbot**")
    st.sidebar.markdown("🌐 **Real-Time Web Scraping**")
    st.sidebar.markdown("🕰️ **Memory System**")

    st.markdown("<style>body { background-color: #111; color: #fff; font-family: Arial; }</style>", unsafe_allow_html=True)
    st.sidebar.markdown("<style> .sidebar { background-color: #222; color: #fff; } </style>", unsafe_allow_html=True)

    st.success("Welcome to BrainWave AI 🔥 - The Most Intelligent AI System")
