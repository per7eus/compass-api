from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from ..database.models import Test

class TestRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self,question, name):
        test = Test(name=name, questions=question)
        self.session.add(test)
        await self.session.commit()
        return test.id