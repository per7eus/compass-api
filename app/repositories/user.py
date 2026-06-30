from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from ..database.models import Users

class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, tid:int) -> str:
        try:
            user = Users(tid=tid)
            self.session.add(user)
            await self.session.commit()

            return "created"
        except Exception as e:
            return f"error {e}"

