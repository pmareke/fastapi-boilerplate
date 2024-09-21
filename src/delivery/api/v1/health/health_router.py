from fastapi import APIRouter

health_router = APIRouter()


@health_router.get("/api/v1/health")
def health() -> dict:
    return {"status": "ok"}
