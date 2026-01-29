from crawler.web_loader import extract_website_text
from utils.text_splitter import split_text
from embeddings.embedder import load_embedding_model
from vectordb.faiss_store import create_vector_db
from llm.groq_client import load_groq_llm
from rag.qa_chain import WebsiteQA


def index_website(url):

    text, title = extract_website_text(url)

    metadata = {
        "source": url,
        "title": title
    }

    documents = split_text(text, metadata)

    embeddings = load_embedding_model()

    vector_db = create_vector_db(documents, embeddings)

    return vector_db


def load_chatbot(vector_db):

    llm = load_groq_llm()

    chatbot = WebsiteQA(llm, vector_db)

    return chatbot