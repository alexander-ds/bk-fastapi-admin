from fastapi import APIRouter
from models import PreguntaCrear,Pregunta
from db import SessionDep

router = APIRouter()

@router.post('/preguntas',response_model=Pregunta)
async def create_student (Pregunta_data:PreguntaCrear):
    return Pregunta_data
