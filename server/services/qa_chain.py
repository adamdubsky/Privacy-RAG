#from langchain.vectorstores import Chroma
#from langchain.embeddings import HuggingFaceEmbeddings
import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from sentence_transformers import SentenceTransformer
from llama_cpp import Llama
from langchain_core.embeddings import Embeddings

load_dotenv()
MODEL_PATH = os.getenv("LLAMA_MODEL_PATH")
CONTEXT_LENGTH = os.getenv("CONTEXT_LENGTH", "1024")
THREADS = os.getenv("THREADS", "4")


#embedding_model = HuggingFaceEmbeddings(model_name="BAAI/bge-m3")


class EmbeddingWrapper(Embeddings):
    def __init__(self, model):
        self.model = model

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return self.model.encode(texts, convert_to_numpy=True).tolist()

    def embed_query(self, text: str) -> list[float]:
        return self.model.encode(text, convert_to_numpy=True).tolist()

embedding_model = EmbeddingWrapper(SentenceTransformer("intfloat/e5-small-v2", trust_remote_code=True)
    #, device="cuda"  # Uncomment if you have a GPU and want to use it
)

db = Chroma(
    persist_directory="vectorstore",
    embedding_function=embedding_model
)


#retriever = db.as_retriever(search_kwargs={"k": 5})
retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 5})


llm = Llama(
    model_path=MODEL_PATH,  # Path to your LLaMA model
    n_ctx=1024,
    n_threads=4
) #modify based on your system's capabilities

def answer_question(question: str) -> str:
    # Step 1: Retrieve relevant documents
    #docs = retriever.get_relevant_documents(question)
    #docs = retriever.get_relevant_documents(f"query: {question}")
    docs = retriever.invoke(f"query: {question}")

    context = "\n\n".join(doc.page_content for doc in docs)

    # Step 2: Build the prompt
    #prompt = f"Answer the question based only on the following context:\n\n{context}\n\nQuestion: {question}"
    prompt = f"""<s>[INST] <<SYS>>
    You are a helpful assistant.
    <</SYS>>

    Answer the following question using only the context provided:

    {context}

    Question: {question} [/INST]"""


    # Step 3: Generate response from LLaMA
    result = llm(prompt)
    return result['choices'][0]['text'].strip()
