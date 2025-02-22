from pydantic import BaseModel
from typing import Optional

class OrderCreate(BaseModel):
    product: str
    quantity: int

class OrderOut(BaseModel):
    id: str
    product: str
    quantity: int
    user_id: str

    class Config:
        from_attributes = True