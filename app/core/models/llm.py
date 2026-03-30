from langchain_google_genai import GoogleGenerativeAI
from app.core.config.settings import settings
from langchain_core.language_models import BaseChatModel

def get_llm() -> BaseChatModel:
    return GoogleGenerativeAI(
        model=settings.MODEL,
        temperature=0.7,
        google_api_key=settings.GOOGLE_API_KEY
    )