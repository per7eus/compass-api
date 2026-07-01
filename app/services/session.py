from ..repositories.session import SessionRepository

class SessionService:
    def __init__(self, repository: SessionRepository):
        self.repository = repository

    async def create(self,session: dict):
        print(f" {session.get('id1')} {session.get('response')} ")
        return await self.repository.create(user1_id=int(session.get('id1')), response=str(session.get('response')))