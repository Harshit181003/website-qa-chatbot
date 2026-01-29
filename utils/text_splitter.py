from config.settings import CHUNK_SIZE, CHUNK_OVERLAP


def split_text(text, metadata):
    chunks = []

    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + CHUNK_SIZE
        chunk_text = text[start:end]

        chunk = {
            "page_content": chunk_text,
            "metadata": metadata
        }

        chunks.append(chunk)

        start = end - CHUNK_OVERLAP

    return chunks