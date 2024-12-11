from fastapi import APIRouter
from models import PruebaCrear,Prueba
from db import SessionDep

router = APIRouter()

@router.post('/pruebas',response_model=Prueba)
async def create_student (Prueba_data:PruebaCrear):
    return Prueba_data
   