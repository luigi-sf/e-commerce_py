from fastapi import HTTPException
from uuid import UUID

from app.models.product import Product
from app.models.user import User

from app.modules.product.product_schema import ProductCreate, ProductUpdate


class ProductService:

    def __init__(self, repo, seller_repo):
        self.repo = repo
        self.seller_repo = seller_repo


    def create(self, data: ProductCreate, current_user: User):

        seller = self.seller_repo.get_by_user(current_user.id)

        if not seller:
            raise HTTPException(400, "User is not a seller")

        product = Product(
            **data.model_dump(),
            seller_id=seller.id
        )

        return self.repo.create(product)


    def list(self):
        return self.repo.list()


    def get_by_id(self, product_id: UUID):

        product = self.repo.get_by_id(product_id)

        if not product:
            raise HTTPException(404, "Product not found")

        return product


    def get_my_products(self, current_user: User):

        seller = self.seller_repo.get_by_user(current_user.id)

        if not seller:
            raise HTTPException(404, "Seller not found")

        return self.repo.get_by_seller(seller.id)


    def update(self, product_id: UUID, data: ProductUpdate, current_user: User):

        product = self.repo.get_by_id(product_id)

        if not product:
            raise HTTPException(404, "Product not found")

        seller = self.seller_repo.get_by_user(current_user.id)

        if not seller or product.seller_id != seller.id:
            raise HTTPException(403, "Not authorized")

        return self.repo.update(product, data)


    def delete(self, product_id: UUID, current_user: User):

        product = self.repo.get_by_id(product_id)

        if not product:
            raise HTTPException(404, "Product not found")

        seller = self.seller_repo.get_by_user(current_user.id)

        if not seller or product.seller_id != seller.id:
            raise HTTPException(403, "Not authorized")

        return self.repo.delete(product)