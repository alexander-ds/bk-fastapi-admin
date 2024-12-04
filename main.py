from pydantic import BaseModel
from fastapi import FastAPI
from models import EstudianteCrear,Estudiante,PruebaCrear,Prueba,PreguntaCrear,Pregunta,ResultadoCrear,Resultado
from db import SessionDep

app = FastAPI()
current_id: int = 0

@app.get('/')
async def root () :
    return {"message": "Hello"}

@app.post('/estudiantes',response_model=Estudiante)
async def create_student (Estudiante_data:EstudianteCrear,session:SessionDep):
    estudiante = Estudiante.model_validate(Estudiante_data.model_dump())
    estudiante.id=current_id+1
    return estudiante

@app.get('/estudiantes')
async def create_student (Estudiante_data:EstudianteCrear):
    return dbResponse

@app.post('/pruebas',response_model=Prueba)
async def create_student (Prueba_data:PruebaCrear):
    return Prueba_data
    
@app.post('/preguntas',response_model=Pregunta)
async def create_student (Pregunta_data:PreguntaCrear):
    return Pregunta_data

@app.post('/resultados',response_model=Resultado)
async def create_student (Resultado_data:ResultadoCrear):
    return Resultado_data