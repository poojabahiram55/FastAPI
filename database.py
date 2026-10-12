# from sqlmodel import SQLModel, create_engine
# import models
#
# sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"
#
# engine = create_engine(sqlite_url, connect_args={"check_same_thread": False}, echo=True)
#
#
# def create_db_and_tables():
#     SQLModel.metadata.create_all(engine)


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = 'postgresql://username:password@localhost:5432/DB'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()