from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from app.core.database import get_db
from app.core.security.dependencies import get_current_user

from app.modules.product.product_schema import (
    ProductCreate,
    ProductUpdate,
    ProductResponse
)

from app.modules.product.product_repository import ProductRepository
from app.modules.product.product_service import ProductService

from app.modules.seller.seller_repository import SellerRepository
from app.models.user import User


router = APIRouter(
    prefix="/products",
    tags=["products"]
)


def get_product_service(db: Session = Depends(get_db)):
    product_repo = ProductRepository(db)
    seller_repo = SellerRepository(db)

    return ProductService(product_repo, seller_repo)


@router.post("/", response_model=ProductResponse)
def create(
    data: ProductCreate,
    service: ProductService = Depends(get_product_service),
    current_user: User = Depends(get_current_user)
):
    return service.create(data, current_user)


@router.get("/", response_model=list[ProductResponse])
def get(
    service: ProductService = Depends(get_product_service)
):
    return service.list()


@router.get("/me", response_model=list[ProductResponse])
def my_products(
    service: ProductService = Depends(get_product_service),
    current_user: User = Depends(get_current_user)
):
    return service.get_my_products(current_user)


@router.get("/{product_id}", response_model=ProductResponse)
def get_by_id(
    product_id: UUID,
    service: ProductService = Depends(get_product_service)
):
    return service.get_by_id(product_id)


@router.put("/{product_id}", response_model=ProductResponse)
def update(
    product_id: UUID,
    data: ProductUpdate,
    service: ProductService = Depends(get_product_service),
    current_user: User = Depends(get_current_user)
):
    return service.update(product_id, data, current_user)


@router.delete("/{product_id}")
def delete(
    product_id: UUID,
    service: ProductService = Depends(get_product_service),
    current_user: User = Depends(get_current_user)
):
    return service.delete(product_id, current_user)