from pydantic import BaseModel
from db import SessionDep

from .routers import estudiantes,preguntas,pruebas,resultados 
app = FastAPI()
current_id: int = 0

@app.get('/')
async def root () :
    return {"message": "Hello"}


