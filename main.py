from pydantic import BaseModel
from fastapi import FastAPI

class Student(BaseModel):
    ID : int 
    Nombres : str
    Grado : str
    Salon : str

app = FastAPI()

@app.get('/')
async def root () :
    return {"message": "Hello"}

@app.post('/estudiantes')
async def create_student (student_data:Student):
    return student_data