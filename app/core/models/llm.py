from langchain_google_genai import GoogleGenerativeAI
from langchain_core.language_models import BaseChatModel

from app.core.config.settings import settings

def get_llm() -> BaseChatModel:

    return GoogleGenerativeAI(
        model=settings.MODEL,
        temperature=0.7,
        google_api_key=settings.GOOGLE_API_KEY
    )