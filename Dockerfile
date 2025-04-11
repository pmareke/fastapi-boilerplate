FROM python:3.12-alpine

RUN apk update --no-cache && apk upgrade --no-cache --available

WORKDIR /code

RUN pip install uv

COPY pyproject.toml /code

RUN uv sync

COPY main.py /code/main.py

COPY src /code/src

EXPOSE 8000

CMD ["OPENAPI_URL=", "uv", "run", "fastapi", "run"]
