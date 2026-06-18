from src.exceptions.product_errors import BusinessError
from src.schemas.PromotionData import PromotionData

class ProductPublishError(BusinessError):
    def __init__(self, promotion: PromotionData):
        self.message = f"Promoção: \n{promotion} \njá foi publicada"
        super().__init__(self.message)

class ScoreInvalidError(BusinessError):
    def __init__(self, score):
        self.message = f"Score: {score} é inválido"
        super().__init__(self.message)