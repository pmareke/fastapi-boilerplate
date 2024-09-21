from fastapi import FastAPI
from src.delivery.api.v1.health.health_router import health_router

app = FastAPI()

app.include_router(health_router)
