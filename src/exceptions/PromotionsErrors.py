from src.schemas.PromotionData import PromotionData


class BusinessError(Exception):
    """Classe base para todos os erros de négocio da promotionsService"""
    pass

class CreatePromotionError(BusinessError):
    def __init__(self, product: PromotionData):
        self.message = f"Falha ao criar o produto: {product}"
        super().__init__(self.message)

class DetectDiscountError(BusinessError):
    def __init__(self, old_price, actual_price):
        self.message = f"O valor não é um desconto válido porque o preço antigo é R${old_price}, e o preço atual é R${actual_price}"
        super().__init__(self.message)

class QuantityDiscountError(BusinessError):
    def __init__(self, discount):
        self.message = f"O valor do desconto é muito abaixo. Desconto = {discount}%"
        super().__init__(self.message)