from fastapi import APIRouter, HTTPException, Query, Depends, Security
from typing import List, Optional
from app.schemas.personal import PersonalRequest, PersonalResponse, PersonalUpdate
from app.db.peewee_conn import to_dict
from app.repositories.personal_repo import (
    create_personal, get_personal, list_personal,
    update_personal, delete_personal, search_personal
)
from app.api.deps import get_api_key

router = APIRouter(prefix="/personal", tags=["personal"], dependencies=[Security(get_api_key)])

@router.post("", response_model=PersonalResponse, status_code=201)
def create_personal_endpoint(payload: PersonalRequest):
    
    created = create_personal(payload.model_dump())
    return to_dict(created)

@router.get("/{expediente}", response_model=PersonalResponse)
def get_personal_endpoint(expediente: int):
    person = get_personal(expediente)
    if not person:
        raise HTTPException(status_code=404, detail="No encontrado")
    return to_dict(person)

@router.get("", response_model=List[PersonalResponse])
def list_personal_endpoint(skip: int = Query(0, ge=0), limit: int = Query(50, ge=1, le=200)):
    rows = list_personal(skip=skip, limit=limit)
    return [to_dict(r) for r in rows]

@router.put("/{expediente}", response_model=PersonalResponse)
def update_personal_endpoint(expediente: int, payload: PersonalUpdate):
    updated = update_personal(expediente, {k: v for k, v in payload.model_dump().items() if v is not None})
    if not updated:
        raise HTTPException(status_code=404, detail="No encontrado o sin cambios")
    return to_dict(updated)

@router.delete("/{expediente}", status_code=204)
def delete_personal_endpoint(expediente: int):
    ok = delete_personal(expediente)
    if not ok:
        raise HTTPException(status_code=404, detail="No encontrado")
    return


