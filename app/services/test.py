from ..repositories.test import TestRepository

from fastapi import HTTPException


class TestService:
    def __init__(self, repository: TestRepository):
        self.repository = repository

    async def create(self, test):
        return await self.repository.create(test.get("questions"), test.get("name"))