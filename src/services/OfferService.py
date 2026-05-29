from tkinter import image_names
from webbrowser import Elinks

from schemas.OffersRequest import OffersRequest
from schemas.ProductData import ProductData

class OfferService:
    def process_offer(self, offer_data: OffersRequest):
        # Converterá o objeto rcebido em um dicionário python puro
        full_dict = offer_data.model_dump()

        promotion_keys = {
            "ProductIdMarketplace", "old_price", "actual_price",
            "discount", "coupon", "date", "score"
        }
        product = ProductData(
            ProductIdMarketplace= full_dict['ProductIdMarketplace'],
            name=full_dict['name'],
            category=full_dict['category'],
            link= full_dict['link'],
            marketplace= full_dict['marketplace'],
            image= full_dict['image'],
            assessment= full_dict['assessment'],
            brand= full_dict['brand'],
            stock= full_dict['stock'],
            sales_quantity= full_dict['sales_quantity'],
            publish= full_dict['publish']
        )

        #product = {k: v for k, v in full_dict.items() if k in product_keys}
        #promotion = {k: v for k, v in full_dict.items() if k in promotion_keys}



        # print("dicionario promotion: ", promotion)
        # print("dicionario product: ", product)

