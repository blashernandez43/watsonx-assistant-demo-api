# services/payment_service.py

import json
from typing import List, Optional
from models.payment import Payment

class PaymentService:
    def __init__(self):
        with open("payments.json", "r") as file:
            self.payment_data = json.load(file)

    def get_all_payments(self) -> List[Payment]:
        return [Payment(**payment) for payment in self.payment_data]

    def get_payment_by_id(self, payment_id: str) -> Optional[Payment]:
        for payment in self.payment_data:
            if payment["id"] == payment_id:
                return Payment(**payment)
        return None
