# routers/client_router.py

from fastapi import APIRouter, HTTPException
from typing import List
from models.client import Client
from services.client_service import ClientService

router = APIRouter(prefix="/clients", tags=["Clients"])

client_service = ClientService()

@router.get("/", response_model=List[Client])
async def get_all_clients():
    return client_service.get_all_clients()

@router.get("/{client_id}", response_model=Client)
async def get_client_by_id(client_id: str):
    client = client_service.get_client_by_id(client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client
