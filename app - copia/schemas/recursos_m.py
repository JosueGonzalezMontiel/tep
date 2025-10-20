from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

# ---------------------------
# REQUEST / CREATE
# ---------------------------
class Recursos_mBase(BaseModel):
    nu_inventario: str = Field(..., description="Número de inventario (PK)")
    nu_NSAR: str = Field(..., max_length=100, description="Número de inventario de sistemas (NSAR)")
    descripcion: Optional[str] = Field(None, max_length=200, description="Descripción del recurso")
    marca: str = Field(..., max_length=150, description="Marca")
    modelo: str = Field(..., max_length=150, description="Modelo")
    serie: str = Field(..., max_length=150, description="Número de serie")
    observaciones: Optional[str] = Field(None, max_length=200, description="Observaciones")
    material: Optional[str] = Field(None, max_length=150, description="Material")
    color: Optional[str] = Field(None, max_length=100, description="Color")
    estado_fisico: Optional[str] = Field(None, max_length=100, description="Estado físico")
    ubicacion: Optional[str] = Field(None, max_length=150, description="Ubicación actual")
    expediente_resguardo: Optional[int] = Field(..., description="Expediente (PK) del personal que lo resguarda")
    fecha_asig: Optional[date] = Field(None, description="Fecha de asignación (YYYY-MM-DD)")
    ruta: Optional[str] = Field(None, description="Ruta local/remota asociada (evidencia, imagen, etc.)")

    class Config:
        json_schema_extra = {
            "example": {
                "nu_inventario": "INV-001",
                "nu_NSAR": "SYS-123",
                "descripcion": "Laptop para desarrollo",
                "marca": "HP",
                "modelo": "ProBook 450 G7",
                "serie": "5CG12345AB",
                "observaciones": "Batería al 90% de vida",
                "material": "Aluminio",
                "color": "Gris",
                "estado_fisico": "Bueno",
                "ubicacion": "Oficina 2do piso",
                "expediente_resguardo": 1001,
                "fecha_asig": "2025-10-10",
                "ruta": "C:/evidencias/INV-001.jpg"
            }
        }

class Recursos_mCreate(Recursos_mBase):
    expediente: int

class Recursos_mUpdate(Recursos_mBase):
    pass

class Recursos_mOut(Recursos_mBase):
    pass