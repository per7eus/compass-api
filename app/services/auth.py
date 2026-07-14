from datetime import datetime, timedelta, timezone

from jose import jwt

from app.repositories.user import UserRepository


SECRET_KEY = "secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10000000


class AuthService:
    def __init__(self, repository: UserRepository):
        self.repository = repository
