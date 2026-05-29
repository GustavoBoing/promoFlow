from datetime import datetime
from pydantic import BaseModel, Field

class PromotionData(BaseModel):
    ProductIdMarketplace: str = Field(...,) # table products and promotion
    old_price: float = Field(...,) # table promotion
    actual_price: float = Field(...,) # table promotion
    discount: float = Field(...,) # table promotion
    coupon: str | None = None # table promotion
    date: datetime = Field(...,) # table promotion
    score: float = Field(...,) # table promotion