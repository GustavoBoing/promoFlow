from typing import Literal
from pydantic import BaseModel, Field, HttpUrl

class ProductData(BaseModel):
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