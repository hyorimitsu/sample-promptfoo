Custom Provider (with LangGraph App)
---

This is a custom provider sample using [promptfoo](https://www.promptfoo.dev/) and [LangGraph](https://python.langchain.com/docs/langgraph).

## Usage

1. Set environment variables

    Copy `.env.sample` to create your .env file.

    ```shell
    cp .env.sample .env
    ```

    Next, set the following values in your .env file.

    ```
    OPENAI_API_KEY=your_openai_api_key_here
    SERPAPI_API_KEY=your_serpapi_api_key_here
    TARGET_DIR=./src/langgraph
    ```

2. Run the evaluation

    Run the evaluation with the following command.

    ```shell
    ./promptfoo.sh eval
    ```

    If you would like to issue a shared URL along with the evaluation, please execute the following command.

    ```shell
    ./promptfoo.sh eval --share
    ```

3. Viewing the Evaluation Results

    The results will be displayed in the terminal (or in a web browser if you issue a shared URL) as follows.

    ![langgraph_result](https://github.com/hyorimitsu/sample-promptfoo/blob/main/src/langgraph/langgraph_result.png)

    The results are displayed in a table format, covering the combinations of `prompts`, `providers`, and `tests` defined in `promptfooconfig.yaml`.
