from fastapi import HTTPException
from app.models.product import Product
from app.models.user import User


class ProductService:

    def __init__(self, repo, seller_repo):
        self.repo = repo
        self.seller_repo = seller_repo


    def create(self, data, current_user: User):

        seller = self.seller_repo.get_by_user(current_user.id)

        if not seller:
            raise HTTPException(400, "User is not a seller")

        product = Product(
            name=data.name,
            description=data.description,
            price=data.price,
            stock=data.stock,
            seller_id=seller.id
        )

        return self.repo.create(product)