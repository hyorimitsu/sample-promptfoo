from langchain_core.messages import HumanMessage
from app.graph import graph

def run(prompt):
    output = graph.invoke({"messages": [HumanMessage(content=prompt)]})
    return output["messages"][-1].content
