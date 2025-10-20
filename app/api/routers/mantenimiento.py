# app/api/routers/mantenimiento.py
from fastapi import APIRouter, HTTPException, Query, Depends, Security
from typing import Optional
from app.schemas.mantenimiento import MantenimientoCreate, MantenimientoUpdate, MantenimientoOut
from app.services.mantenimiento_service import MantenimientoService
from app.db.peewee_conn import db_session
from app.api.deps import get_api_key

router = APIRouter(prefix="/mantenimiento", tags=["mantenimiento"], dependencies=[Security(get_api_key)])

def get_service():
    return MantenimientoService()

@router.post("", response_model=MantenimientoOut, status_code=201)
def create_mantenimiento(payload: MantenimientoCreate, svc: MantenimientoService = Depends(get_service), _: None = Depends(db_session)):
    return svc.create(payload.model_dump())

@router.get("/{id}", response_model=MantenimientoOut)
def get_mantenimiento(id: int, svc: MantenimientoService = Depends(get_service), _: None = Depends(db_session)):
    data = svc.get(id)
    if not data:
        raise HTTPException(status_code=404, detail="No encontrado")
    return data

@router.get("", response_model=dict)
def list_mantenimientos(
    q: Optional[str] = Query(None, description="Buscar por trabajo/fallas/estatus"),
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
    order_by: str = Query("id"),
    desc: bool = Query(False),
    svc: MantenimientoService = Depends(get_service),
    _: None = Depends(db_session)
):
    return svc.list(q=q, limit=limit, offset=offset, order_by=order_by, desc=desc)

@router.patch("/{id}", response_model=MantenimientoOut)
def update_mantenimiento(id: int, payload: MantenimientoUpdate, svc: MantenimientoService = Depends(get_service), _: None = Depends(db_session)):
    data = svc.update(id, payload.model_dump(exclude_unset=True))
    if not data:
        raise HTTPException(status_code=404, detail="No encontrado o sin cambios")
    return data

@router.delete("/{id}", status_code=204)
def delete_mantenimiento(id: int, svc: MantenimientoService = Depends(get_service), _: None = Depends(db_session)):
    ok = svc.delete(id)
    if not ok:
        raise HTTPException(status_code=404, detail="No encontrado")
    return None
