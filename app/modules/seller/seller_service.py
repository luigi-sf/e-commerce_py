from sqlalchemy.orm import Session
from app.models.seller import Seller
from fastapi import HTTPException
from app.models.user import User
from app.modules.seller.seller_repository import SellerRepository


class SellerService:
    
    def __init__(self,repo:SellerRepository):
        self.repo = repo
        
        
    def create(self,data,current_user: User):
        
        seller_exists = self.repo.get_by_user(current_user.id)
        
        if seller_exists:
            raise HTTPException(400, 'User already has a store')
        
        seller = Seller(
            store_name = data.store_name,
            user_id = current_user.id
        )
        
        return self.repo.create(seller)
