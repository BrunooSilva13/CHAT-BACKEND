from pydantic import BaseModel

class MessageCreate(BaseModel):
    content: str

class MessageRead(BaseModel):
    id: int
    content: str

    class Config:
        orm_mode = True

class MessageUpdate(BaseModel):
    content: str