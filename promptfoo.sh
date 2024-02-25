#!/bin/sh

docker compose -f ./compose-tools.yaml run --rm promptfoo $@
