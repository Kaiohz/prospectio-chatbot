from graphs.conversational.graph import ConversationalGraph
from graphs.generic_graph import GenericGraph
from graphs.graph_params import GraphParams


class GraphFactory:

    graph_mapping = {
        "Conversational AI": ConversationalGraph,
    }

    def __init__(self, graph_params: GraphParams):
        self.graph_params = graph_params

    def create_graph(self) -> GenericGraph:
        if self.graph_mapping.get(self.graph_params.agent):
            return self.graph_mapping[self.graph_params.agent](self.graph_params)
        else:
            raise ValueError('Invalid graph name')