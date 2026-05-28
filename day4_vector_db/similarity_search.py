from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain.schema import Document

# Documents
docs = [
    Document(page_content="Python is used for AI."),
    Document(page_content="Machine learning uses embeddings."),
    Document(page_content="FAISS helps in similarity search."),
]

# Embeddings
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# Create vector DB
db = FAISS.from_documents(
    docs,
    embeddings
)

# Query
query = "What is FAISS?"

# Similarity search
results = db.similarity_search(query)

print("\nTop Similar Documents:\n")

for doc in results:
    print(doc.page_content)