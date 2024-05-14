# routers/payment_router.py

from fastapi import APIRouter, HTTPException
from typing import List
from models.payment import Payment
from services.payment_service import PaymentService

router = APIRouter(prefix="/payments", tags=["Payments"])

payment_service = PaymentService()

@router.get("/", response_model=List[Payment])
async def get_all_payments():
    return payment_service.get_all_payments()

@router.get("/{payment_id}", response_model=Payment)
async def get_payment_by_id(payment_id: str):
    payment = payment_service.get_payment_by_id(payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment
