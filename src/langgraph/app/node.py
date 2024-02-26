import operator
from typing import Annotated, Sequence, TypedDict
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_core.runnables import Runnable
from app.agent import llm, researcher_agent, writer_agent
from app.util import create_supervisor

RESEARCHER = "RESEARCHER"
WRITER = "WRITER"
SUPERVISOR = "SUPERVISOR"

agents = [RESEARCHER, WRITER]

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
    next: str

def researcher_node(state: AgentState) -> dict:
    result = researcher_agent().invoke(state)
    return {"messages": [HumanMessage(content=result["output"], name=RESEARCHER)]}

def writer_node(state: AgentState) -> dict:
    result = writer_agent().invoke(state)
    return {"messages": [HumanMessage(content=result["output"], name=WRITER)]}

def supervisor_node(state: AgentState) -> Runnable:
    return create_supervisor(llm, agents)
