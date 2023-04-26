# System imports
from enum import Enum
# Libs imports
from pydantic import BaseModel

class Planning(BaseModel):
    id_planning: int = None
    name: str
    surname: str
    email: str
    password_hash: str
    tel: str

class PlanningOptionnalFields(BaseModel):
    name: str = None
    surname: str = None
    email: str = None
    password_hash: str = None
    tel: str = None