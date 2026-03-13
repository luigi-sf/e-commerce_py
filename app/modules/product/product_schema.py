from pydantic import BaseModel
from uuid import UUID


class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    stock: int


class ProductUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    stock: int | None = None


class ProductResponse(BaseModel):
    id: UUID
    name: str
    description: str
    price: float
    stock: int
    seller_id: UUID

    class Config:
        from_attributes = True