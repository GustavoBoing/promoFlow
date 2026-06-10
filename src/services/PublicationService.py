from src.exceptions.PublicationsErrors import ProductPublishError, ScoreInvalidError
from src.schemas.ProductData import ProductData
from src.schemas.PromotionData import PromotionData


class PublicationService:
    #definir regras de publicação
    #definir o que será publicado
    #evitar duplicidade de publicações
    #loop pelo que não foi publicado
    def evaluate_publication(self, promotion: PromotionData, product: ProductData):
        if not self.is_already_published(product):
            raise ProductPublishError(product)

        if not self.is_score_valid(promotion):
            raise ScoreInvalidError(promotion.score)

        product.publish = True

    def is_already_published(self, product: ProductData):
        if not product.publish:
            return True
        return False

    def is_score_valid(self, promotion: PromotionData):
        if promotion.score >= 80:
            return True
        return False
