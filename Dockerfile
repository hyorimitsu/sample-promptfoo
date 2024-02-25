FROM node:20.11.1-alpine3.19

ENV PROMPTFOO_VERSION=0.43.1

RUN npm install -g promptfoo@"${PROMPTFOO_VERSION}"

ENTRYPOINT [ "promptfoo" ]
CMD [ "eval" ]
