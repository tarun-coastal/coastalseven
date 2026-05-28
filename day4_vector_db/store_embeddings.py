from langchain_community.vectorstores import FAISS
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain.schema import Document

# Sample documents
docs = [
    Document(page_content="Python is used for AI and ML."),
    Document(page_content="FAISS is a vector database by Meta."),
    Document(page_content="ChromaDB is used for storing embeddings."),
]

# Create embeddings model
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# ---------------- FAISS ----------------
faiss_db = FAISS.from_documents(
    docs,
    embeddings
)

print("FAISS vector store created!")

# ---------------- ChromaDB ----------------
chroma_db = Chroma.from_documents(
    docs,
    embeddings,
    persist_directory="./chroma_db"
)

print("ChromaDB vector store created!")