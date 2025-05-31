import chromadb
from chromadb.utils import embedding_functions

client = chromadb.PersistentClient(path="vectorstore")
collection = client.get_or_create_collection(name="secure_rag")

def add_to_vectorstore(items: list[tuple[str, list[float], dict]]):
    ids = [item[0] for item in items]
    embeddings = [item[1] for item in items]
    metadatas = [item[2] for item in items]
    documents = [f"chunk-{i}" for i in range(len(items))]  # not used now

    collection.add(
        ids=ids,
        embeddings=embeddings,
        metadatas=metadatas,
        documents=documents
    )
