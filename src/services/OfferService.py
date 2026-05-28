from schemas.OffersRequest import OffersRequest


class OfferService:
    def process_offer(self, offer_data: OffersRequest):
        # Converterá o objeto rcebido em um dicionário python puro
        full_dict = offer_data.model_dump()

        # Criar as chaves de cada dicionario
        product_keys = {
            "ProductIdMarketplace", "name", "categoria", "link",
            "marketplace", "image", "assessment", "brand",
            "stock", "sales_quantity", "publish"
        }

        promotion_keys = {
            "ProductIdMarketplace", "old_price", "actual_price",
            "discount", "coupon", "date", "score"
        }

        # Itera sobre os dados de full_dict para verificar se a
        # chave que esta nele corresponde a alguma chave do dicionario criado
        product = {k: v for k, v in full_dict.items() if k in product_keys}
        promotion = {k: v for k, v in full_dict.items() if k in promotion_keys}

        # print("dicionario promotion: ", promotion)
        # print("dicionario product: ", product)

