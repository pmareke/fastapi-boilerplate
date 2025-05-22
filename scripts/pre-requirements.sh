#!/bin/bash

function uv_is_not_installed() {
    if ! command -v uv &> /dev/null; then
        echo "uv is not installed. Please go to https://docs.astral.sh/uv/getting-started/installation/."
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

uv_is_not_installed
docker_is_not_installed
