from sqlalchemy.orm import Session
from src.models.Promotion import Promotion

from src.exceptions.PromotionsErrors import GetPromotionError
from src.schemas.PromotionData import PromotionData


class PromotionRepository:
    def __init__(self, db: Session):
        #self.promotions = []
        self.db = db

    def save(self, promotion: PromotionData):
        """Cria uma promoção no banco de dados"""
        #self.promotions.append(promotion)

        promotion_dto = promotion.model_dump()

        promotion_db = Promotion(**promotion_dto)

        self.db.add(promotion_db)
        self.db.commit()

        return promotion_db

    def get_promotion_by_id_product(self, product_id_marketplace) -> Promotion | None:
        # for p in self.promotions:
        #     if p.ProductIdMarketplace == product_id_marketplace:
        #         return p

        promotion: Promotion | None = (
            self.db.query(Promotion)
            .filter_by(ProductIdMarketplace = product_id_marketplace)
            .first()
        )

        if promotion is not None:
            return promotion

        return None

    def exists(self, product_id_marketplace):
        promotion = self.get_promotion_by_id_product(product_id_marketplace)

        if promotion is not None:
            return True

        return False

    def update(self, promotion: PromotionData):
        promotion_old = self.get_promotion_by_id_product(promotion.ProductIdMarketplace)

        if promotion_old is None:
            raise GetPromotionError

        promotion_old.old_price = promotion.old_price
        promotion_old.actual_price = promotion.actual_price
        promotion_old.discount = promotion.discount
        promotion_old.coupon = promotion.coupon
        promotion_old.date = promotion.date
        promotion_old.score = promotion.score
        promotion_old.publish = False

        self.db.commit()
        self.db.refresh(promotion_old)

        return promotion_old

    def get_all(self):
        return self.db.query(Promotion).all()
