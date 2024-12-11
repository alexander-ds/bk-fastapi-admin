from fastapi import APIRouter
from models import ResultadoCrear,Resultado
from db import SessionDep

router = APIRouter()

@router.post('/resultados',response_model=Resultado)
async def create_student (Resultado_data:ResultadoCrear):
    return Resultado_data