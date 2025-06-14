FROM python:3.12.8-alpine

ENV PATH="/code/.venv/bin:$PATH"

# Hide the docs
ENV OPENAPI_URL= 

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /code

RUN uv python pin 3.12.8

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-group dev

COPY pyproject.toml /code

COPY uv.lock /code/uv.lock

COPY main.py /code/main.py

COPY src /code/src

RUN --mount=type=cache,target=/root/.cache/uv uv sync --locked --no-group dev

EXPOSE 8000

CMD []

ENTRYPOINT ["fastapi", "run"]
