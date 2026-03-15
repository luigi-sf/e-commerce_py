from sqlalchemy.orm import relationship
import uuid
from sqlalchemy import Column, String,ForeignKey,Boolean
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base


class Seller(Base):

    __tablename__ = "sellers"
    
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    store_name = Column(String, nullable=False)

    cpf = Column(String, unique=True)
    cnpj = Column(String, unique=True)

    phone = Column(String)

    city = Column(String)
    state = Column(String)
    country = Column(String, default="Brasil")

    address = Column(String)
    zip_code = Column(String)

    is_active = Column(Boolean, default=True)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    user = relationship("User", back_populates="seller")

    products = relationship("Product", back_populates="seller")