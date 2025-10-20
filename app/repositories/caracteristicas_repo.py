# app/repositories/caracteristicas_repo.py
from typing import Optional, List
from peewee import DoesNotExist
from app.models.caracteristicas import Caracteristicas

class CaracteristicasRepository:
    def create(self, data: dict) -> Caracteristicas:
        valid_fields = set(Caracteristicas._meta.fields.keys())
        clean = {k: v for k, v in data.items() if k in valid_fields}
        return Caracteristicas.create(**clean)

    def get(self, nu_inventario: str) -> Optional[Caracteristicas]:
        try:
            return Caracteristicas.get(Caracteristicas.nu_inventario == nu_inventario)
        except DoesNotExist:
            return None

    def list(self, q: Optional[str] = None, limit: int = 50, offset: int = 0,
             order_by: str = "nu_inventario", desc: bool = False):
        query = Caracteristicas.select()
        if q:
            query = query.where(
                (Caracteristicas.nombre.contains(q)) |
                (Caracteristicas.ip.contains(q)) |
                (Caracteristicas.procesador.contains(q)) |
                (Caracteristicas.memoria.contains(q)) |
                (Caracteristicas.disco_duro.contains(q))
            )
        total = query.count()
        field = getattr(Caracteristicas, order_by, Caracteristicas.nu_inventario)
        query = query.order_by(field.desc() if desc else field.asc()).limit(limit).offset(offset)
        return list(query), total

    def update(self, nu_inventario: str, data: dict) -> Optional[str]:
        clean = {k: v for k, v in data.items() if v is not None}
        rows = Caracteristicas.update(**clean).where(Caracteristicas.nu_inventario == nu_inventario).execute()
        return rows if rows else None

    def delete(self, nu_inventario: str) -> bool:
        return bool(Caracteristicas.delete().where(Caracteristicas.nu_inventario == nu_inventario).execute())
