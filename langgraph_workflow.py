from typing import TypedDict

from langgraph.graph import (
    StateGraph,
    END
)

from agents.memory_agent import (
    memory_agent
)

from agents.router_agent import (
    router_agent
)

from agents.pdf_agent import (
    pdf_agent
)

from agents.code_agent import (
    code_agent
)

from agents.dependency_agent import (
    dependency_agent
)

from agents.summarizer_agent import (
    summarizer_agent
)

from agents.reasoning_agent import (
    reasoning_agent
)


class AgentState(TypedDict):

    query: str

    route: str

    pdf_results: dict

    code_results: dict

    dependencies: dict

    summarized_context: list

    final_answer: str


workflow = StateGraph(
    AgentState
)

workflow.add_node(
    "memory",
    memory_agent
)

workflow.add_node(
    "router",
    router_agent
)

workflow.add_node(
    "pdf_agent",
    pdf_agent
)

workflow.add_node(
    "code_agent",
    code_agent
)

workflow.add_node(
    "dependency_agent",
    dependency_agent
)

workflow.add_node(
    "summarizer",
    summarizer_agent
)

workflow.add_node(
    "reasoning",
    reasoning_agent
)

workflow.set_entry_point(
    "memory"
)

workflow.add_edge(
    "memory",
    "router"
)


def route_logic(state):

    return state["route"]


workflow.add_conditional_edges(

    "router",

    route_logic,

    {

        "pdf": "pdf_agent",

        "code": "code_agent"
    }
)

workflow.add_edge(
    "pdf_agent",
    "dependency_agent"
)

workflow.add_edge(
    "code_agent",
    "dependency_agent"
)

workflow.add_edge(
    "dependency_agent",
    "summarizer"
)

workflow.add_edge(
    "summarizer",
    "reasoning"
)

workflow.add_edge(
    "reasoning",
    END
)

graph = workflow.compile()