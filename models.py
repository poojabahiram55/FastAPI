# from sqlmodel import Field, SQLModel
#
#
# class Room(SQLModel, table=True):
#     __tablename__ = "rooms"
#
#     id: int | None = Field(default=None, primary_key=True)
#     name: str = Field()
#     price_per_night: int = Field()
#     bedrooms: float = Field(multiple_of=0.5)
#     bathrooms: float = Field(multiple_of=0.5)

from sqlalchemy import Boolean, Column, Integer, ForeignKey, Integer, String
from database import Base

class Questions(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String, index=True)

class Choices(Base):
    __tablename__ = 'choices'

    id = Column(Integer, primary_key=True, index=True)
    choices_text = Column(String, index=True)
    is_correct = Column(Boolean, default=False)
    question_id = Column(Integer, ForeignKey("questions.id"))