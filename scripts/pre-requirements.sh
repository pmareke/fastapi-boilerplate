#!/bin/bash

function rye_is_not_installed() {
    if ! command -v rye &> /dev/null; then
        echo "rye is not installed. Please go to https://docs.astral.sh/rye/getting-started/installation/."
        return 1
    fi
    return 0
}

function docker_is_not_installed() {
    if ! command -v docker &> /dev/null; then
        echo "docker is not installed. Please go to https://docs.docker.com/get-docker/."
        return 1
    fi
    return 0
}

rye_is_not_installed
docker_is_not_installed
