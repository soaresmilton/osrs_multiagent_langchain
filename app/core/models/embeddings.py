from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.core.config.settings import settings
from langchain_core.embeddings import Embeddings

def get_embeddings() -> Embeddings:
    return GoogleGenerativeAIEmbeddings(
        model=settings.EMBEDDING_MODEL,
        google_api_key=settings.GOOGLE_API_KEY
    )