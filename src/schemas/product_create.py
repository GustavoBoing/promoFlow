from typing import Literal
from pydantic import BaseModel, Field, HttpUrl

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=2)
    categoria: str = Field(...,)
    link: HttpUrl = Field(...,)
    marketplace: Literal["Mercado Livre", "Shopee"] = Field(...,)
    image: HttpUrl = Field(...,)
    assessment: float = Field(...,)
    brand: str = Field(...,)
    stock: int = Field(...,)
    sales_quantity: int = Field(...,)