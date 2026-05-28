class BusinessError(Exception):
    """Classe base para todos os erros de négocio da aplicação"""
    pass

class PriceInvalidError(BusinessError):
    """Lançado quando o preço é menor ou igual a zero"""
    def __init__(self, price):
        self.message = f"O preço R$ {price} é inválido. Deve ser maior que zero."
        super().__init__(self.message)

class StockQuantityInvalid(BusinessError):
    """Lançado quando o stock é menor ou igual a zero"""
    def __init__(self, stock):
        self.message = f"A quantidade em estoque {stock} é inválida. Deve ser maior que zero"
        super().__init__(self.message)

class CategoryInvalid(BusinessError):
    """Lançado quando a categoria não é inválida"""
    def __init__(self, category):
        self.message = f"A categoria {category} não é válida"
        super().__init__(self.message)

class AssessmentInvalid(BusinessError):
    """Lançado quando a nota do produto não é inválida"""
    def __init__(self, assessment):
        self.message = f"A nota {assessment} para o produto não é válida"
        super().__init__(self.message)

class SalesQuantityInvalid(BusinessError):
    """Lançado quando a quantidade vendida não é inválida"""
    def __init__(self, salesQuantity):
        self.message = f"A quantidade {salesQuantity} vendida é inválida"
        super().__init__(self.message)
