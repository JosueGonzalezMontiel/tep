from pydantic import BaseModel, Field
from datetime import date
from typing import Optional, Literal

EstadoCivil = Literal["Soltero", "Casado", "Divorciado", "Viudo", "Unión libre"]

class PersonalRequest(BaseModel):
    expediente: int = Field(..., description="Número de expediente (PK)")
    paterno: str = Field(..., max_length=100, description="Apellido paterno")
    materno: Optional[str] = Field(None, max_length=100, description="Apellido materno")
    nombre: str = Field(..., max_length=150, description="Nombre o nombres del empleado")
    f_nacimiento: Optional[date] = Field(None, description="Fecha de nacimiento (YYYY-MM-DD)")
    estado_civil: Optional[EstadoCivil] = Field(None, description="Estado civil del empleado")
    adscripcion: Optional[str] = Field(None, max_length=150, description="Departamento o adscripción")
    cargo: Optional[str] = Field(None, max_length=150, description="Cargo o puesto")
    ruta: Optional[str] = Field(None, description="Ruta local de la imagen o expediente")

    class Config:
        json_schema_extra = {
            "example": {
                "expediente": 1001,
                "paterno": "González",
                "materno": "Montiel",
                "nombre": "Josué",
                "f_nacimiento": "1999-05-20",
                "estado_civil": "Soltero",
                "adscripcion": "Recursos Humanos",
                "cargo": "Analista Administrativo",
                "ruta": "C:/imagenes/expedientes/1001.jpg"
            }
        }

class PersonalUpdate(BaseModel):
    # Para PUT/PATCH (todos opcionales excepto la PK que viene en la ruta)
    paterno: Optional[str] = Field(None, max_length=100)
    materno: Optional[str] = Field(None, max_length=100)
    nombre: Optional[str] = Field(None, max_length=150)
    f_nacimiento: Optional[date] = None
    estado_civil: Optional[EstadoCivil] = None
    adscripcion: Optional[str] = Field(None, max_length=150)
    cargo: Optional[str] = Field(None, max_length=150)
    ruta: Optional[str] = None

class PersonalResponse(PersonalRequest):
    pass
