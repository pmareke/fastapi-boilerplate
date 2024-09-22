from fastapi import APIRouter, Depends, HTTPException
from http.client import BAD_REQUEST
from src.domain.exceptions import SayHelloCommandHandlerException
from src.use_cases.say_hello_command import (
    SayHelloCommand,
    SayHelloCommandHandler,
)
from src.domain.command import CommandHandler
from src.domain.hello_client import HelloClient
from src.delivery.api.v1.hello.hello_response import HelloResponse
from src.infrastructure.hello.hello_client import DummyHelloClient

hello: APIRouter = APIRouter()


async def hello_client() -> DummyHelloClient:
    return DummyHelloClient()


async def say_hello_command_handler(
    client: HelloClient = Depends(hello_client),
) -> CommandHandler:
    return SayHelloCommandHandler(client)


@hello.get("/hello/{name}", response_model=HelloResponse)
def get(
    name: str, handler: CommandHandler = Depends(say_hello_command_handler)
) -> HelloResponse:
    command = SayHelloCommand(name)
    try:
        response = handler.execute(command)
        message = response.message()
        return HelloResponse(message=message)
    except SayHelloCommandHandlerException as ex:
        raise HTTPException(status_code=BAD_REQUEST, detail=f"{ex}")
