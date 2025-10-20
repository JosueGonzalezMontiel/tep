from fastapi import APIRouter, HTTPException, Query, Depends, Security
from typing import List, Optional
from app.db.peewee_conn import db_session
from app.schemas.recursos_m import Recursos_mCreate, Recursos_mUpdate, Recursos_mOut
from app.db.peewee_conn import to_dict

from app.services.recursosm_service import Recursos_mService


from app.api.deps import get_api_key

router = APIRouter(prefix="/recursos_m", tags=["recursos_m"], dependencies=[Security(get_api_key)])

def get_service():
    return Recursos_mService()

@router.post("", response_model=Recursos_mOut, status_code=201)
def create_recursos_m(payload: Recursos_mCreate, svc: Recursos_mService = Depends(get_service), _: None = Depends(db_session)):
    try:
        return svc.create(payload.model_dump())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{nu_inventario}", response_model=Recursos_mOut)
def get_personal(recursos_m: str, svc: Recursos_mService = Depends(get_service), _: None = Depends(db_session)):
    data = svc.get(recursos_m)
    if not data:
        raise HTTPException(status_code=404, detail="No encontrado")
    return data

@router.get("", response_model=dict)
def list_recursos_m(
    q: Optional[str] = Query(None, description="Búsqueda por descripcion/marca/modelo,serie/expediente_resguardo"),
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
    order_by: str = Query("recursos_m"),
    desc: bool = Query(False),
    svc: Recursos_mService = Depends(get_service),
    _: None = Depends(db_session)
):
    return svc.list(q=q, limit=limit, offset=offset, order_by=order_by, desc=desc)

@router.patch("/{nu_inventario}", response_model=Recursos_mOut)
def update_recursos_m(
    recursos_m: str,
    payload: Recursos_mUpdate,
    svc: Recursos_mService = Depends(get_service),
    _: None = Depends(db_session)
):
    data = svc.update(recursos_m, payload.model_dump(exclude_unset=True))
    if not data:
        raise HTTPException(status_code=404, detail="No encontrado o sin cambios")
    return data

@router.delete("/{nu_inventario}", status_code=204)
def delete_recursos_m(
    recursos_m: str,
    svc: Recursos_mService = Depends(get_service),
    _: None = Depends(db_session)
):
    ok = svc.delete(recursos_m)
    if not ok:
        raise HTTPException(status_code=404, detail="No encontrado")
    return None

