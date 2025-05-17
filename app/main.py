"""
main.py - Módulo principal da API de chat

Este arquivo define a aplicação FastAPI, configura a conexão com o banco de dados SQLite,
define o modelo de dados para mensagens, cria a tabela no banco (caso não exista),
e expõe uma rota de exemplo para consulta de mensagens.

Fluxo principal:
- Criação da instância FastAPI
- Configuração do banco de dados SQLite
- Definição do modelo Message
- Criação da tabela no banco
- Criação da sessão de banco de dados
- Definição da rota '/hello'
"""

from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Criando a instância FastAPI
app = FastAPI()

# Definindo a URL de conexão do banco SQLite
DATABASE_URL = "sqlite:///./chat.db"

# Criando a engine para conectar ao banco SQLite
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Definindo a base para os modelos de dados
Base = declarative_base()

# Definindo o modelo de dados para mensagens
class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)

# Criando o banco de dados (caso não exista)
Base.metadata.create_all(bind=engine)

# Criando a sessão para interagir com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para obter todas as mensagens do banco de dados
@app.get("/hello")
def read_root(db: Session = Depends(get_db)):
    messages = db.query(Message).all()
    return {"messages": "OLá mundo"}
