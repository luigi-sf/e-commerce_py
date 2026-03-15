from sqlalchemy.orm import relationship
import uuid
from sqlalchemy import Column, String,Float,ForeignKey,Integer
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base
from app.models.seller import Seller


class Product(Base):

    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    name = Column(String, nullable=False)

    description = Column(String)

    price = Column(Float, nullable=False)

    stock = Column(Integer, default=0)

    seller_id = Column(UUID(as_uuid=True), ForeignKey("sellers.id"))

    seller = relationship("Seller", back_populates="products")