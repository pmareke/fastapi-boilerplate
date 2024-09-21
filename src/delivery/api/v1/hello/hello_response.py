from pydantic import BaseModel


class HelloResponse(BaseModel):
    message: str
