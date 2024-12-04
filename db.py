from typing import Annotated
from fastapi import Depends,FastAPI
from sqlmodel import Session,create_engine,SQLModel

BBDD = "PruebaDesarrollador"
HOST_BBDD = "localhost"
PORT_BBDD = 1433
USER_BBDD = "deiby"
PASSWRD_BBDD = "0208Yesik@"
SERVER_BBDD = "ALX\SQLEXPRESS"

sqlServer_url=f"mssql+pyodbc://{USER_BBDD}:{PASSWRD_BBDD}@{SERVER_BBDD}/{BBDD}"
engine = create_engine(sqlServer_url)

def crear_tablas(app:FastAPI):
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session


SessionDep=Annotated[Session,Depends(get_session)]       