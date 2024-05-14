# models/rental_contract.py

from pydantic import BaseModel

class RentalContract(BaseModel):
    id: str
    machinery_id: str
    client_id: str
    start_date: str
    end_date: str
    total_rental_cost: float
    payment_status: str
    terms_and_conditions: str
