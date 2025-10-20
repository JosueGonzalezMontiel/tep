from typing import Optional, Dict, Any
from peewee import IntegrityError
from playhouse.shortcuts import model_to_dict
from app.repositories.recursosget_repo import recursos_mRepository

class Recursos_mService:
    def __init__(self, repo: Optional[recursos_mRepository] = None):
        self.repo = repo or recursos_mRepository()

    def create(self, payload: Dict[str, Any]) -> Dict:
        try:
            inst = self.repo.create(payload)
            return model_to_dict(inst)
        except IntegrityError as e:
            raise ValueError(f"Error de integridad: {e}")

    def get(self, nu_inventario: str) -> Optional[Dict]:
        inst = self.repo.get(nu_inventario)
        return model_to_dict(inst) if inst else None

    def list(self, **kwargs) -> Dict:
        objs, total = self.repo.list(
            q=kwargs.get("q"),
            limit=kwargs.get("limit", 50),
            offset=kwargs.get("offset", 0),
            order_by=kwargs.get("order_by", "nu_inventario"),
            desc=kwargs.get("desc", False),
        )
        items = [model_to_dict(x) for x in objs]
        return {
            "total": total,
            "limit": kwargs.get("limit", 50),
            "offset": kwargs.get("offset", 0),
            "count": len(items),
            "items": items,
        }

    def update(self, nu_inventario: str, payload: Dict[str, Any]) -> Optional[Dict]:
        rows = self.repo.update(nu_inventario, payload)
        if not rows:
            return None
        return self.get(nu_inventario)

    def delete(self, nu_inventario: str) -> bool:
        return self.repo.delete(nu_inventario)
