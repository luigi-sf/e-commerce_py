from sqlalchemy.orm import Session
from app.models.seller import Seller


class SellerRepository:
    
    def __init__(self, db:Session):
        self.db = db
        
        
        
    
    def create (self, seller:Seller):
        self.db.add(seller)
        self.db.commit()
        self.db.refresh(seller)
        return seller
    
    
    
    def get_by_user(self,user_id):
        return self.db.query(Seller).filter(
            Seller.user_id == user_id
        ).first()
        


