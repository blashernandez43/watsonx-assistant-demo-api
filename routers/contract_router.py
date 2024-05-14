# routers/contract_router.py

from fastapi import APIRouter, HTTPException
from typing import List
from models.rental_contract import RentalContract
from services.rental_contract_service import RentalContractService

router = APIRouter(prefix="/contracts", tags=["Contracts"])

contract_service = RentalContractService()

@router.get("/", response_model=List[RentalContract])
async def get_all_contracts():
    return contract_service.get_all_contracts()

@router.get("/{contract_id}", response_model=RentalContract)
async def get_contract_by_id(contract_id: str):
    contract = contract_service.get_contract_by_id(contract_id)
    if not contract:
        raise HTTPException(status_code=404, detail="Contract not found")
    return contract
