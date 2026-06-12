import unittest
from itertools import product

from src.exceptions.product_errors import CategoryInvalid, StockQuantityInvalid, AssessmentInvalid, SalesQuantityInvalid
from src.schemas.ProductData import ProductData
from src.services.ProductService import ProductService

from src.repositories.ProductRepository import ProductRepository

#Validar produto

class TestProductService(unittest.TestCase):

    product_repository = ProductRepository()

    product_service = ProductService(product_repository)

    product_data = ProductData(
        ProductIdMarketplace= "123456789",
        name= "produto1",
        category= "moda fitness",
        link= "https://image.com",
        marketplace= "Mercado Livre",
        image= "https://image.com",
        assessment= 9.0,
        brand= "Nike",
        stock= 50,
        sales_quantity= 60
    )

    def test_validate_category(self):
        self.product_data.category = "carro"
        with self.assertRaises(CategoryInvalid) as contexto:
            self.product_service.validate_product(self.product_data)

        self.assertEqual(str(contexto.exception), f"A categoria {self.product_data.category} não é válida")

        #self.assertRaises(CategoryInvalid, self.product_service.validate_product, self.product_data.category)

    def test_validate_stock(self):
        self.product_data.stock = 0

        with self.assertRaises(StockQuantityInvalid) as context:
            self.product_service.validate_product(self.product_data)

        self.assertEqual(str(context.exception), f"A quantidade em estoque {self.product_data.stock} é inválida. Deve ser maior que zero")

    def test_validate_assessment(self):
        self.product_data.assessment = 5

        with self.assertRaises(AssessmentInvalid) as context:
            self.product_service.validate_product(self.product_data)

        self.assertEqual(str(context.exception), f"A nota {self.product_data.assessment} para o produto não é válida")

    def test_validate_sales_quantity(self):
        self.product_data.sales_quantity = 1

        with self.assertRaises(SalesQuantityInvalid) as context:
            self.product_service.validate_product(self.product_data)

        self.assertEqual(str(context.exception), f"A quantidade {self.product_data.sales_quantity} vendida é inválida")