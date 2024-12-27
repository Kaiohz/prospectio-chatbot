from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from graphs.news.tools.news import NewsTools

class FetchNewsChain():
    def __init__(self, model: str, temperature: float, prompt: str):
        self.prompt = PromptTemplate(template=prompt,input_variables=["question","country"])
        self.tools = NewsTools().tools
        self.llm = ChatOllama(model=model, temperature=temperature)
        self.chain_with_tools = self.prompt | self.llm.bind_tools(self.tools)
        self.tool_node = NewsTools().tool_node