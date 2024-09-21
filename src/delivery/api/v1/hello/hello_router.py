from fastapi import APIRouter, Depends
from src.use_cases.say_hello_command import (
    SayHelloCommand,
    SayHelloCommandHandler,
)
from src.domain.command import CommandHandler
from src.delivery.api.v1.hello.hello_response import HelloResponse

hello_router: APIRouter = APIRouter()


async def say_hello_command_handler() -> CommandHandler:
    return SayHelloCommandHandler()


@hello_router.get("/api/v1/hello/{name}", response_model=HelloResponse)
def hello(
    name: str, handler: CommandHandler = Depends(say_hello_command_handler)
) -> HelloResponse:
    command = SayHelloCommand(name)
    response = handler.execute(command)
    return HelloResponse(message=response.message())
