from sqlalchemy.orm import relationship
import uuid
from sqlalchemy import Column, String,ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base


class Seller(Base):

    __tablename__ = "sellers"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    store_name = Column(String, nullable=False)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    user = relationship("User", back_populates="seller")
    
    products = relationship("Product", back_populates="seller")