from sqlalchemy import Column, String, Integer, Double, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship

from src.database.Database import Base


class Promotion(Base):
    __tablename__ = "promotions"

    Id = Column(Integer, primary_key=True, autoincrement=True)

    ProductIdMarketplace = Column(String, ForeignKey("products.ProductIdMarketplace", ondelete="SET NULL"))
    product = relationship("Product", back_populates="promotions")

    old_price = Column(Double)
    actual_price = Column(Double)
    discount = Column(Double)
    coupon = Column(String)
    date = Column(DateTime)
    score = Column(Integer)
    publish = Column(Boolean)