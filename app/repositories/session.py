from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from fastapi import HTTPException, status

from  ..database.models import Session, User


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

    async def create_by_tid(self, tid1: int,answer1:str,test_id: int):
        try:
            user_id = await self.session.scalar(select(User.id).where(User.tid == tid1))
            if not user_id:
                return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            return await  self.create(user_id, answer1, test_id)
        except Exception as e:
            HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

    async def set_id2_answer2_result_by_tid(self,session_id: int,tid2: int, answer2:str, result:str):
        try:
            id2 = await self.session.scalar(select(User.id).where(User.tid == tid2))
            if not id2:
                return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            return await  self.set_id2_answer2_result(session_id=session_id,id2=id2, answer2=answer2, result=result)
        except Exception as e:
            HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

