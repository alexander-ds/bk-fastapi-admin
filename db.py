from typing import Annotated
from fastapi import Depends,FastAPI
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os 

load_dotenv(".env")
 
DB_HOST = os.environ.get("HOST_BBDD")
DB_PORT = os.environ.get("PORT_BBDD")
DB_NAME = os.environ.get("BBDD")
DB_USER = os.environ.get("USER_BBDD")
DB_PASSWORD = os.environ.get("PASSWRD_BBDD")
 
DATABASE_URL = f'mssql+pymssql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}?timeout=5'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def crear_tablas(app:FastAPI):
    metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session


SessionDep=Annotated[SessionLocal,Depends(get_session)]       