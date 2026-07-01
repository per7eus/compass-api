from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship


class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tid: Mapped[int] = mapped_column(Integer)


class Sessions(Base):
    __tablename__ = 'session'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user1_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user2_id: Mapped[int|None] = mapped_column(ForeignKey("user.id"),nullable=True)

    resource1: Mapped[str] = mapped_column(String)
    resource2: Mapped[str|None] = mapped_column(String, nullable=True)

    result: Mapped[str|None] = mapped_column(String, nullable=True)

    user1: Mapped["Users"] = relationship(foreign_keys=[user1_id])
    user2: Mapped["Users"] = relationship(foreign_keys=[user2_id])