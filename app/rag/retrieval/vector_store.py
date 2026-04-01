from langchain_community.vectorstores import FAISS
from langchain_core.vectorstores import VectorStore

from app.core.models.embeddings import get_embeddings

PERSIST_PATH = "C:/Users/Administrador/OneDrive/Documentos/Projects/007_osrs_multi_agent/app/data/vectorstore"
def load_vectorstore(path: str = PERSIST_PATH) -> VectorStore:
    """
    Carrega o vectorstore salvo localmente
    """

    embeddings = get_embeddings()
    local_vectorstore = FAISS.load_local(
        folder_path=path,
        embeddings=embeddings,
        allow_dangerous_deserialization=True
    )

    return local_vectorstore