from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from app.core.database import get_db
from app.core.security.dependencies import get_current_user, require_role

from app.models.user import User
from app.modules.seller.seller_schema import SellerCreate, SellerResponse, SellerUpdate
from app.modules.seller.seller_repository import SellerRepository
from app.modules.seller.seller_service import SellerService


router = APIRouter(
    prefix="/sellers",
    tags=["sellers"]
)


def get_seller_service(db: Session = Depends(get_db)):
    repo = SellerRepository(db)
    return SellerService(repo)


@router.post("/", response_model=SellerResponse)
def create(
    seller: SellerCreate,
    service: SellerService = Depends(get_seller_service),
    current_user: User = Depends(get_current_user)
):
    return service.create(seller, current_user)


@router.get("/", response_model=list[SellerResponse])
def list(
    service: SellerService = Depends(get_seller_service),
    current_user: User = Depends(require_role(["admin"]))
):
    return service.list()


@router.get("/{seller_id}", response_model=SellerResponse)
def get_by_id(
    seller_id: UUID,
    service: SellerService = Depends(get_seller_service),
    current_user: User = Depends(require_role(["admin"]))
):
    return service.get_by_id(seller_id)


@router.put("/{seller_id}", response_model=SellerResponse)
def update(
    seller_id: UUID,
    seller: SellerUpdate,
    service: SellerService = Depends(get_seller_service),
    current_user: User = Depends(require_role(["seller", "admin"]))
):
    return service.update(seller_id, seller, current_user)


@router.delete("/{seller_id}")
def delete(
    seller_id: UUID,
    service: SellerService = Depends(get_seller_service),
    current_user: User = Depends(require_role(["seller", "admin"]))
):
    return service.delete(seller_id, current_user)