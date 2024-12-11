from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column,Mapped

class EstudianteBase(DeclarativeBase):
    Nombres : Mapped[str] = mapped_column(default = None)
    Grado : Mapped[str] = mapped_column(default = None)
    Salon : Mapped[str] = mapped_column(default = None)

class EstudianteCrear(EstudianteBase):
    pass

class Estudiante(EstudianteBase,table=True):
    __tablename__ = "Estudiante"
    ID:Mapped[Integer] | None = mapped_column(default=None,primary_key=True)

class PruebaBase(DeclarativeBase): 
    Nombre : Mapped[str] = mapped_column(default = None)
    Anio : Mapped[str] = mapped_column(default = None)

class PruebaCrear(PruebaBase):
    pass

class Prueba(PruebaBase,table=True):
    __tablename__ = "Prueba"
    ID:Mapped[Integer] | None = mapped_column(default=None,primary_key=True)

class PreguntaBase(DeclarativeBase):
    IDPrueba : Mapped[str]  = mapped_column(default = None)
    Respuesta : Mapped[str] = mapped_column(default = None)
    Orden : Mapped[str] = mapped_column(default = None)


class PreguntaCrear(PreguntaBase):
    pass

class Pregunta(PreguntaBase,table=True):
    __tablename__ = "Pregunta"
    ID:Mapped[Integer] | None = Mapped(default=None,primary_key=True)

class ResultadoBase(DeclarativeBase):
    IDPregunta : Mapped[Integer] = mapped_column(default = None)
    IDEstudiante : Mapped[Integer] = mapped_column(default = None)
    IDPrueba : Mapped[str] = mapped_column(default = None)


class ResultadoCrear(ResultadoBase):
    pass

class Resultado(ResultadoBase,table=True):
    __tablename__ = "Resultado"
    ID:Mapped[Integer] | None = mapped_column(default=None,primary_key=True)
