from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security.dependencies import get_current_user

from app.modules.product.product_schema import (
    ProductCreate,
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
def list(service: ProductService = Depends(get_product_service)):

    return service.repo.list()