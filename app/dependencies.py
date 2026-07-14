from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from .database.session import get_session
from .services.user import UserService
from .repositories.user import UserRepository
from .services.auth import SECRET_KEY, ALGORITHM

from .services.session import SessionService
from .repositories.session import SessionRepository

from .repositories.test import TestRepository
from .services.test import TestService


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme),session: AsyncSession = Depends(get_session)):
    print(f"DEBUG: Получен токен: {token}")
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY,algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError as e:
        print(f"DEBUG: Ошибка JWT: {e}")
        raise credentials_exception

    repository = UserRepository(session)
    user = await repository.find_user_by_id(int(user_id))
    if user is None:
        raise credentials_exception
    return user


def get_user_repository(sessions: AsyncSession = Depends(get_session)):
    return UserRepository(sessions)


def get_user_service(repository: UserRepository = Depends(get_user_repository)):
    return UserService(repository)


def get_session_repository(sessions: AsyncSession = Depends(get_session)):
    return SessionRepository(sessions)


def get_session_service(repository: SessionRepository = Depends(get_session_repository)):
    return SessionService(repository)


def get_test_repository(sessions: AsyncSession = Depends(get_session)):
    return TestRepository(sessions)

def get_test_service(repository: TestRepository = Depends(get_test_repository)):
    return TestService(repository)