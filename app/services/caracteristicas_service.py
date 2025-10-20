# app/services/caracteristicas_service.py
from typing import Dict, Any, Optional
from playhouse.shortcuts import model_to_dict
from app.repositories.caracteristicas_repo import CaracteristicasRepository

class CaracteristicasService:
    def __init__(self):
        self.repo = CaracteristicasRepository()

    def create(self, payload: Dict[str, Any]) -> Dict:
        inst = self.repo.create(payload)
        return model_to_dict(inst, recurse=False)

    def get(self, nu_inventario: str) -> Optional[Dict]:
        inst = self.repo.get(nu_inventario)
        return model_to_dict(inst, recurse=False) if inst else None

    def list(self, **kwargs) -> Dict:
        objs, total = self.repo.list(
            q=kwargs.get("q"),
            limit=kwargs.get("limit", 50),
            offset=kwargs.get("offset", 0),
            order_by=kwargs.get("order_by", "nu_inventario"),
            desc=kwargs.get("desc", False),
        )
        items = [model_to_dict(inst, recurse=False) for inst in objs]
        return {
            "total": total,
            "limit": kwargs.get("limit", 50),
            "offset": kwargs.get("offset", 0),
            "count": len(items),
            "items": items,
        }

    def update(self, nu_inventario: str, payload: Dict[str, Any]) -> Optional[Dict]:
        updated = self.repo.update(nu_inventario, payload)
        return self.get(nu_inventario) if updated else None

    def delete(self, nu_inventario: str) -> bool:
        return self.repo.delete(nu_inventario)
