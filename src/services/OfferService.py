from tkinter import image_names
from webbrowser import Elinks

from schemas.OffersRequest import OffersRequest
from schemas.ProductData import ProductData

from src.exceptions.OffersErrors import create_offer_error
from src.repositories.ProductRepository import ProductRepository
from src.repositories.PromotionRepository import PromotionRepository
from src.services.ProductService import ProductService
from src.services.PromotionService import PromotionService

from src.schemas.PromotionData import PromotionData


class OfferService:

    product_repository = ProductRepository()
    promotion_repository = PromotionRepository()

    def process_offer(self, offer_data: OffersRequest):
        # Converterá o objeto rcebido em um dicionário python puro

        full_dict = offer_data.model_dump()

        product: ProductData = ProductData(
            ProductIdMarketplace= full_dict['ProductIdMarketplace'],
            name=full_dict['name'],
            category=full_dict['category'],
            link= full_dict['link'],
            marketplace= full_dict['marketplace'],
            image= full_dict['image'],
            assessment= full_dict['assessment'],
            brand= full_dict['brand'],
            stock= full_dict['stock'],
            sales_quantity= full_dict['sales_quantity'],
            publish= full_dict['publish']
        )

        promotion: PromotionData = PromotionData(
            ProductIdMarketplace= full_dict['ProductIdMarketplace'], # table products and promotion
            old_price= full_dict['old_price'], # table promotion
            actual_price= full_dict['actual_price'],
            discount=  full_dict['discount'],
            coupon=  full_dict['coupon'],
            date=  full_dict['date'],
            score=  full_dict['score']
        )

        product_service = ProductService(self.product_repository)
        promotion_service = PromotionService(self.promotion_repository)


        product_service.create_product(product)



        return product, promotion
