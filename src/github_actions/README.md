Integration (with GitHub Actions)
---

This is an integration sample using [promptfoo](https://www.promptfoo.dev/) and [GitHub Actions](https://docs.github.com/en/actions).

## Usage

The [LLM Prompt Evaluation workflow](https://github.com/hyorimitsu/sample-promptfoo/blob/main/.github/workflows/prompt-evaluation.yaml) is triggered by a Pull Request for changes to `promptfooconfig.yaml` or `prompt.json`.

The evaluation result is output as a comment to the Pull Request as follows. (This Pull Request is [here](https://github.com/hyorimitsu/sample-promptfoo/pull/4))

| Success | Failure |
| --- | --- |
| ![github-actions-comment-success](https://github.com/hyorimitsu/sample-promptfoo/blob/main/src/github_actions/github-actions-comment-success.png) | ![github-actions-comment-failure](https://github.com/hyorimitsu/sample-promptfoo/blob/main/src/github_actions/github-actions-comment-failure.png) |

You can also click `View eval results` to see the details of the evaluation results as follows.

| Success | Failure |
| --- | --- |
| ![github-actions-result-success](https://github.com/hyorimitsu/sample-promptfoo/blob/main/src/github_actions/github-actions-result-success.png) | ![github-actions-result-failure](https://github.com/hyorimitsu/sample-promptfoo/blob/main/src/github_actions/github-actions-result-failure.png) |
