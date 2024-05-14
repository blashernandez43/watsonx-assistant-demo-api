# models/client.py

from pydantic import BaseModel

class Client(BaseModel):
    id: str
    name: str
    contact_information: str
    company: bool
    billing_address: str
