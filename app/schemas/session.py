from pydantic import BaseModel


class CreateSessionSchema(BaseModel):
    id1: int
    response: str