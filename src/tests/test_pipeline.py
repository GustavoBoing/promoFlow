import asyncio

from src.database.Database import SessionLocal
from src.services.OfferService import OfferService
from src.schemas.OffersRequest import OffersRequest

offer = OffersRequest(
    ProductIdMarketplace="123",
    name="Tênis Nike Air Max",
    category="Moda Fitness",
    link="https://produto.com",
    marketplace="Mercado Livre",
    image="https://imagem.com",
    assessment=9.2,
    brand="Nike",
    stock=5,
    sales_quantity=50,
    publish=False,
    old_price=499.90,
    actual_price=299.90,
    discount=0,
    coupon=None,
    date="2026-06-11",
    score=0
)

async def main():
    db = SessionLocal()

    service = OfferService(db)

    await service.process_offer(offer)

    db.close()

if __name__ == "__main__":
    asyncio.run(main())