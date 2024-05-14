# models/machinery.py

from pydantic import BaseModel
from typing import List, Optional

class MaintenanceRecord(BaseModel):
    maintenance_id: str
    date: str
    description: str
    cost: float
    technician: str

class Machinery(BaseModel):
    id: str
    name: str
    type: str
    model: str
    manufacturer: str
    year_of_manufacture: int
    rental_rate_per_day: float
    status: str
    maintenance_history: List[MaintenanceRecord] = []
