from typing import List
from chainlit.input_widget import Select, Slider, InputWidget


class ChatSettings:
    def get_chat_settings(self) -> List[InputWidget]:
        return [
            Select(
                id="Model",
                label="LLM Model",
                values=[
                    "Ollama/qwen2.5:14b",
                    "Ollama/qwen2.5:7b",
                    "Ollama/qwen3:14b",
                    "Google/gemini-2.5-pro",
                    "Google/gemini-2.0-flash",
                    "Mistral/pixtral-large-2411",
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
