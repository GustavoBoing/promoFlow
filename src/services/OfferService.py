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
from src.services.PublicationService import PublicationService
from src.services.ScoringService import ScoringService


class OfferService:

    product_repository = ProductRepository()
    promotion_repository = PromotionRepository()
    publication_service = PublicationService()

    async def process_offer(self, offer_data: OffersRequest):
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
            sales_quantity= full_dict['sales_quantity']
        )

        promotion: PromotionData = PromotionData(
            ProductIdMarketplace= full_dict['ProductIdMarketplace'], # table products and promotion
            old_price= full_dict['old_price'], # table promotion
            actual_price= full_dict['actual_price'],
            discount=  full_dict['discount'],
            coupon=  full_dict['coupon'],
            date=  full_dict['date'],
            score=  full_dict['score'],
            publish= full_dict['publish']
        )

        product_service = ProductService(self.product_repository)
        promotion_service = PromotionService(self.promotion_repository)

        #Normalizando produto
        product_service.normalize_product(product)
        product_service.validate_product(product)

        #Normalizando promoção
        promotion_service.validate_promotion(promotion)

        #Inserir score na variável promotion
        scoring_service = ScoringService()

        score = scoring_service.calculate_score(#product.name, product.assessment, product.stock, product.sales_quantity, promotion.old_price,
                                        #promotion.actual_price, promotion.discount, promotion.coupon
                                                promotion, product)


        if score['score'] is None:
            raise ValueError("Score está vazio. Não é possível concluir o processo")

        promotion.score = score['score']

        if self.product_repository.exists(product.ProductIdMarketplace):
            product_service.update_product(product)

            if self.promotion_repository.exists(promotion.ProductIdMarketplace):
                promotion_service.update_promotion(promotion)
            else:
                promotion_service.create_promotion(promotion)
        else:
            product_service.create_product(product)
            promotion_service.create_promotion(promotion)

        await self.publication_service.evaluate_publication(promotion, product)

        #product_service.create_product(product)
        return product, promotion
