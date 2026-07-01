from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..database.session import get_session
from ..repositories.user import UserRepository
from ..services import user
from ..services.session import SessionService
from ..schemas.session import CreateSessionSchema
from  ..database.models import Users
from ..dependencies import get_current_user, get_session_repository, get_session_service

session_router = APIRouter(tags=["session"], prefix="/session")


@session_router.get("/")
async def main():
    return {"session": "session"}


@session_router.post("/create")
async def create(session: CreateSessionSchema, session_service: SessionService = Depends(get_session_service)):
    response = await session_service.create(session.model_dump())
    resource = session.model_dump()

    return {"id": f" {resource.get('id1')} {resource.get('response')} "}
