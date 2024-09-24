import logging

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.common import config
from src.common.logger import setup_logging
from src.common.settings import Settings
from src.delivery.api.v1.health.health_router import health
from src.delivery.api.v1.hello.hello_router import hello
from time import sleep


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator:
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Starting FastAPI server...")

    yield

    # Graceful shutdown
    sleep(5)  # wait for the app to finish processing requests
    logger.info("FastAPI server finished!")


settings = Settings()

app = FastAPI(
    title=config.PROJECT_NAME,
    description="This is the documentation of the FastAPI template project.",
    lifespan=lifespan,
    openapi_url=settings.openapi_url,
)

app.include_router(prefix=config.API_V1_PREFIX, router=health)
app.include_router(prefix=config.API_V1_PREFIX, router=hello)
