from app.main import run

def call_api(prompt, options, context):
    output = run(prompt)
    return {
        "output": output,
        # NOTE: Omitted as this is a sample when combined with LangGraph.
        # "tokenUsage": {
        #     "total": "",
        #     "prompt": "",
        #     "completion": "",
        # }
    }
