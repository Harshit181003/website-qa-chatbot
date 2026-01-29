import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from config.settings import GROQ_MODEL

load_dotenv()

def load_groq_llm():
    return ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name=GROQ_MODEL,
        temperature=0
    )