from src.exceptions.PublicationsErrors import ProductPublishError, ScoreInvalidError
from src.schemas.ProductData import ProductData
from src.schemas.PromotionData import PromotionData
from src.services.TelegramService import TelegramService


class PublicationService:
    #definir regras de publicação
    #definir o que será publicado
    #evitar duplicidade de publicações
    #loop pelo que não foi publicado

    telegram_service = TelegramService()

    async def evaluate_publication(self, promotion: PromotionData, product: ProductData):
        if not self.is_already_published(promotion):
            raise ProductPublishError(promotion)

        if not self.is_score_valid(promotion):
            raise ScoreInvalidError(promotion.score)

        await self.telegram_service.publish_offer(promotion, product)

        promotion.publish = True

    def is_already_published(self, promotion: PromotionData):
        if not promotion.publish:
            return True
        return False

    def is_score_valid(self, promotion: PromotionData):
        if promotion.score >= 70:
            return True
        return False
