class GraphParams:
    def __init__(
        self,
        agent: str = '',
        model: str = '',
        temperature: float = 0.0,
        embeddings: str = '',
        tools_list: list = [],
    ):
        self.agent = agent
        self.model = model
        self.temperature = temperature
        self.embeddings = embeddings
        self.tools_list = tools_list
