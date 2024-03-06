Custom Provider (with LangGraph App)
---

This is a custom provider sample using [promptfoo](https://www.promptfoo.dev/) and [LangGraph](https://python.langchain.com/docs/langgraph).

## Usage

1. Set environment variables

    Copy the .env.sample to create the .env file.

    ```shell
    cp .env.sample .env
    ```

    Then, set the following values in the created .env file.

    ```
    OPENAI_API_KEY=your_openai_api_key_here
    SERPAPI_API_KEY=your_serp_api_key_here
    TARGET_DIR=./src/langgraph
    ```

2. Run the evaluation

    You can run the evaluation with the following command.

    ```shell
    ./promptfoo.sh eval
    ```

    If you would like to issue a shared URL along with the evaluation, please execute the following command.

    ```shell
    ./promptfoo.sh eval --share
    ```

3. Confirmation of evaluation results

    The results are displayed in the terminal (or web browser if you are issuing a shared URL) as follows.

    ![langgraph_result](https://github.com/hyorimitsu/sample-promptfoo/blob/main/src/simple/langgraph_result.png)

    The results are displayed in a table format, covering the combinations of `prompts`, `providers`, and `tests` defined in `promptfooconfig.yaml`.
