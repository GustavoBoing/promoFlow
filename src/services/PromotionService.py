from itertools import product
from tokenize import detect_encoding
from src.schemas.PromotionData import PromotionData

from src.exceptions.PromotionsErrors import *

class PromotionService:

    def create_promotion(self, promotion: PromotionData):
        #após todas as validações, a promoção será criada
        self.validate_promotion(promotion)
        pass

    def validate_promotion(self, promotion: PromotionData):
        #validar regras que serão impostas antes da promoção ser aprovada
        #Verificar se o preço antigo é menor que o atual
        #Verificar score
        #Verificar a porcentagem de desconto
        if self.validate_price(promotion.old_price, promotion.actual_price):
            promotion.discount = self.calculate_percent(promotion.old_price, promotion.actual_price)
            #self.verify_coupun()
            #self.define_score
        else:
            raise CreatePromotionError(promotion)

    def calculate_percent(self, old_price, actual_price):
        #calcular valor percentual da promoção
        discount = 100 - ((actual_price/old_price)*100)
        discount = round(discount, 1)

        if discount <= 10:
            raise QuantityDiscountError(discount)

        return discount

    def validate_price(self, old_price, actual_price):
        if old_price <= actual_price:
            raise DetectDiscountError(old_price, actual_price)

        return True
