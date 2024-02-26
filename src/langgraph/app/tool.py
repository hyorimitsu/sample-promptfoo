from langchain.tools import tool
from langchain_community.utilities import SerpAPIWrapper
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

@tool("researcher")
def researcher(query: str) -> str:
    """Research by SERP API"""
    serp_api = SerpAPIWrapper()
    return serp_api.run(query)

@tool("writer")
def writer(content: str) -> str:
    """Write a tweet"""
    chat = ChatOpenAI()
    messages = [
        SystemMessage(
            content="You are a operator of a corporate Twitter account."
                    " You are responsible for writing tweets based on the content given."
                    " As a prerequisite, you must always write within 140 characters according to Twitter's specifications."
        ),
        HumanMessage(
            content=content
        ),
    ]
    response = chat(messages)
    return response.content
