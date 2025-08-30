from pydantic.v1 import Field
from pydantic_settings import BaseSettings

class OllamaSettings(BaseSettings):
    """Settings for Ollama API."""
    OLLAMA_BASE_URL: str = Field(..., env="OLLAMA_BASE_URL")

class GeminiSettings(BaseSettings):
    """Settings for Gemini API."""
    GOOGLE_API_KEY: str = Field(..., env="GOOGLE_API_KEY")

class MistralSettings(BaseSettings):
    """Settings for Mistral API."""
    MISTRAL_API_KEY: str = Field(..., env="MISTRAL_API_KEY")

class PostgreSettings(BaseSettings):
    """Settings for PostgreSQL connection."""
    POSTGRE_CONNECTION_STRING: str = Field(..., env="POSTGRE_CONNECTION_STRING")
