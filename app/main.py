from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import engine, Base, get_db
from .models import Message
from .schemas import MessageCreate, MessageRead
from fastapi import HTTPException

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.post("/messages/", response_model=MessageRead)
def create_message(message: MessageCreate, db: Session = Depends(get_db)):
    db_message = Message(content=message.content)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

@app.get("/messages/", response_model=list[MessageRead])
def read_messages(db: Session = Depends(get_db)):
    return db.query(Message).all()

@app.delete("/messages/{message_id}", response_model=MessageRead)
def delete_message(message_id: int, db: Session = Depends(get_db)):
    message = db.query(Message).filter(Message.id == message_id).first()
    if not message:
        raise HTTPException(status_code=404, detail="Mensagem não encontrada")
    db.delete(message)
    db.commit()
    return message