from fastapi import APIRouter

from .user import user_router
from .session import session_router
from .test import test_router

router = APIRouter()


router.include_router(user_router)
router.include_router(session_router)
router.include_router(test_router)