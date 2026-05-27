from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

from langchain_ollama import ChatOllama

# 1. Load PDF
loader = PyPDFLoader("sample.pdf")
documents = loader.load()

# 2. Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = text_splitter.split_documents(documents)

# 3. Create embeddings
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# 4. Store embeddings in FAISS
vectorstore = FAISS.from_documents(
    docs,
    embeddings
)

# 5. Load Ollama model
llm = ChatOllama(
    model="llama3.2"
)

# 6. Chat loop
while True:

    query = input("\nAsk Question: ")

    if query.lower() == "exit":
        break

    # 7. Semantic search
    results = vectorstore.similarity_search(
        query,
        k=3
    )

    # 8. Create context
    context = "\n\n".join(
        [doc.page_content for doc in results]
    )

    # 9. Final prompt
    prompt = f"""
    Answer the question using the context below.

    Context:
    {context}

    Question:
    {query}
    """

    # 10. Generate answer
    response = llm.invoke(prompt)

    print("\nAnswer:\n")
    print(response.content)