from sqlalchemy.orm import Session
from app.models.seller import Seller
from app.modules.seller.seller_schema import SellerCreate, SellerResponse,SellerUpdate
from app.models.user import User
from uuid import UUID


class SellerRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, seller: SellerCreate, current_user: User):

        db_seller = Seller(
            **seller.model_dump(),
            user_id=current_user.id
        )

        self.db.add(db_seller)
        self.db.commit()
        self.db.refresh(db_seller)

        return db_seller
    
    
    def list(self):
        return self.db.query(Seller).all()
    
    


    def get_by_user(self, user_id:UUID):
        return self.db.query(Seller).filter(
            Seller.user_id == user_id
        ).first()
        
    
    def  get_by_id(self,seller_id:UUID):
        return self.db.query(Seller).filter(
            Seller.id == seller_id
        ).first
        
        
    
    def update(self, seller_id: UUID, seller: SellerUpdate, user_id: UUID):

        db_seller = self.db.query(Seller).filter(
        Seller.id == seller_id,
        Seller.user_id == user_id
        ).first()

        if not db_seller:
            return None

        for key, value in seller.model_dump(exclude_unset=True).items():
            setattr(db_seller, key, value)

        self.db.commit()
        self.db.refresh(db_seller)

        return db_seller
    
    
    
    def delete(self, seller_id:UUID):
        db_seller = self.get_by_id(seller_id)
        
        if not db_seller:
            return None
        
        self.db.delete(db_seller)
        self.db.commit()
        
        
        return db_seller

        