from typing import List, Optional
from peewee import DoesNotExist
from app.models.recursos_m import recursos_m

class recursos_mRepository:

    def create(self, data: dict) -> recursos_m:
        return recursos_m.create(**data)

    def get(self, nu_inventario: str) -> Optional[recursos_m]:
        try:
            return recursos_m.get(recursos_m.nu_inventario == nu_inventario)
        except DoesNotExist:
            return None

    def list(self, q: Optional[str] = None, limit: int = 50, offset: int = 0,
             order_by: str = "nu_inventario", desc: bool = False):
        query = recursos_m.select()
        if q:
            query = query.where(
                (recursos_m.descripcion.contains(q)) |
                (recursos_m.marca.contains(q)) |
                (recursos_m.modelo.contains(q)) |
                (recursos_m.serie.contains(q)) |
                (recursos_m.expediente_resguardo.contains(q))
            )
        total = query.count()
        field = getattr(recursos_m, order_by, recursos_m.nu_inventario)
        query = query.order_by(field.desc() if desc else field.asc()).limit(limit).offset(offset)
        return list(query), total

    def update(self, nu_inventario: str, data: dict) -> Optional[str]:
        q = recursos_m.update(**data).where(recursos_m.nu_inventario == nu_inventario)
        rows = q.execute()
        return rows if rows else None

    def delete(self, nu_inventario: str) -> bool:
        rows = recursos_m.delete().where(recursos_m.nu_inventario == nu_inventario).execute()
        return rows > 0
