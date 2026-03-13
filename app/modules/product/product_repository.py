from sqlalchemy.orm import Session
from app.models.product import Product


class ProductRepository:

    def __init__(self, db: Session):
        self.db = db


    def create(self, product: Product):
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product


    def list(self):
        return self.db.query(Product).all()


    def get_by_id(self, product_id):
        return self.db.query(Product).filter(
            Product.id == product_id
        ).first()


    def delete(self, product):
        self.db.delete(product)
        self.db.commit()