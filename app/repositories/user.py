from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ..database.models import Users

class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session


