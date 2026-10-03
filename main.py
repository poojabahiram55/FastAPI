from contextlib import asynccontextmanager
from fastapi import FastAPI, status, HTTPException, APIRouter
from database import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(
    lifespan=lifespan,
    title="Rent a room API",
    description="Book a stay in a house or room",
    version="1.0.0",
    contact={"name": "Rent Room", "email": "rooms@gmail.com"},
)

router = APIRouter()

data = [
    {
        "id": 1,
        "name": "Pooja",
    },
    {
        "id": 2,
        "name": "Khushi",
    },
]


@router.get("/", status_code=status.HTTP_200_OK)  # another way status_code = 200
def root():
    return {"message": "Welcome to Rent a Room."}


@router.get("/room")
def get_rooms(search: str = "", max_price=10_000):
    pass


@router.get("/room/{room_id}")
def get_room(room_id: int):
    for row in data:
        if row.get("id") == room_id:
            return row
    raise HTTPException(status.HTTP_404_NOT_FOUND, "Room not found.")


app.include_router(router)
