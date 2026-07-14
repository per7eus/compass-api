from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from  ..database.models import Session

class SessionRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, user1_id, answer1,test_id):
        try:
            session = Session(user1_id=user1_id, answer1=answer1, test_id=test_id)
            self.session.add(session)
            await self.session.commit()
            return session.id
        except Exception as e:
            return f"error: {e}"


    async def get_by_id(self, session_id: int):
        try:
            result = await self.session.execute(
                select(Session)
                .options(selectinload(Session.test))
                .where(Session.id == session_id)
            )
            return result.scalar_one_or_none()

        except Exception as e:
            return f"error: {e}"

    async def set_id2_answer2_result(self,session_id: int,id2: int, answer2:str, result:str):
        session = await self.session.get(Session, session_id)
        session.user2_id = id2
        session.answer2 = answer2

        session.result = result
        await self.session.commit()

