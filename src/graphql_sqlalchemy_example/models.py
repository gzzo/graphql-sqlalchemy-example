from typing import List

from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))

    user = relationship("User", back_populates="books")


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    books: List[Book] = relationship("Book", back_populates="user")
