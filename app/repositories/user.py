from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException, status
from ..database.models import User

class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, tid:int):
        try:
            user = User(tid=tid)
            self.session.add(user)
            await self.session.commit()

            return user.id

        except Exception as e:
            return HTTPException(status_code=400, detail=str(e))

