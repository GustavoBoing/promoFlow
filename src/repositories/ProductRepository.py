from src.schemas.ProductData import ProductData

class ProductRepository:
    def __init__(self):
        self.products = []

    #salvar produto
    def save(self, product: ProductData):
        self.products.append(product)

        return product

    #Filtrar todos os produtos
    def get_all(self):
        return self.products

    #Verificar se existe um produto identico
    def exists(self, product_id_marketplace: str):
        for p in self.products:
            if p.ProductIdMarketplace == product_id_marketplace:
                return True

        return False

