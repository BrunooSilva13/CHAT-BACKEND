import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, create_db

# Lê variáveis de ambiente do Docker (.env)
POSTGRES_USER = os.getenv("POSTGRES_USER", "admin")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "admin")
POSTGRES_DB = os.getenv("POSTGRES_DB", "chatdb")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "db")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

# URL do banco PostgreSQL
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Criar conexão com o banco
engine = create_engine(DATABASE_URL)

# Sessão do banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função para obter a sessão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Criar o banco de dados (as tabelas definidas no Base)
create_db(engine)
