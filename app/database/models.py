from typing import List
from sqlalchemy import Integer, String, JSON, ForeignKey, Table, Column
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tid: Mapped[int] = mapped_column(Integer,unique= True)

    sessions_as_user1: Mapped[List["Session"]] = relationship(foreign_keys="Session.user1_id",
                                                             back_populates="user1")
    sessions_as_user2: Mapped[List["Session"]] = relationship(foreign_keys="Session.user2_id",
                                                             back_populates="user2")


class Session(Base):
    __tablename__ = 'session'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    answer1: Mapped[dict[str,str]] = mapped_column(JSON)
    answer2: Mapped[dict[str,str]|None] = mapped_column(JSON, nullable=True)

    result: Mapped[str|None] = mapped_column(String, nullable=True)

    test_id: Mapped[int] = mapped_column(ForeignKey("test.id"))

    user1_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user2_id: Mapped[int|None] = mapped_column(ForeignKey("user.id"), nullable=True)


    user1: Mapped["User"] = relationship(foreign_keys=[user1_id], back_populates="sessions_as_user1")
    user2: Mapped["User"] = relationship(foreign_keys=[user2_id], back_populates="sessions_as_user2")
    test: Mapped["Test"] = relationship(back_populates="sessions")


class Test(Base):
    __tablename__ = 'test'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)

    questions: Mapped[dict[str,str]] = mapped_column(JSON)

    sessions: Mapped[List["Session"]] = relationship( back_populates="test")