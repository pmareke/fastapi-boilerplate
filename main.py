import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from time import sleep

from fastapi import FastAPI

from src.common.logger import setup_logging
from src.common.settings import Settings
from src.delivery.api.v1.health.health_router import health
from src.delivery.api.v1.hello.hello_router import hello


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
    title=settings.project_name,
    description="This is the documentation of the FastAPI template project.",
    lifespan=lifespan,
    openapi_url=settings.openapi_url,
)

app.include_router(prefix=settings.api_v1_prefix, router=health)
app.include_router(prefix=settings.api_v1_prefix, router=hello)
