FROM alpine:3.19

ENV PROMPTFOO_VERSION=0.43.1

# Preparation
RUN apk add --no-cache \
    npm \
    py3-pip

# Install Python packages (The purpose of this repository is solely to experiment with `promptfoo`, so we are avoiding the use of tools like `pipx` and instead using `--break-system-packages`.)
RUN pip install --break-system-packages \
    langchain \
    langchain_openai \
    langgraph \
    google-search-results

# Install promptfoo
RUN npm install -g promptfoo@"${PROMPTFOO_VERSION}"

ENTRYPOINT [ "promptfoo" ]
CMD [ "eval" ]
