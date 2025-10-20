# app/api/routers/caracteristicas.py
from fastapi import APIRouter, HTTPException, Query, Depends, Security
from typing import Optional
from app.schemas.caracteristicas import CaracteristicasCreate, CaracteristicasUpdate, CaracteristicasOut
from app.services.caracteristicas_service import CaracteristicasService
from app.db.peewee_conn import db_session
from app.api.deps import get_api_key

router = APIRouter(prefix="/caracteristicas", tags=["caracteristicas"], dependencies=[Security(get_api_key)])

def get_service():
    return CaracteristicasService()

@router.post("", response_model=CaracteristicasOut, status_code=201)
def create_caracteristicas(payload: CaracteristicasCreate, svc: CaracteristicasService = Depends(get_service), _: None = Depends(db_session)):
    return svc.create(payload.model_dump())

@router.get("/{nu_inventario}", response_model=CaracteristicasOut)
def get_caracteristicas(nu_inventario: str, svc: CaracteristicasService = Depends(get_service), _: None = Depends(db_session)):
    data = svc.get(nu_inventario)
    if not data:
        raise HTTPException(status_code=404, detail="No encontrado")
    return data

@router.get("", response_model=dict)
def list_caracteristicas(
    q: Optional[str] = Query(None, description="Buscar por nombre/ip/procesador/memoria"),
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
    order_by: str = Query("nu_inventario"),
    desc: bool = Query(False),
    svc: CaracteristicasService = Depends(get_service),
    _: None = Depends(db_session)
):
    return svc.list(q=q, limit=limit, offset=offset, order_by=order_by, desc=desc)

@router.patch("/{nu_inventario}", response_model=CaracteristicasOut)
def update_caracteristicas(nu_inventario: str, payload: CaracteristicasUpdate, svc: CaracteristicasService = Depends(get_service), _: None = Depends(db_session)):
    data = svc.update(nu_inventario, payload.model_dump(exclude_unset=True))
    if not data:
        raise HTTPException(status_code=404, detail="No encontrado o sin cambios")
    return data

@router.delete("/{nu_inventario}", status_code=204)
def delete_caracteristicas(nu_inventario: str, svc: CaracteristicasService = Depends(get_service), _: None = Depends(db_session)):
    ok = svc.delete(nu_inventario)
    if not ok:
        raise HTTPException(status_code=404, detail="No encontrado")
    return None
