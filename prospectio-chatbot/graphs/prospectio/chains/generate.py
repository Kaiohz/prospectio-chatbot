from json import tool
from os import system
from langchain_core.output_parsers import StrOutputParser
from llm.client_factory import LLMClientFactory
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langgraph.prebuilt import ToolNode
import chainlit as cl


class GenerateChain:
    def __init__(self, model: str, temperature: float, prompt: str, tools_list: list):
        prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", prompt),
                ("placeholder", "{messages}"),
            ]
        )
        llm = LLMClientFactory(model=model, temperature=temperature).create_client()
        llm_with_tools = llm.bind_tools(tools_list)
        self.chain = prompt_template | llm_with_tools
