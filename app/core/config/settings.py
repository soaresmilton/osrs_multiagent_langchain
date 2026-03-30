from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROVIDER: str
    GOOGLE_API_KEY: str
    MODEL: str
    EMBEDDING_MODEL: str
    TAVILY_API_KEY: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()