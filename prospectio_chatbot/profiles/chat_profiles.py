from typing import List
import chainlit as cl

profiles = [
    cl.ChatProfile(
        name="Prospectio",
        markdown_description="To have a conversation with the selected model. You can change the model from the **settings**.",
        icon="public/avatars/prospectio-logo.png",
    )
]


class ChatProfiles:
    def get_chat_profiles(self) -> List[cl.ChatProfile]:
        return profiles
