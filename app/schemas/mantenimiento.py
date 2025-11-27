# app/schemas/mantenimiento.py
from pydantic import BaseModel, Field
from datetime import date
from typing import Optional
from app.schemas.personal import PersonalResponse

class MantenimientoBase(BaseModel):
    nu_inventario: str = Field(..., description="FK de recursos_m.nu_inventario")
    fecha: date = Field(..., description="Fecha del mantenimiento (YYYY-MM-DD)")
    trabajo: str = Field(..., max_length=150, description="Descripción del trabajo realizado")
    fallas: str = Field(..., max_length=150, description="Fallas detectadas")
    estatus: str = Field(..., max_length=100, description="Estatus del mantenimiento")
    observaciones: Optional[str] = Field(None, max_length=200, description="Observaciones adicionales")
    responsable: int = Field(..., description="Expediente del personal responsable")

    class Config:
        json_schema_extra = {
            "example": {
                "nu_inventario": "INV-001",
                "fecha": "2025-11-01",
                "trabajo": "Revisión general",
                "fallas": "Sin fallas",
                "estatus": "Completado",
                "observaciones": "Equipo en buen estado",
                "responsable": 1001
            }
        }

class MantenimientoCreate(MantenimientoBase):
    pass

class MantenimientoUpdate(BaseModel):
    fecha: Optional[date] = None
    trabajo: Optional[str] = None
    fallas: Optional[str] = None
    estatus: Optional[str] = None
    observaciones: Optional[str] = None
    responsable: Optional[int] = None

class MantenimientoOut(MantenimientoBase):
    id: int = Field(..., description="ID del registro de mantenimiento")
    responsable: Optional[PersonalResponse]

    class Config:
        from_attributes = True
