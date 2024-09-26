from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    openapi_url: str = "/openapi.json"
    api_v1_prefix: str = "/api/v1"
    project_name: str = "FastAPI Template"
    logger_name: str = "server"


settings = Settings()
