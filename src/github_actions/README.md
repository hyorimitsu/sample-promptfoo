Integration (with GitHub Actions)
---

This is an integration sample using [promptfoo](https://www.promptfoo.dev/) and [GitHub Actions](https://docs.github.com/en/actions).

## Usage

The LLM Prompt Evaluation workflow, which is defined in the repository, is triggered by a Pull Request for changes to `promptfooconfig.yaml` or `prompt.json`.  
You can find the workflow definition [here](https://github.com/hyorimitsu/sample-promptfoo/blob/main/.github/workflows/prompt-evaluation.yaml).

The evaluation result is posted as a comment to the Pull Request as follows.  
You can see the original Pull Request for these screenshots [here](https://github.com/hyorimitsu/sample-promptfoo/pull/4).

| Success | Failure |
| --- | --- |
| ![github-actions-comment-success](https://github.com/hyorimitsu/sample-promptfoo/blob/main/src/github_actions/github-actions-comment-success.png) | ![github-actions-comment-failure](https://github.com/hyorimitsu/sample-promptfoo/blob/main/src/github_actions/github-actions-comment-failure.png) |

You can also click `View eval results` to see the details of the evaluation results as follows.  
Details of these evaluation results can be found in the same Pull Request [here](https://github.com/hyorimitsu/sample-promptfoo/pull/4).  
Please note that the data for these evaluation results will be deleted after two weeks.

| Success | Failure |
| --- | --- |
| ![github-actions-result-success](https://github.com/hyorimitsu/sample-promptfoo/blob/main/src/github_actions/github-actions-result-success.png) | ![github-actions-result-failure](https://github.com/hyorimitsu/sample-promptfoo/blob/main/src/github_actions/github-actions-result-failure.png) |
