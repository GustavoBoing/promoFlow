class BusinessError(Exception):
    pass

class ErrorDiscount(BusinessError):
    def __init__(self):
        self.message = "O preço antigo é menor que o preço atual. Não existe desconto!!"
        super().__init__(self.message)

class ErrorDiscountPercent(BusinessError):
    def __init__(self):
        self.message = f"A porcentagem de desconto é menor que o exigido"
        super().__init__(self.message)

class GetPromotionError(BusinessError):
    def __init__(self):
        self.message = "Promoção não encontrada"
        super().__init__(self.message)
