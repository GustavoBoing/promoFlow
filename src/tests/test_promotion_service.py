import unittest

from src.exceptions.PromotionsErrors import ErrorDiscount, ErrorDiscountPercent
from src.repositories.PromotionRepository import PromotionRepository
from src.services.PromotionService import PromotionService


class TestPromotionService(unittest.TestCase):

    promotion_repository = PromotionRepository()

    promotion_service = PromotionService(promotion_repository)

    def test_detect_discount_actual_price_more_than_old_price(self):
        #Verificar se o preco atual é maior que o antigo
        with self.assertRaises(ErrorDiscount) as context:
            self.promotion_service.detect_discount(400, 600)

        self.assertEqual(str(context.exception), "O preço antigo é menor que o preço atual. Não existe desconto!!")


    def test_detect_discount_actual_price_less_than_zero(self):
        #Verifica se o preço atual é menor que 0
        with self.assertRaises(ErrorDiscount) as context:
            self.promotion_service.detect_discount(40, -50)

        self.assertEqual(str(context.exception), "O preço antigo é menor que o preço atual. Não existe desconto!!")

    def test_detect_discount_old_price_less_than_zero(self):
        #Verifica se o preço antigo é menor que 0
        with self.assertRaises(ErrorDiscount) as context:
            self.promotion_service.detect_discount(40, -50)

        self.assertEqual(str(context.exception), "O preço antigo é menor que o preço atual. Não existe desconto!!")

    def test_detect_discount_percent(self):
        old_price = 80
        actual_price = 75

        #discount = self.promotion_service.calculate_percent(old_price, actual_price)

        with self.assertRaises(ErrorDiscountPercent) as context:
            self.promotion_service.calculate_percent(old_price, actual_price)

        self.assertEqual(str(context.exception), f"A porcentagem de desconto é menor que o exigido")