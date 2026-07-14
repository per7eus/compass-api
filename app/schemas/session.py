from pydantic import BaseModel


class CreateSessionSchema(BaseModel):
    id1: int
    answer1: dict[str, str]
    test_id: int


class JoinSessionSchema(BaseModel):
    id2: int
    answer2: dict[str, str]