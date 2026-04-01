from langchain_core.vectorstores import VectorStore, VectorStoreRetriever
from langchain_community.vectorstores import FAISS

def get_retriever(vectorstore: VectorStore, k: int = 3) -> VectorStoreRetriever:
    """
    Create retriever from vector store
    """
    vector_store_retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": k
        }
    )

    return vector_store_retriever