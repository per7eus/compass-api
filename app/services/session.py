from openai import AsyncOpenAI

from ..repositories.session import SessionRepository

from ..config import API_KEY_YANDEX, PROMPT_ID


class SessionService:
    def __init__(self, repository: SessionRepository):
        self.repository = repository
        self.client = AsyncOpenAI(
            api_key=API_KEY_YANDEX,
            base_url="https://ai.api.cloud.yandex.net/v1",
        )

    async def create(self,session: dict):
        return await self.repository.create(user1_id=int(session.get('id1')), answer1=str(session.get('answer1')))

    async def join_session(self, session_id: int, session_schem: dict):
        session = await self.repository.get_by_id(session_id)
        try:
            response = await self.client.responses.create(
            prompt={
                "id": PROMPT_ID,
            },
            input=f"""Вопрос: Тебе нравится пить кокаколу? 
            Ответ1: {session.answer1}
            Ответ2: {session_schem.get('answer2')}
                """,
            )
            await self.repository.set_id2_answer2_result(session_id=session_id,
                                                         id2=session_schem.get("id2"),
                                                         answer2=session_schem.get("answer2"),
                                                         result=response.output_text)
            return response.output_text

        except Exception as e:
            print(f"Ошибка: {e}")
            return None


