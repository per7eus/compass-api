from pydantic import BaseModel



class CreateUserSchema(BaseModel):
    tid: int