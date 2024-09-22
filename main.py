import logging

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.common import config
from src.common.logger import setup_logging
from src.delivery.api.v1.health.health_router import health_router
from src.delivery.api.v1.hello.hello_router import hello_router
from time import sleep


logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator:
    setup_logging()
    logger.info("Starting FastAPI server...")

    yield

    # Graceful shutdown
    sleep(5)  # wait for the app to finish processing requests
    logger.info("FastAPI server finished!")


app = FastAPI(title=config.PROJECT_NAME, lifespan=lifespan)

app.include_router(prefix=config.API_V1_PREFIX, router=health_router)
app.include_router(prefix=config.API_V1_PREFIX, router=hello_router)
