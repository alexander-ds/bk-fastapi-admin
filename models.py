from pydantic import BaseModel
from sqlmodel import SQLModel,Field

class EstudianteBase(SQLModel):
    Nombres : str = Field(default = None )
    Grado : str = Field(default = None )
    Salon : str = Field(default = None )

class EstudianteCrear(EstudianteBase):
    pass

class Estudiante(EstudianteBase,table=True):
    ID:int | None = Field(default=None,primary_key=True)

class PruebaBase(SQLModel): 
    Nombre : str = Field(default = None )
    Anio : str = Field(default = None )

class PruebaCrear(PruebaBase):
    pass

class Prueba(PruebaBase):
    ID:int | None = Field(default=None,primary_key=True)

class PreguntaBase(BaseModel):
    IDPrueba : int  = Field(default = None )
    Respuesta : str = Field(default = None )
    Orden : str = Field(default = None )


class PreguntaCrear(PreguntaBase):
    pass

class Pregunta(PreguntaBase):
    ID:int | None = Field(default=None,primary_key=True)

class ResultadoBase(BaseModel):
    IDPregunta : int = Field(default = None )
    IDEstudiante : int = Field(default = None )
    IDPrueba : str = Field(default = None )


class ResultadoCrear(ResultadoBase):
    pass

class Resultado(ResultadoBase):
    ID:int | None = Field(default=None,primary_key=True)
