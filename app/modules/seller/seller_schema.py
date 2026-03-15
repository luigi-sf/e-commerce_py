from pydantic import BaseModel
from uuid import UUID
from typing import Optional


class SellerCreate(BaseModel):
    store_name: str
    cpf: str
    cnpj: Optional[str] = None

    phone: str

    city: str
    state: str
    country: str = "Brasil"

    address: Optional[str] = None
    zip_code: Optional[str] = None



class SellerUpdate(BaseModel):
    store_name: Optional[str] = None
    cpf: Optional[str] = None
    cnpj: Optional[str] = None

    phone: Optional[str] = None

    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None

    address: Optional[str] = None
    zip_code: Optional[str] = None
    
    
class SellerResponse(BaseModel):
    id: UUID

    store_name: str

    cpf: Optional[str] = None
    cnpj: Optional[str] = None

    phone: Optional[str] = None

    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None

    address: Optional[str] = None
    zip_code: Optional[str] = None

    user_id: UUID
    class Config:
        from_attributes = True