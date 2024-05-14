# routers/machinery_router.py

from fastapi import APIRouter, HTTPException, Query
from typing import List
from models.machinery import Machinery
from services.machinery_service import MachineryService

router = APIRouter(prefix="/machinery", tags=["Machinery"])

machinery_service = MachineryService()

@router.get("/", response_model=List[Machinery])
async def get_machinery(
    type: str = Query(None, title="Machinery Type"),
    status: str = Query(None, title="Machinery Status"),
    ):
    machinery = machinery_service.get_machinery(type, status)
    return machinery

@router.get("/{machinery_id}", response_model=Machinery)
async def get_machinery_by_id(machinery_id: str):
    machinery = machinery_service.get_machinery_by_id(machinery_id)
    if not machinery:
        raise HTTPException(status_code=404, detail="Machinery not found")
    return machinery
