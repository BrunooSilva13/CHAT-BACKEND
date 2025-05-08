from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, create_db

DATABASE_URL = "sqlite:///./chat.db"

# Criar conexão com o banco
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Sessão do banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função para obter a sessão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Criar o banco de dados
create_db(engine)
