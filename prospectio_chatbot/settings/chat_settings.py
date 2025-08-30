from typing import List
from chainlit.input_widget import Select, Slider, InputWidget
from config import ChainlitSettings

class ChatSettings:
    models_list = ChainlitSettings().MODELS_LIST

    def get_chat_settings(self) -> List[InputWidget]:
        return [
            Select(
                id="Model",
                label="LLM Model",
                values=self.models_list,
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
