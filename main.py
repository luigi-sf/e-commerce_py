from fastapi import FastAPI
from app.core.database import Base, engine

# routers
from app.modules.user.user_controller import router as user_router
from app.modules.auth.auth_controller import router as auth_router
from app.modules.seller.seller_controller import router as seller_router
from app.modules.product.product_controller import router as product_router


app = FastAPI(
    title="Marketplace API",
    version="1.0.0"
)


# cria tabelas automaticamente
Base.metadata.create_all(bind=engine)


# routers
app.include_router(auth_router, prefix="/auth")
app.include_router(user_router)
app.include_router(seller_router)
app.include_router(product_router)


@app.get("/")
def root():
    return {"message": "Marketplace API running"}