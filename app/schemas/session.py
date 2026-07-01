from pydantic import BaseModel


class CreateSessionSchema(BaseModel):
    id1: int
    answer1: str


class JoinSessionSchema(BaseModel):
    id2: int
    answer2: str