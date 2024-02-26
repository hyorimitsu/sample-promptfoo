from langgraph.graph import StateGraph, END
from app.node import AgentState, RESEARCHER, WRITER, SUPERVISOR, researcher_node, writer_node, supervisor_node

workflow = StateGraph(AgentState)

workflow.add_node(RESEARCHER, researcher_node)
workflow.add_node(WRITER, writer_node)
workflow.add_node(SUPERVISOR, supervisor_node)

workflow.add_edge(RESEARCHER, SUPERVISOR)
workflow.add_edge(WRITER, SUPERVISOR)
workflow.add_conditional_edges(
    SUPERVISOR,
    lambda x: x["next"],
    {
        RESEARCHER: RESEARCHER,
        WRITER: WRITER,
        "FINISH": END
    }
)

workflow.set_entry_point(SUPERVISOR)

graph = workflow.compile()
