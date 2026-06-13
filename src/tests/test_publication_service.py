import datetime
import unittest

from src.schemas.PromotionData import PromotionData
from src.services.PublicationService import PublicationService


class TestPublicationService(unittest.TestCase):

    promotion = PromotionData(
        ProductIdMarketplace= "123456",
        old_price= 400,
        actual_price= 200,
        discount= 50,
        coupon= None,
        date= datetime.datetime.now(),
        score= 50,
        publish= False
    )

    publication_service = PublicationService()

    def test_already_publish(self):
        self.promotion.publish = True
        self.assertFalse(self.publication_service.is_already_published(self.promotion))

    def test_score_valid(self):
        self.assertFalse(self.publication_service.is_score_valid(self.promotion))