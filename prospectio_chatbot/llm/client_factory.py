from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mistralai import ChatMistralAI
from langchain_openai import ChatOpenAI
from llm.generic_client import LLMGenericClient
from config import OllamaSettings, OpenRouterSettings


class LLMClientFactory:
    def __init__(self, model: str, temperature: float):
        self.ollama_settings = OllamaSettings()
        self.open_router_settings = OpenRouterSettings()
        self.model = model
        self.temperature = temperature
        self.model_mapping = {
            "Ollama": ChatOllama,
            "Google": ChatGoogleGenerativeAI,
            "Mistral": ChatMistralAI,
            "OpenRouter": ChatOpenAI
        }

    def create_client(self) -> LLMGenericClient:
        category = self.model.split("/")[0]
        model = self.model.split("/", 1)[1]
        params = {"model": model, "temperature": self.temperature}
        if category == "Ollama":
            params["base_url"] = self.ollama_settings.OLLAMA_BASE_URL
        if category == "OpenRouter":
            params["api_key"] = self.open_router_settings.OPEN_ROUTER_API_KEY
            params["base_url"] = self.open_router_settings.OPEN_ROUTER_API_URL
        client = self.model_mapping.get(category)(**params) # type: ignore
        if not client:
            raise ValueError(f"Invalid model name: {self.model}")
        return client
