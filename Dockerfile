FROM python:3.12-alpine

RUN apk update --no-cache && apk upgrade --no-cache --available

WORKDIR /code

RUN pip install poetry

COPY pyproject.toml /code

RUN poetry install --without test

COPY main.py /code/main.py

COPY src /code/src

EXPOSE 8000

CMD ["OPENAPI_URL=", "poetry", "run", "fastapi", "run"]
