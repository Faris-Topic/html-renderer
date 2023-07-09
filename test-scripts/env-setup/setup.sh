#!/usr/bin/env bash
source config.sh

docker network create ${NETWORK_NAME}
docker run --network ${NETWORK_NAME} -d --rm --publish ${MONGO_PORT_EXTERNAL}:${MONGO_PORT_INTERNAL} --name ${MONGO_NAME} mongo:${MONGO_VERSION}
