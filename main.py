import chainlit as cl
from graphs.generic_graph import GenericGraph
from graphs.graph_factory import GraphFactory
from graphs.graph_params import GraphParams
from settings.chat_settings import ChatSettings
from profiles.chat_profiles import ChatProfiles
from langchain_core.messages import AIMessageChunk

chatSettings = ChatSettings().get_chat_settings()
chatProfiles = ChatProfiles().get_chat_profiles()
graph_params = GraphParams()
graph_factory = GraphFactory(graph_params)

async def setup_chat(model: str, temperature: float):
    chat_profile: str= cl.user_session.get("chat_profile")
    graph_params.agent = chat_profile
    graph_params.model = model
    graph_params.temperature = temperature
    graph = graph_factory.create_graph()
    cl.user_session.set("graph", graph)

@cl.set_chat_profiles
async def chat_profile():
    return chatProfiles

@cl.on_chat_start
async def on_chat_start():
    await setup_chat(chatSettings[0].values[0], chatSettings[1].initial)
    await cl.ChatSettings(chatSettings).send()

@cl.on_message
async def main(msg: cl.Message):
    answer = cl.Message(content="")
    graph: GenericGraph = cl.user_session.get("graph")
    chat_history = cl.chat_context.to_openai()[-4:-1]
    response = graph.get_graph().astream({"question": msg.content, "history": chat_history}, stream_mode=["messages"])
    async for chunk in response:
        if chunk[0] == "messages" and chunk[1][1]["langgraph_node"] == "generate":
            values: AIMessageChunk = chunk[1][0]
            await answer.stream_token(values.content)
    await answer.send()

@cl.on_settings_update
async def setup_agent(settings):
    await setup_chat(settings["Model"], settings["Temperature"])
