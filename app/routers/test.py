from fastapi import APIRouter, Depends
from ..schemas.test import TestCreatSchema

from ..services.test import TestService

from ..dependencies import get_test_service

test_router = APIRouter(prefix="/test", tags=["test"])


@test_router.post("/create")
async def create_test(schema: TestCreatSchema, test_server: TestService = Depends(get_test_service)):
    id_test = await test_server.create(schema.model_dump())
    return {"id":id_test}

@test_router.get("/all")
async def get_all_tests(test_server: TestService = Depends(get_test_service)):
    return await test_server.get_all()