from pydantic import BaseModel
from uuid import UUID


class SellerCreate(BaseModel):
    store_name: str


class SellerResponse(BaseModel):
    id: UUID
    store_name: str
    user_id: UUID

    class Config:
        from_attributes = True