from typing import List
import chainlit as cl

profiles = [
    cl.ChatProfile(
        name="Conversational AI",
        markdown_description="To have a conversation with the selected model. You can change the model from the **settings**.",
        icon="public/avatars/my_assistant.png",
    ),
    cl.ChatProfile(
        name="Freelancer AI",
        markdown_description="To have a conversation with the selected model. You can change the model from the **settings**.",
        icon="public/avatars/my_assistant.png",
    ),
]

class ChatProfiles:
     def get_chat_profiles(self) -> List[cl.ChatProfile]:
        return profiles