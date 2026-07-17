from ..repositories.test import TestRepository

from fastapi import HTTPException


class TestService:
    def __init__(self, repository: TestRepository):
        self.repository = repository

    async def create(self, test):
        return await self.repository.create(test.get("questions"), test.get("name"))

    async def get_all(self):
        tests =  await self.repository.get_all()
        result = {}
        for test in tests:
            result.update({test.id: {"id": test.id,"name":test.name, "questions": test.questions}})
        return result

