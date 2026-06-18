from sqlalchemy import Column, String, Integer, Double
from sqlalchemy.orm import relationship

from src.database.Database import Base

class Product(Base):
    __tablename__ = "products"

    ProductIdMarketplace = Column(String(100), primary_key=True)

    promotions = relationship("Promotion", back_populates="product")

    name = Column(String(100))
    category = Column(String(50))
    link = Column(String(100))
    marketplace = Column(String(50))
    image = Column(String(200))
    assessment = Column(Double)
    brand = Column(String(50))
    stock = Column(Integer)
    sales_quantity = Column(Integer)