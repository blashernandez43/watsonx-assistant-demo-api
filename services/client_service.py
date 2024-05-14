# services/client_service.py

import json
from typing import List, Optional
from models.client import Client

class ClientService:
    def __init__(self):
        with open("clients.json", "r") as file:
            self.clients_data = json.load(file)

    def get_all_clients(self) -> List[Client]:
        return [Client(**client) for client in self.clients_data]

    def get_client_by_id(self, client_id: str) -> Optional[Client]:
        for client in self.clients_data:
            if client["id"] == client_id:
                return Client(**client)
        return None
