from fastapi import APIRouter, Depends, Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from .user import user_router
from .session import session_router
from .test import test_router

from ..config import SERVICE_API_KEY

api_key_header = APIKeyHeader(name="X-API-Key")  # auto_error=True по умолчанию

async def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != SERVICE_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key"
        )
    return api_key
router = APIRouter(dependencies=[Depends(verify_api_key)])


router.include_router(user_router)
router.include_router(session_router)
router.include_router(test_router)