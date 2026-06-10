from src.exceptions.PromotionsErrors import GetPromotionError
from src.schemas.PromotionData import PromotionData


class PromotionRepository:
    def __init__(self):
        self.promotions = []

    def save(self, promotion: PromotionData):
        self.promotions.append(promotion)

        return promotion

    def exists(self, product_id_marketplace):
        for p in self.promotions:
            if p.ProductIdMarketplace == product_id_marketplace :
                return True

        return False

    def get_promotion_by_id_product(self, product_id_marketplace):
        for p in self.promotions:
            if p.ProductIdMarketplace == product_id_marketplace:
                return p

        return None

    def update(self, promotion: PromotionData):
        promotion_old: PromotionData = self.get_promotion_by_id_product(promotion.ProductIdMarketplace)

        if promotion_old is None:
            raise GetPromotionError

        promotion_old.old_price = promotion.old_price
        promotion_old.actual_price = promotion.actual_price
        promotion_old.discount = promotion.discount
        promotion_old.coupon = promotion.coupon
        promotion_old.date = promotion.date
        promotion_old.score = promotion.score
        promotion_old.publish = False

        return promotion_old

    def get_all(self):
        return self.promotions
