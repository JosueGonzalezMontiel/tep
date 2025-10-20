# app/services/mantenimiento_service.py
from typing import Dict, Any, Optional
from playhouse.shortcuts import model_to_dict
from app.repositories.mantenimiento_repo import MantenimientoRepository

class MantenimientoService:
    def __init__(self):
        self.repo = MantenimientoRepository()

    def create(self, payload: Dict[str, Any]) -> Dict:
        inst = self.repo.create(payload)
        data = model_to_dict(inst, recurse=False)
        # devolver sólo el id del responsable (no el objeto)
        data['responsable'] = inst.responsable_id
        return data

    def get(self, id: int) -> Optional[Dict]:
        inst = self.repo.get(id)
        if not inst:
            return None
        data = model_to_dict(inst, recurse=False)
        data['responsable'] = inst.responsable_id
        return data

    def list(self, **kwargs) -> Dict:
        objs, total = self.repo.list(
            q=kwargs.get("q"),
            limit=kwargs.get("limit", 50),
            offset=kwargs.get("offset", 0),
            order_by=kwargs.get("order_by", "id"),
            desc=kwargs.get("desc", False),
        )
        items = []
        for inst in objs:
            row = model_to_dict(inst, recurse=False)
            row['responsable'] = inst.responsable_id
            items.append(row)
        return {
            "total": total,
            "limit": kwargs.get("limit", 50),
            "offset": kwargs.get("offset", 0),
            "count": len(items),
            "items": items,
        }

    def update(self, id: int, payload: Dict[str, Any]) -> Optional[Dict]:
        updated = self.repo.update(id, payload)
        return self.get(id) if updated else None

    def delete(self, id: int) -> bool:
        return self.repo.delete(id)
