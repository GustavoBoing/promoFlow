from src.exceptions.PromotionsErrors import ErrorDiscount
from src.schemas.PromotionData import PromotionData
from src.repositories.PromotionRepository import PromotionRepository

class PromotionService:

    def __init__(self, repository: PromotionRepository):
        self.repository = repository

    def create_promotion(self, promotion: PromotionData ):
        #após todas as validações, a promoção será criada

        return self.repository.save(promotion)


    @staticmethod
    def detect_discount(old_price, actual_price):
        #verificar se o preco atual é maior que o anterior
        if actual_price <= 0 or old_price <= 0:
            raise ErrorDiscount
        elif actual_price >= old_price:
            raise ErrorDiscount

    def validate_promotion(self, promotion: PromotionData):
        self.detect_discount(promotion.old_price, promotion.actual_price)
        promotion.discount = self.calculate_percent(promotion.old_price, promotion.actual_price)
        self.get_coupun(promotion)

    @staticmethod
    def calculate_percent(old_price, actual_price):
        percent = ((actual_price/old_price) - 1) * (-100)
        return percent

    def get_coupun(self, promotion: PromotionData):
        # lógica de receber cupom
        coupon = None

        #Inserindo dados do cupom na variável de promoção
        promotion.coupon = coupon

    def update_promotion(self, promotion: PromotionData):

        #self.validate_promotion(promotion)

        return self.repository.update(promotion)

