import pyshorteners
from src.exceptions.product_errors import *
from src.repositories.ProductRepository import ProductRepository
from src.schemas.ProductData import ProductData

class ProductService:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def create_product(self, product: ProductData):
        self.normalize_product(product)
        self.validate_product(product)
        #productRepository deve ser chamado para que os dados sejam persistidos

        return self.repository.save(product)

    #moda fitness e saúde são as categorias escolhidas
    def validate_product(self, product: ProductData):
        category_permits = ["saúde", "moda fitness"]

        #if product.category == "Saúde" or product.category == "Moda Fitness":
        if product.category in category_permits:
            if product.stock <= 0:
                raise StockQuantityInvalid(product.stock)

            if product.assessment < 8:
                raise AssessmentInvalid(product.assessment)

            if product.sales_quantity < 2:
                raise SalesQuantityInvalid(product.sales_quantity)

        else:
            raise CategoryInvalid(product.category)

        #validar regras que serão setadas para cada produto antes de qualquer outra etapa

    #normalizar o produto
    def normalize_product(self, product: ProductData):
        s = pyshorteners.Shortener()

        product.name = product.name.strip().lower()
        product.category = product.category.strip().lower()
        # product.image = s.tinyurl.short(product.image)
        product.brand = product.brand.strip().lower()

        return product

    def update_product(self, product: ProductData):
        self.normalize_product(product)
        self.validate_product(product)

        return self.repository.update(product)