import json

from openai import AsyncOpenAI

from ..repositories.session import SessionRepository

from fastapi import HTTPException, status

from ..config import API_KEY_YANDEX, PROMPT_ID


class SessionService:
    def __init__(self, repository: SessionRepository):
        self.repository = repository
        self.client = AsyncOpenAI(
            api_key=API_KEY_YANDEX,
            base_url="https://ai.api.cloud.yandex.net/v1",
        )

    async def create(self,session: dict):
        return await self.repository.create(user1_id=int(session.get('id1')), answer1=session.get('answer1'),test_id=session.get('test_id'))

    async def join_session(self, session_id: int, session_schem: dict):
        session = await self.repository.get_by_id(session_id)
        if session.result:
            raise HTTPException(status_code=status.HTTP_410_GONE, detail="Session is already terminated and cannot be used anymore")
        elif session.user1_id == session_schem.get("id2"):
            return HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Cannot create session with yourself")
        try:
            questions = session.test.questions
            answers1 = session.answer1
            answers2 = session_schem.get('answer2')

            text = f"Тема: {session.test.name}\n"
            for i in range(1,len(questions)+1):
                text += f"Вопрос {i} {questions.get(str(i))}\nОтвет 1 пользователя: {answers1.get(str(i))}\nОтвет 2 пользователя: {answers2.get(str(i))}\n"

            response = await self.client.responses.create(
            prompt={
                "id": PROMPT_ID,
            },
            input=text,
            )

            await self.repository.set_id2_answer2_result(session_id=session_id,
                                                         id2=session_schem.get("id2"),
                                                         answer2=session_schem.get("answer2"),
                                                         result=response.output_text)
            return response.output_text

        except Exception as e:

            return HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=f"{e}")


    async def create_by_tid(self,schema):
        id = await self.repository.create_by_tid(schema.get("tid1"), answer1=schema.get('answer1'),test_id=schema.get('test_id'))
        return id


    async def join_session_by_tid(self,session_id, schema:dict[str,str]):
        session = await self.repository.get_by_id(session_id)
        if session.result:
            raise HTTPException(status_code=status.HTTP_410_GONE,
                                detail="Session is already terminated and cannot be used anymore")
        elif session.user1_id == schema.get("id2"):
            return HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Cannot create session with yourself")
        try:
            questions = session.test.questions
            answers1 = session.answer1
            answers2 = schema.get('answer2')

            text = f"Тема: {session.test.name}\n"
            for i in range(1, len(questions) + 1):
                text += f"Вопрос {i} {questions.get(str(i))}\nОтвет 1 пользователя: {answers1.get(str(i))}\nОтвет 2 пользователя: {answers2.get(str(i))}\n"

            response = await self.client.responses.create(
                prompt={
                    "id": PROMPT_ID,
                },
                input=text,
            )

            await self.repository.set_id2_answer2_result_by_tid(session_id=session_id,
                                                         tid2=int(schema.get('tid2')),
                                                         answer2=schema.get("answer2"),
                                                         result=response.output_text)
            return response.output_text

        except Exception as e:

            return HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=f"{e}")
