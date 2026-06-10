from src.exceptions.product_errors import BusinessError
from src.schemas.ProductData import ProductData

class ProductPublishError(BusinessError):
    def __init__(self, product: ProductData):
        self.message = f"Produto: \n{product} \njá publicado"
        super().__init__(self.message)

class ScoreInvalidError(BusinessError):
    def __init__(self, score):
        self.message = f"Score: {score} é inválido"
        super().__init__(self.message)