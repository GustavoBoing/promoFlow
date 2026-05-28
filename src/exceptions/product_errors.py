class BusinessError(Exception):
    """Classe base para todos os erros de négocio da aplicação"""
    pass

class PriceInvalidError(BusinessError):
    pass

class StockQuantityInvalid(BusinessError):
    pass

class CategoryInvalid(BusinessError):
    pass

class AssessmentInvalid(BusinessError):
    pass

class SalesQuantityInvalid(BusinessError):
    pass