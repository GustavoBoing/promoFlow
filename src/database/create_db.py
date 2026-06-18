from src.database.Database import engine, Base

from src.models.Product import Product
from src.models.Promotion import Promotion

print("Criando as tabelas no PostgreSQL")
Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso")