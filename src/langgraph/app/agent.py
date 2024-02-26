from langchain_core.runnables import Runnable
from langchain_openai import ChatOpenAI
from app.tool import researcher, writer
from app.util import create_agent

llm = ChatOpenAI(model="gpt-4-turbo-preview")

def researcher_agent() -> Runnable:
    prompt = (
        "You are a researcher who uses SERP API's search engine to find the most up-to-date and correct information."
    )
    return create_agent(llm, [researcher], prompt)

def writer_agent() -> Runnable:
    prompt = (
        "You are a operator of a corporate Twitter account."
    )
    return create_agent(llm, [writer], prompt)
