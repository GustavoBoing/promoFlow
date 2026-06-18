from src.exceptions.product_errors import BusinessError

class create_offer_error(BusinessError):
    def __init__(self):
        self.message = "Erro ao criar nova promoção"
        super().__init__(self.message)