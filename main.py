# from contextlib import asynccontextmanager
# from fastapi import FastAPI, status, HTTPException, APIRouter
# from database import create_db_and_tables
#
#
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     create_db_and_tables()
#     yield
#
#
# app = FastAPI(
#     lifespan=lifespan,
#     title="Rent a room API",
#     description="Book a stay in a house or room",
#     version="1.0.0",
#     contact={"name": "Rent Room", "email": "rooms@gmail.com"},
# )
#
# router = APIRouter()
#
# data = [
#     {
#         "id": 1,
#         "name": "Pooja",
#     },
#     {
#         "id": 2,
#         "name": "Khushi",
#     },
# ]
#
#
# @router.get("/", status_code=status.HTTP_200_OK)  # another way status_code = 200
# def root():
#     return {"message": "Welcome to Rent a Room."}
#
#
# @router.get("/room")
# def get_rooms(search: str = "", max_price=10_000):
#     pass
#
#
# @router.get("/room/{room_id}")
# def get_room(room_id: int):
#     for row in data:
#         if row.get("id") == room_id:
#             return row
#     raise HTTPException(status.HTTP_404_NOT_FOUND, "Room not found.")
#
#
# app.include_router(router)


from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.createall(bind=engine)

class ChoiceBase(BaseModel):
    choice_text: str
    is_correct: bool

class QuestionBase(BaseModel):
    question_text: str
    choices: List[ChoiceBase]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/questions/{question_id}")
async def read_questions(question_id: int, db: db_dependency):
    result = db.query(
        models.Questions
    ).filter(
        models.Questions.id==question_id
    ).first()

    if not result:
        raise HTTPException(status_code=404, detail='Question is not found')

    return result


@app.post("/questions/")
async def create_questions(question: QuestionBase, db: db_dependency):
    db_question = models.Questions(question_text=question.question_text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)

    for choice in question.choices:
        db_choice = models.Choices(
            choice_text=choice.choice_text,
            is_correct=choice.is_correct,
            question_id=db_question.id
        )
        db.add(db_choice)

    db.commit()




