from pydantic import BaseModel

class DocumentCreate(BaseModel):
    content: str

class DocumentUpdate(BaseModel):
    content: str
    version: int

class DocumentResponse(BaseModel):
    id: int
    content: str
    version: int

    class Config:
        orm_mode = True