from ..repositories.user import UserRepository

class UserService:
    def __init__(self, repository: UserRepository):
        self.UserRepository = repository

    async def create_user(self):
        pass