from fastapi import APIRouter, Depends

from src.domain.command import CommandHandler
from src.delivery.api.v1.health.health_response import HealthResponse
from src.use_cases.health_command import HealthCommand, HealthCommandHandler

health_router: APIRouter = APIRouter()


async def health_command_handler() -> CommandHandler:
    return HealthCommandHandler()


@health_router.get("/health", response_model=HealthResponse)
def health(handler: CommandHandler = Depends(health_command_handler)) -> HealthResponse:
    command = HealthCommand()
    response = handler.execute(command)
    ok = response.message()
    return HealthResponse(ok=ok)
