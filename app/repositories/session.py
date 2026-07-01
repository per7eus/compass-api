from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from  ..database.models import Sessions

class SessionRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, user1_id, response):
        try:
            session = Sessions(user1_id=user1_id, resource1=response)
            self.session.add(session)
            await self.session.commit()
            return "created"
        except Exception as e:
            return f"error: {e}"