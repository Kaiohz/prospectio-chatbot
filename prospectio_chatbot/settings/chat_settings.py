from typing import List
from chainlit.input_widget import Select, Slider, InputWidget


class ChatSettings:
    def get_chat_settings(self) -> List[InputWidget]:
        return [
            Select(
                id="Model",
                label="LLM Model",
                values=[
                    "Ollama/qwen3:4b",
                    "Google/gemini-2.0-flash",
                    "Ollama/qwen3:8b",
                    "Google/gemini-2.5-pro",
                ],
                initial_index=0,
            ),
            Slider(
                id="Temperature",
                label="Model Temperature",
                initial=0.0,
                min=0.0,
                max=1.0,
                step=0.1,
            ),
        ]
