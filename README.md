# AI Website QA Chatbot

An AI-powered chatbot that accepts a website URL, extracts content, creates embeddings, and answers questions strictly based on the website content using Retrieval Augmented Generation (RAG).

---

## Features

- Website crawling and text extraction
- Semantic search using FAISS
- SentenceTransformer embeddings
- Groq LLM integration
- Streamlit chat interface
- Context-aware conversation memory
- No hallucinated answers

---

## Tech Stack

- Frontend: Streamlit
- Embeddings: SentenceTransformers
- Vector Database: FAISS
- LLM: Groq (llama-3.1-8b-instant)
- Web Scraping: BeautifulSoup
- Backend: Python

---

## Architecture Flow

URL Input  
→ Website Scraping  
→ Text Chunking  
→ Embeddings  
→ FAISS Vector Search  
→ Groq LLM  
→ Streamlit Chat UI  

---

## Setup Instructions (Local)

### Install uv
pip install uv

### Install dependencies
uv sync

### Add API key

Create `.env` file:

GROQ_API_KEY=your_api_key_here


### Run app
uv run streamlit run app.py

---

## Streamlit Deployment

Public app deployed using Streamlit Cloud.

Add GROQ_API_KEY in Streamlit Secrets Manager.

---

## Vector Database Choice

FAISS was selected because:

- Fast similarity search
- Lightweight
- No external server needed
- Production-proven

---

## Embedding Strategy

SentenceTransformer model `all-MiniLM-L6-v2` is used for:

- High semantic accuracy
- Fast embedding generation
- Local execution

---

## Limitations

- Single-page crawling
- Session-based vector storage
- No PDF support

---

## Future Improvements

- Multi-page crawling
- Persistent vector storage
- PDF upload support
- Multi-user authentication
