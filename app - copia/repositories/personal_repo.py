from typing import List, Optional
from app.models.personal import Personal
from app.db.peewee_conn import database
from peewee import DoesNotExist

def create_personal(data: dict) -> Personal:
    return Personal.create(**data)

def get_personal(expediente: int) -> Optional[Personal]:
    try:
        return Personal.get(Personal.expediente == expediente)
    except DoesNotExist:
        return None

def list_personal(skip: int = 0, limit: int = 50) -> List[Personal]:
    return list(Personal.select().offset(skip).limit(limit))

def update_personal(expediente: int, data: dict) -> Optional[Personal]:
    row = (Personal
           .update(**data)
           .where(Personal.expediente == expediente)
           .execute())
    return get_personal(expediente) if row else None

def delete_personal(expediente: int) -> bool:
    return bool(Personal.delete().where(Personal.expediente == expediente).execute())


