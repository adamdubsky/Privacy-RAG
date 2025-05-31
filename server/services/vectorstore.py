import chromadb
from chromadb.utils import embedding_functions

client = chromadb.PersistentClient(path="vectorstore")
collection = client.get_or_create_collection(name="secure_rag")

def add_to_vectorstore(items: list[tuple[str, list[float], dict]]) -> None:
    """
    Adds a batch of vectors to the global collection.

    This function takes a list of tuples, each containing an ID, its corresponding
    embedding vector, and a metadata dictionary. It then unpacks these values and
    calls the collection’s add method to store them.

    Parameters
    ----------
    items : list[tuple[str, list[float], dict]]
        A list where each tuple represents:
            - item_id (str): A unique identifier for the vector.
            - embedding (list[float]): The vector values to store.
            - metadata (dict): Additional information to associate with this vector.

    Returns
    -------
    None
        This function does not return anything; it directly adds the given items
        to the vector store.
    """
    ids = [item[0] for item in items]
    embeddings = [item[1] for item in items]
    metadatas = [item[2] for item in items]
    documents = [f"chunk-{i}" for i in range(len(items))]  # placeholder document names

    collection.add(
        ids=ids,
        embeddings=embeddings,
        metadatas=metadatas,
        documents=documents
    )
