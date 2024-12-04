from pydantic import BaseModel

class EstudianteBase(BaseModel):
    nombres : str
    grado : str
    salon : str

class EstudianteCrear(EstudianteBase):
    pass

class Estudiante(EstudianteBase):
    id:int | None = None    

class PruebaBase(BaseModel): 
    Nombre : str
    Anio : str

class PruebaCrear(PruebaBase):
    pass

class Prueba(PruebaBase):
    id:int | None = None   

class PreguntaBase(BaseModel):
    idPrueba : int 
    Respuesta : str
    Orden : str


class PreguntaCrear(PreguntaBase):
    pass

class Pregunta(PreguntaBase):
    id:int | None = None   

class ResultadoBase(BaseModel):
    idPregunta : int
    idEstudiante : int
    idPrueba : str


class ResultadoCrear(ResultadoBase):
    pass

class Resultado(ResultadoBase):
    id:int | None = None   
