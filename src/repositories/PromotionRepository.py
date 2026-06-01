from src.schemas.PromotionData import PromotionData


class PromotionRepository:
    def __init__(self):
        self.promotions = []

    def save(self, promotion: PromotionData):
        self.promotions.append(promotion)

        return promotion

    def get_all(self):
        return self.promotions
