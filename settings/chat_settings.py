from typing import List
from chainlit.input_widget import Select, Switch, InputWidget, Slider

class ChatSettings:
     def get_chat_settings(self) -> List[InputWidget]:
        return [
            Select(
                id="Model",
                label="LLM Model",
                values=["llama3.2", "llama3.1","qwen2.5", "mistral"],
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