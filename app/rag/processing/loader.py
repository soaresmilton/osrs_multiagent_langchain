from langchain_core.documents import Document

import os
from pathlib import Path
from typing import List

def load_txt_files(path: str) -> List[Document]:
    """
    Load all .txt files from a director into Langchain Documents
    """
    base_path = Path(path)
    if not base_path.exists():
        raise ValueError("Path does not exist: {path}")

    documents: List[Document] = []

    for file_path in base_path.glob("*.txt"):
        content = file_path.read_text(encoding="utf-8")

        doc = Document(
            page_content=content,
            metadata={
                "source": str(file_path),
                "file_name": file_path.name
            }
        )

        documents.append(doc)
    
    return documents