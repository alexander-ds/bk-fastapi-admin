from fastapi import APIRouter
from models import EstudianteCrear,Estudiante
from db import SessionDep

router = APIRouter()

@router.post('/estudiantes',response_model=Estudiante)
async def create_student (Estudiante_data:EstudianteCrear,session:SessionDep):
    estudiante = Estudiante.model_validate(Estudiante_data.model_dump())
    session.add(estudiante)
    session.commit()
    session.refresh(estudiante)
    return estudiante

@router.get('/estudiantes')
async def create_student (Estudiante_data:EstudianteCrear):
    return dbResponse