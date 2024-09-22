from fastapi import APIRouter, Depends, HTTPException
from src.domain.exceptions import SayHelloCommandHandlerException
from src.use_cases.say_hello_command import (
    SayHelloCommand,
    SayHelloCommandHandler,
)
from src.domain.command import CommandHandler
from src.delivery.api.v1.hello.hello_response import HelloResponse
from src.infrastructure.hello.hello_client import DummyHelloClient

hello_router: APIRouter = APIRouter()


async def say_hello_command_handler() -> CommandHandler:
    hello_client = DummyHelloClient()
    return SayHelloCommandHandler(hello_client)


@hello_router.get("/api/v1/hello/{name}", response_model=HelloResponse)
def hello(
    name: str, handler: CommandHandler = Depends(say_hello_command_handler)
) -> HelloResponse:
    command = SayHelloCommand(name)
    try:
        response = handler.execute(command)
        message = response.message()
        return HelloResponse(message=message)
    except SayHelloCommandHandlerException as ex:
        raise HTTPException(status_code=500, detail="fatal error")
