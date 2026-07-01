from fastapi import APIRouter
from fastapi.params import Depends


from ..services.session import SessionService
from ..schemas.session import CreateSessionSchema, JoinSessionSchema

from ..dependencies import get_session_service


session_router = APIRouter(tags=["session"], prefix="/session")


@session_router.get("/")
async def main():
    return {"session": "session"}


@session_router.post("/create")
async def create(session: CreateSessionSchema, session_service: SessionService = Depends(get_session_service)):
    response = await session_service.create(session.model_dump())

    return {"id_session": response}


@session_router.post("/{session_id}/join")
async def join(session_id, session_join: JoinSessionSchema,session_service: SessionService = Depends(get_session_service)):
    result = await session_service.join_session(session_id, session_join.model_dump())
    return {"result": result}