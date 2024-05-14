# services/rental_contract_service.py

import json
from typing import List, Optional
from models.rental_contract import RentalContract

class RentalContractService:
    def __init__(self):
        with open("contracts.json", "r") as file:
            self.contract_data = json.load(file)

    def get_all_contracts(self) -> List[RentalContract]:
        return [RentalContract(**contract) for contract in self.contract_data]

    def get_contract_by_id(self, contract_id: str) -> Optional[RentalContract]:
        for contract in self.contract_data:
            if contract["id"] == contract_id:
                return RentalContract(**contract)
        return None
