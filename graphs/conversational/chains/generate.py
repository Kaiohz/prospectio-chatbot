from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOllama
from langchain.prompts import PromptTemplate

class GenerateChain():
    def __init__(self, model: str, temperature: float, prompt: str):
        self.prompt = PromptTemplate(template=prompt,input_variables=["history", "question"])
        self.llm = ChatOllama(model=model, temperature=temperature)
        self.chain = self.prompt | self.llm | StrOutputParser()