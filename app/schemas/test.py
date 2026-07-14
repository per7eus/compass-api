from pydantic import BaseModel


class TestCreatSchema(BaseModel):
    name: str
    questions: dict[str,str]