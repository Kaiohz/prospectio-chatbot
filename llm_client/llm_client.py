from typing import Any, Coroutine, List
from ollama import AsyncClient, ChatResponse

class OllamaClient:
    def __init__(self, model: str, stream: bool):
        self.model = model
        self.stream = stream

    async def chat(self, messages: List[dict]) -> Coroutine[Any, Any, ChatResponse]:
        response = await AsyncClient().chat(model=self.model, messages=messages, stream=self.stream)
        return response
    
    async def setChatModel(self, model:str):
        self.model = model