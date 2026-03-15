from app.core.database import Base, engine

# IMPORTAR TODOS OS MODELS
from app.models.user import User
from app.models.seller import Seller
from app.models.product import Product

print("Resetando banco...")

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

print("Banco resetado!")