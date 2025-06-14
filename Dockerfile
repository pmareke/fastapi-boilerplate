###################################
#            BUILDER              #
###################################

FROM python:3.12.8-alpine AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /code

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-group dev

###################################
#            RUNTIME              #
###################################

FROM python:3.12.8-alpine

ENV PATH="/code/.venv/bin:$PATH"

WORKDIR /code

COPY --from=builder /code/.venv /code/.venv

COPY main.py /code/main.py

COPY src /code/src

EXPOSE 8000

ENTRYPOINT ["fastapi", "run"]
