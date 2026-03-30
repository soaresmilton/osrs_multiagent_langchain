from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    PROVIDER = os.getenv("PROVIDER")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    MODEL = os.getenv("MODEL")
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
