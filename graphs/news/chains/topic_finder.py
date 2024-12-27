from langchain_core.output_parsers import JsonOutputParser
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate

class TopicFinderChain():
    def __init__(self, model: str, temperature: float, prompt: str):
        self.prompt = PromptTemplate(template=prompt,input_variables=["question"])
        self.llm = ChatOllama(model=model, temperature=temperature)
        self.chain = self.prompt | self.llm | JsonOutputParser()