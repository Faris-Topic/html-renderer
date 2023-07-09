#!/usr/bin/env bash
source config.sh

docker kill ${MONGO_NAME}
docker network rm ${NETWORK_NAME}