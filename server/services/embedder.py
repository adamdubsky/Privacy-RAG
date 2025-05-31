from sentence_transformers import SentenceTransformer

# Load once at module level
embed_model = SentenceTransformer("BAAI/bge-m3")

def embed_chunks(chunks: list[dict]) -> list[tuple[str, list[float], dict]]:
    """
    Returns a list of tuples:
    (chunk_id, embedding_vector, metadata_dict)
    """
    texts = [chunk["text"] for chunk in chunks]
    ids = [chunk["chunk_id"] for chunk in chunks]
    embeddings = embed_model.encode(texts, convert_to_numpy=True).tolist()

    results = []
    for chunk, emb in zip(chunks, embeddings):
        metadata = {
            "source_file": chunk["source_file"],
            "origin": chunk["origin"],
            "type": chunk["type"],
            "chunk_index": chunk["chunk_index"],
        }
        results.append((chunk["chunk_id"], emb, metadata))

    return results
