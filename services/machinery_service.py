# services/machinery_service.py

import json
from typing import List, Optional
from models.machinery import Machinery

class MachineryService:
    def __init__(self):
        with open("machinery.json", "r") as file:
            self.machinery_data = json.load(file)

    def get_all_machinery(self) -> List[Machinery]:
        return [Machinery(**machinery) for machinery in self.machinery_data]

    def get_machinery_by_id(self, machinery_id: str) -> Optional[Machinery]:
        for machinery in self.machinery_data:
            if machinery["id"] == machinery_id:
                return Machinery(**machinery)
        return None

    def get_machinery(self, type: Optional[str] = None, status: Optional[str] = None) -> List[Machinery]:
        filtered_machinery = self.machinery_data
        if type:
            filtered_machinery = [machinery for machinery in filtered_machinery if machinery["type"] == type]
        if status:
            filtered_machinery = [machinery for machinery in filtered_machinery if machinery["status"] == status]
        return [Machinery(**machinery) for machinery in filtered_machinery]
