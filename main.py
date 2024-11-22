import chainlit as cl
from llm_client.llm_client import LLMProxyChatOpenAI

# Initialize the LLM client
llm = LLMProxyChatOpenAI(streaming=True)

@cl.on_message
async def main(message: cl.Message):
    # Call LLM with user's message
    response = await llm.agenerate([[{"role": "user", "content": message.content}]])
    
    # Send the LLM's response
    await cl.Message(
        content=response.generations[0][0].text,
    ).send()
