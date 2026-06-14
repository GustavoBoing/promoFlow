from sqlalchemy import create_engine # gerencia as conexões físicas do banco
from sqlalchemy.orm import sessionmaker # faz todas as operações do banco de dados(inserir, atualizar, deletar  e buscar)
from sqlalchemy.orm import declarative_base # Todas as classes que representam as tabelas devem herdar dessa classe

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/PromoFlow"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit= False,
    autoflush= False,
    bind=engine
)

Base = declarative_base()