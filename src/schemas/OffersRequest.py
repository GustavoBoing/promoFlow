from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, HttpUrl

class OffersRequest(BaseModel):
    ProductIdMarketplace: str = Field(...,) # table products and promotion
    name: str = Field(..., min_length=2) # table products
    category: str = Field(...,) # table products
    link: HttpUrl = Field(...,) # table products
    marketplace: Literal["Mercado Livre", "Shopee"] = Field(...,) # table products
    image: HttpUrl = Field(...,) # table products
    assessment: float = Field(...,) # table products
    brand: str = Field(...,) # table products
    stock: int = Field(...,) # table products
    sales_quantity: int = Field(...,) # table products
    publish: bool = Field(...,) # table products
    old_price: float = Field(...,) # table promotion
    actual_price: float = Field(...,) # table promotion
    discount: float = Field(...,) # table promotion
    coupon: str | None = None # table promotion
    date: datetime = Field(...,) # table promotion
    score: float = Field(...,) # table promotion