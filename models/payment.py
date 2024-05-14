# models/payment.py

from pydantic import BaseModel

class Payment(BaseModel):
    id: str
    contract_id: str
    client_id: str
    date: str
    amount: float
    payment_method: str
