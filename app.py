import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils.validators import is_valid_url
from main import index_website, load_chatbot

st.set_page_config(page_title="Website Chatbot", layout="wide")

st.title("Website Question Answer Chatbot")

if "chatbot" not in st.session_state:
    st.session_state.chatbot = None

url = st.text_input("Enter Website URL")

if st.button("Index Website"):

    if not is_valid_url(url):
        st.error("Invalid or unreachable URL")
    else:
        with st.spinner("Indexing website..."):
            vector_db = index_website(url)
            st.session_state.chatbot = load_chatbot(vector_db)
            st.success("Website Indexed Successfully")

if st.session_state.chatbot:

    st.subheader("Ask Questions")

    user_question = st.text_input("Your Question")

    if st.button("Ask"):

        response = st.session_state.chatbot.ask(user_question)

        st.markdown("### Answer")
        st.write(response)