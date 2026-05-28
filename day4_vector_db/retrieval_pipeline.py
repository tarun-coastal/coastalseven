from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_ollama.llms import OllamaLLM
from langchain.schema import Document

# -----------------------------
# Step 1: Create Better Documents
# -----------------------------

docs = [
    Document(
        page_content="""
        LangChain is a framework used for building AI-powered applications.
        It helps developers create chatbots, RAG systems, AI agents,
        and document-based question answering systems.
        """
    ),

    Document(
        page_content="""
        Embeddings are numerical vector representations of text.
        They help machines understand semantic meaning and are widely
        used in similarity search, recommendation systems, and retrieval pipelines.
        """
    ),

    Document(
        page_content="""
        FAISS is an efficient vector database library developed by Meta.
        It performs fast similarity searches on high-dimensional vectors
        and is commonly used in Retrieval-Augmented Generation applications.
        """
    ),

    Document(
        page_content="""
        Retrievers are components that fetch the most relevant documents
        from a vector database based on semantic similarity between
        user queries and stored embeddings.
        """
    ),
]

# -----------------------------
# Step 2: Load Embedding Model
# -----------------------------

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# -----------------------------
# Step 3: Create Vector Store
# -----------------------------

db = FAISS.from_documents(
    docs,
    embeddings
)

# -----------------------------
# Step 4: Create Retriever
# -----------------------------

retriever = db.as_retriever(
    search_kwargs={"k": 2}
)

# -----------------------------
# Step 5: Load Ollama LLM
# -----------------------------

llm = OllamaLLM(
    model="llama3.2"
)

# -----------------------------
# Step 6: Get User Query
# -----------------------------

query = input("\nAsk your question: ")

# -----------------------------
# Step 7: Retrieve Relevant Docs
# -----------------------------

retrieved_docs = retriever.invoke(query)

print("\nRetrieved Context:\n")

context = ""

for doc in retrieved_docs:
    print(doc.page_content)
    context += doc.page_content + "\n"

# -----------------------------
# Step 8: Create Prompt
# -----------------------------

prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{query}

Answer:
"""

# -----------------------------
# Step 9: Generate AI Response
# -----------------------------

response = llm.invoke(prompt)

# -----------------------------
# Step 10: Final Output
# -----------------------------

print("\nAI Response:\n")
print(response)