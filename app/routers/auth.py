from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from ..repositories.user import UserRepository
from ..services.auth import AuthService
from ..database.session import get_session


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


auth_router = APIRouter(prefix="/auth", tags=["auth"])


def get_user_repository(sessions: AsyncSession = Depends(get_session)):
    return UserRepository(sessions)


async def get_auth_service(repository: UserRepository = Depends(get_user_repository)):
    return AuthService(repository)

