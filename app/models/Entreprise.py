# System imports
from enum import Enum
# Libs imports
from pydantic import BaseModel

class Entreprise(BaseModel):
    id_entreprise: int = None
    firm: str
    location: str


class EntrepriseOptionnalFields(BaseModel):
    name: str = None
    surname: str = None
    email: str = None
    password_hash: str = None
    tel: str = None
    newsletter: bool = None
    is_client: bool = None