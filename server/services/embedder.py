from transformers import AutoTokenizer, AutoModel
import torch

# Load once at module level
model_name = "BAAI/bge-m3"
#tokenizer = AutoTokenizer.from_pretrained(model_name)
#model = AutoModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
model = AutoModel.from_pretrained(model_name, trust_remote_code=True, use_safetensors=True)

# Converts natural language text into dense vector representations that capture semantic meaning
def embed_chunks(chunks: list[dict]) -> list[tuple[str, list[float], dict]]:
    """
    Generate embeddings for a list of text chunks and package them with metadata.

    This function takes in a list of chunk dictionaries (each containing text and
    related attributes), uses the embedding model to compute embedding vectors for
    each chunk’s text, and returns a list of tuples containing the chunk ID,
    embedding vector, and a metadata dictionary.

    Parameters
    ----------
    chunks : list[dict]
        A list of dictionaries, where each dictionary must include:
            - "chunk_id" (str): Unique identifier for this chunk.
            - "text" (str): The text content to embed.
            - "source_file" (str): The filename or source of the chunk.
            - "origin" (str): Any origin information (e.g., document, URL).
            - "type" (str): A descriptor for the chunk type (e.g., paragraph).
            - "chunk_index" (int): Position index of this chunk in its source.

    Returns
    -------
    list[tuple[str, list[float], dict]]
        A list of tuples, one per input chunk. Each tuple contains:
            - chunk_id (str): The same ID from the input chunk.
            - embedding_vector (list[float]): The numerical embedding for `text`.
            - metadata_dict (dict): A dictionary with keys "source_file",
              "origin", "type", and "chunk_index" extracted from the chunk.
    """
    texts = [chunk["text"] for chunk in chunks]
    ids = [chunk["chunk_id"] for chunk in chunks]

    encoded = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        model_output = model(**encoded)

    # Mean pooling over token embeddings (ignoring padding)
    attention_mask = encoded['attention_mask']
    token_embeddings = model_output.last_hidden_state
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1)
    sum_mask = torch.clamp(input_mask_expanded.sum(1), min=1e-9)
    embeddings = (sum_embeddings / sum_mask).cpu().numpy().tolist()

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
