from src.exceptions.product_errors import GetProductError
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

    def get_product_by_product_id_marketplace(self, product_id_marketplace):
        for p in self.products:
            if p.ProductIdMarketplace == product_id_marketplace:
                return p

        return None

    def update(self, product: ProductData):
        product_old: ProductData = self.get_product_by_product_id_marketplace(product.ProductIdMarketplace)

        if product_old is None:
            raise GetProductError

        product_old.name = product.name
        product_old.category = product.category
        product_old.link = product.link
        product_old.marketplace = product.marketplace
        product_old.image = product.image
        product_old.assessment = product.assessment
        product_old.brand = product.brand
        product_old.stock = product.stock
        product_old.sales_quantity = product.sales_quantity


        return product_old
