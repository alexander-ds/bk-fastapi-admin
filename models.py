from pydantic import BaseModel

class Student(BaseModel):
    ID : int 
    Nombres : str
    Grado : str
    Salon : str
