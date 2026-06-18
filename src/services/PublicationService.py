from requests.sessions import Session

from src.exceptions.PublicationsErrors import ProductPublishError, ScoreInvalidError
from src.repositories.PromotionRepository import PromotionRepository
from src.schemas.ProductData import ProductData
from src.schemas.PromotionData import PromotionData
from src.services.PromotionService import PromotionService
from src.services.TelegramService import TelegramService


class PublicationService:
    #definir regras de publicação
    #definir o que será publicado
    #evitar duplicidade de publicações
    #loop pelo que não foi publicado

    def __init__(self, db: Session):
        self.db = db
        self.telegram_service = TelegramService()
        self.promotion_service = PromotionService(self.db)

    async def evaluate_publication(self, promotion: PromotionData, product: ProductData):
        # if not self.is_already_published(promotion):
        #     raise ProductPublishError(promotion)

        if not self.is_score_valid(promotion):
            raise ScoreInvalidError(promotion.score)

        await self.telegram_service.publish_offer(promotion, product)

    # def is_already_published(self, promotion: PromotionData):
    #     if not promotion.publish:
    #         return True
    #     return False

    def is_score_valid(self, promotion: PromotionData):
        if promotion.score >= 70:
            return True
        return False
