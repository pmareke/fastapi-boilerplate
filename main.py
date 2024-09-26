from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from time import sleep

from fastapi import FastAPI

from src.common.logger import logger
from src.common.settings import settings
from src.delivery.api.v1.health.health_router import health
from src.delivery.api.v1.hello.hello_router import hello


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator:
    logger.info("Starting FastAPI server...")

    yield

    # Graceful shutdown
    sleep(5)  # wait for the app to finish processing requests
    logger.info("FastAPI server finished!")


app = FastAPI(
    title=settings.project_name,
    description=settings.description,
    lifespan=lifespan,
    openapi_url=settings.openapi_url,
)

app.include_router(prefix=settings.api_v1_prefix, router=health)
app.include_router(prefix=settings.api_v1_prefix, router=hello)
