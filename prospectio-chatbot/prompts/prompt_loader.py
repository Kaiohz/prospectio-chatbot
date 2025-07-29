import os


class PromptLoader:
    prompt_mapping = {
        "Prospectio": "prospectio/system",
    }

    def load_prompt(self, chat_profile: str) -> str:
        prompt_path = os.path.join(
            os.path.dirname(__file__),
            f"{self.prompt_mapping.get(chat_profile)}.md",
        )
        try:
            with open(prompt_path, "r", encoding="utf-8") as f:
                return f.read().strip()
        except FileNotFoundError:
            return "You are a helpful AI assistant."
