from graphs.prospectio.graph import ProspectioGraph
from graphs.generic_graph import GenericGraph
from graphs.graph_params import GraphParams


class GraphFactory:
    def __init__(
        self,
        graph_params: GraphParams,
    ):
        self.graph_params = graph_params
        self.graph_mapping = {
            "Prospectio": ProspectioGraph,
        }

    def create_graph(self) -> GenericGraph:
        graph_class = self.graph_mapping.get(self.graph_params.agent)
        if graph_class:
            return graph_class(self.graph_params)
        else:
            raise ValueError(f"Invalid graph name: {self.graph_params.agent}")
