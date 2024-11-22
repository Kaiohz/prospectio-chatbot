from typing import List
import httpx
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from config import LLM_URL, LLM_KEY, MODEL

class LLMProxyChatOpenAI(ChatOpenAI):
    def __init__(self, streaming: str = False) -> None:
        super().__init__(
            http_client=httpx.Client(http2=True, verify=False),
            http_async_client=httpx.AsyncClient(http2=True, verify=False),
            openai_api_base=LLM_URL,
            model=MODEL,
            openai_api_key=LLM_KEY,
            streaming=streaming,
            callbacks=[],
        )