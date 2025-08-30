from langgraph.graph import StateGraph, START, END, MessagesState
from numpy import add
from graphs.prospectio.nodes import ProspectioNodes
from graphs.generic_graph import GenericGraph
from langgraph.graph.state import CompiledStateGraph
from graphs.graph_params import GraphParams


class ProspectioGraph(GenericGraph):

    def __init__(self, graph_params: GraphParams):
        self.ProspectioGraph = StateGraph(MessagesState)
        self.ProspectioNodes = ProspectioNodes(graph_params)
        self.construct_graph()

    def construct_graph(self):
        self.ProspectioGraph.add_node("call_model", self.ProspectioNodes.call_model)
        self.ProspectioGraph.add_node("tools", self.ProspectioNodes.call_tools)

        self.ProspectioGraph.add_edge(START, "call_model")
        self.ProspectioGraph.add_conditional_edges(
            "call_model", self.ProspectioNodes.should_continue
        )

        self.ProspectioGraph.add_edge("tools", "call_model")

    def get_graph(self) -> CompiledStateGraph:
        return self.ProspectioGraph.compile()
