from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security.dependencies import get_current_user,require_role

from app.modules.seller.seller_schema import SellerCreate, SellerResponse
from app.modules.seller.seller_service import SellerService
from app.modules.seller.seller_repository import SellerRepository

from app.models.user import User


router = APIRouter(
    prefix="/sellers",
    tags=["sellers"]
)


def get_seller_service(db:Session = Depends(get_db)):
    repo = SellerRepository(db)
    return SellerService(repo)


@router.post('/', response_model=SellerResponse)
def create(
    data: SellerCreate,
    service: SellerService = Depends(get_seller_service),
    current_user: User = Depends(get_current_user)
):
    return service.create(data, current_user)



