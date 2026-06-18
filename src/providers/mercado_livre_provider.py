from src.providers.base_provider import BaseProvider
from src.schemas.OffersRequest import OffersRequest


class MercadoLivreProvider(BaseProvider):
    def get_offers(self):
        return [
           OffersRequest (
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
        ]