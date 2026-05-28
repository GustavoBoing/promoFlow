from schemas.ProductAndPromotionRequest import ProductAndPromotionRequest

class PromotionService:

    def create_promotion(self):
        #após todas as validações, a promoção será criada
        pass

    def validate_promotion(self):
        #validar regras que serão impostas antes da promoção ser aprovada
        pass

    def calculate_percent(self, old_price, actual_price):
        #calcular valor percentual da promoção
        pass

    def detect_discount(self, old_price, actual_price):
        #verificar se o preco atual é maior que o anterior
        pass

    def verify_coupun(self):
        #verificar a existência de cupons válidos para esse produto
        pass

