from langchain_community.vectorstores import FAISS


def create_vector_db(documents, embedding_model):

    texts = []
    metadatas = []

    for d in documents:
        texts.append(d["page_content"])
        metadatas.append(d["metadata"])

    db = FAISS.from_texts(
        texts=texts,
        embedding=embedding_model,
        metadatas=metadatas
    )

    return db