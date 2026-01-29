from sentence_transformers import SentenceTransformer
from config.settings import EMBEDDING_MODEL


class LocalEmbeddingWrapper:

    def __init__(self):
        self.model = SentenceTransformer(EMBEDDING_MODEL)


    def __call__(self, text):
        return self.embed_query(text)

    
    def embed_documents(self, texts):
        return self.model.encode(texts).tolist()

    
    def embed_query(self, text):
        return self.model.encode(text).tolist()


def load_embedding_model():
    return LocalEmbeddingWrapper()