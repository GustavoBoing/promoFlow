from sqlalchemy.orm import Session
from src.models.Product import Product

from src.exceptions.product_errors import GetProductError
from src.schemas.ProductData import ProductData

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db
        #self.products = []

    #salvar produto
    def save(self, product: ProductData):
        """Cria um produto no banco de dados"""
        #self.products.append(product)

        product_dto = product.__dict__

        db_product = Product(**product_dto)

        self.db.add(db_product)
        self.db.commit()

        return db_product

    #Filtrar todos os produtos
    def get_all(self):
        """Retorna todos os produtos da tabela"""
        #return self.products
        return self.db.query(Product).all()

    #Verificar se existe um produto identico
    def exists(self, product_id_marketplace: str):
        product = self.get_product_by_product_id_marketplace(product_id_marketplace)

        if product is not None:
            return True

        return False

    def get_product_by_product_id_marketplace(self, product_id_marketplace) -> Product | None:
        produto: Product | None = (
            self.db.query(Product)
           .filter_by(ProductIdMarketplace = product_id_marketplace)
           .first()
        )

        if produto is None:
            return None

        return produto

    def update(self, product: ProductData):
        product_old = self.get_product_by_product_id_marketplace(product.ProductIdMarketplace)

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

        self.db.commit()

        self.db.refresh(product_old)


        return product_old
