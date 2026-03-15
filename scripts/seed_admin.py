from app.core.database import SessionLocal

from app.core.security.hashed import hash_password
from app.models.user import User
from app.models.seller import Seller
from app.models.product import Product


db = SessionLocal()


def seed():

    admin = db.query(User).filter(
        User.email == "admin@email.com"
    ).first()

    if admin:
        print("Admin already exists")
        return

    admin = User(
        name="Admin",
        email="admin@email.com",
        password=hash_password("123456"),
        role="admin"
    )

    db.add(admin)
    db.commit()

    print("Admin created")


if __name__ == "__main__":
    seed()