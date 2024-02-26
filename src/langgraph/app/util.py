from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

def create_agent(llm: ChatOpenAI, tools: list, system_prompt: str):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )
    agent = create_openai_tools_agent(llm, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools)

def create_supervisor(llm: ChatOpenAI, agents: list[str]):
    system_prompt = (
        "You are the supervisor over the following agents: {agents}."
        " You are responsible for assigning tasks to each agent as requested by the user."
        " Each agent executes tasks according to their roles and responds with their results and status."
        " Please review the information and answer with the name of the agent to which the task should be assigned next."
        " Answer 'FINISH' if you are satisfied that you have fulfilled the user's request."
    )

    options = ["FINISH"] + agents
    function_def = {
        "name": "supervisor",
        "description": "Select the next agent.",
        "parameters": {
            "type": "object",
            "properties": {
                "next": {
                    "anyOf": [
                        {"enum": options},
                    ],
                }
            },
            "required": ["next"],
        },
    }

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
            (
                "system",
                "In light of the above conversation, please select one of the following options for which agent should be act or end next: {options}."
            ),
        ]
    ).partial(options=str(options), agents=", ".join(agents))

    return (
        prompt
        | llm.bind_functions(functions=[function_def], function_call="supervisor")
        | JsonOutputFunctionsParser()
    )
