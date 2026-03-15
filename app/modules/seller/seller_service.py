from fastapi import HTTPException
from uuid import UUID
from app.models.user import User
from app.modules.seller.seller_repository import SellerRepository
from app.modules.seller.seller_schema import SellerCreate, SellerUpdate


class SellerService:

    def __init__(self, repo: SellerRepository):
        self.repo = repo


    def create(self, data: SellerCreate, current_user: User):

        seller_exists = self.repo.get_by_user(current_user.id)

        if seller_exists:
            raise HTTPException(400, "User already has a store")

        return self.repo.create(data, current_user)


    def list(self):
        return self.repo.list()


    def get_by_id(self, seller_id: UUID):

        seller = self.repo.get_by_id(seller_id)

        if not seller:
            raise HTTPException(404, "Seller not found")

        return seller


    def update(self, seller_id: UUID, data: SellerUpdate, current_user: User):

        seller = self.repo.get_by_id(seller_id)

        if not seller:
            raise HTTPException(404, "Seller not found")

        if seller.user_id != current_user.id:
            raise HTTPException(403, "Not authorized")

        return self.repo.update(seller_id, data)


    def delete(self, seller_id: UUID, current_user: User):

        seller = self.repo.get_by_id(seller_id)

        if not seller:
            raise HTTPException(404, "Seller not found")

        if seller.user_id != current_user.id:
            raise HTTPException(403, "Not authorized")

        return self.repo.delete(seller_id)