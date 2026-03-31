import os
from typing import List
from langchain_core.documents import Document

from app.rag.processing.loader import load_txt_files
from app.rag.processing.chunking import split_documents
from app.rag.processing.vectorstore import create_vectorstore

DATA_PATH = "C:/Users/Administrador/OneDrive/Documentos/Projects/007_osrs_multi_agent/app/data/quests"
PERSIST_PATH = "C:/Users/Administrador/OneDrive/Documentos/Projects/007_osrs_multi_agent/app/data/vectorstore"

def run_ingestion(
    datah_path: str = DATA_PATH,
    persist_path: str = PERSIST_PATH
) -> None:
    """
    Executa o pipeline de ingestão: 
    load -> chunk -> embed -> persist
    """

    print("Loading documents...")
    documents: List[Documents] = load_txt_files(datah_path)
    print(f"Loaded {len(documents)} documents.")

    print("Splitting documents...")
    chunks: List[Documents] = split_documents(documents)
    print(f"Generated {len(chunks)} chunks.")

    print("Creating vector store...")
    vectorstore = create_vectorstore(chunks)

    print("Saving vector store...")
    vectorstore.save_local(persist_path)

    print("Ingestion complete.")


if __name__ == "__main__":
    run_ingestion()
