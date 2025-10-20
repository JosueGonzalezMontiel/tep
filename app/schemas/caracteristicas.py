# app/schemas/caracteristicas.py
from pydantic import BaseModel, Field
from typing import Optional

class CaracteristicasBase(BaseModel):
    nu_inventario: str = Field(..., description="FK de recursos_m.nu_inventario")
    nombre: Optional[str] = Field(None, max_length=150, description="Nombre del equipo o hostname")
    ip: Optional[str] = Field(None, max_length=50, description="Dirección IP")
    procesador: Optional[str] = Field(None, max_length=100, description="Procesador")
    memoria: Optional[str] = Field(None, max_length=50, description="Memoria RAM")
    disco_duro: Optional[str] = Field(None, max_length=50, description="Almacenamiento")
    paqueterias: Optional[str] = Field(None, max_length=200, description="Paqueterías instaladas")
    inv_anterio: Optional[str] = Field(None, max_length=50, description="Número de inventario anterior")

    class Config:
        json_schema_extra = {
            "example": {
                "nu_inventario": "INV-001",
                "nombre": "Equipo de diseño",
                "ip": "192.168.1.100",
                "procesador": "Intel i7",
                "memoria": "16 GB",
                "disco_duro": "512 GB SSD",
                "paqueterias": "Office, Photoshop",
                "inv_anterio": "INV-000"
            }
        }

class CaracteristicasCreate(CaracteristicasBase):
    pass

class CaracteristicasUpdate(BaseModel):
    nombre: Optional[str] = None
    ip: Optional[str] = None
    procesador: Optional[str] = None
    memoria: Optional[str] = None
    disco_duro: Optional[str] = None
    paqueterias: Optional[str] = None
    inv_anterio: Optional[str] = None

class CaracteristicasOut(CaracteristicasBase):
    pass
