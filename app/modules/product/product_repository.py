from sqlalchemy.orm import Session
from uuid import UUID
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


    def get_by_id(self, product_id: UUID):
        return self.db.query(Product).filter(
            Product.id == product_id
        ).first()


    def get_by_seller(self, seller_id:UUID):
        return self.db.query(Product).filter(
        Product.seller_id == seller_id
    ).all()

    def update(self, product: Product, data):

        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(product, key, value)

        self.db.commit()
        self.db.refresh(product)

        return product


    def delete(self, product: Product):
        self.db.delete(product)
        self.db.commit()
        return product