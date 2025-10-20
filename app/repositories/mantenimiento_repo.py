# app/repositories/mantenimiento_repo.py
from typing import Optional, List
from peewee import DoesNotExist
from app.models.mantenimiento import Mantenimiento

class MantenimientoRepository:
    def create(self, data: dict) -> Mantenimiento:
        # acepta sólo campos válidos
        valid_fields = set(Mantenimiento._meta.fields.keys())
        clean = {k: v for k, v in data.items() if k in valid_fields}
        return Mantenimiento.create(**clean)

    def get(self, id: int) -> Optional[Mantenimiento]:
        try:
            return Mantenimiento.get(Mantenimiento.id == id)
        except DoesNotExist:
            return None

    def list(self, q: Optional[str] = None, limit: int = 50, offset: int = 0,
             order_by: str = "id", desc: bool = False):
        query = Mantenimiento.select()
        if q:
            query = query.where(
                (Mantenimiento.trabajo.contains(q)) |
                (Mantenimiento.fallas.contains(q)) |
                (Mantenimiento.estatus.contains(q))
            )
        total = query.count()
        field = getattr(Mantenimiento, order_by, Mantenimiento.id)
        query = query.order_by(field.desc() if desc else field.asc()).limit(limit).offset(offset)
        return list(query), total

    def update(self, id: int, data: dict) -> Optional[str]:
        clean = {k: v for k, v in data.items() if v is not None}
        rows = Mantenimiento.update(**clean).where(Mantenimiento.id == id).execute()
        return rows if rows else None

    def delete(self, id: int) -> bool:
        return bool(Mantenimiento.delete().where(Mantenimiento.id == id).execute())
