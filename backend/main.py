from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from models import Base, Document
from schemas import DocumentCreate, DocumentUpdate

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Middleware requirement from assignment
@app.middleware("http")
async def add_student_id_header(request, call_next):
    response = await call_next(request)
    response.headers["X-Student-ID"] = "BSCS23150"
    return response

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create document
@app.post("/documents")
def create_document(doc: DocumentCreate, db: Session = Depends(get_db)):
    new_doc = Document(
        content=doc.content,
        version=1
    )

    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)

    return new_doc

# Get document
@app.get("/documents/{doc_id}")
def get_document(doc_id: int, db: Session = Depends(get_db)):
    doc = db.query(Document).filter(Document.id == doc_id).first()

    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")

    return doc

# Naive update (for demonstrating failure first)
@app.put("/documents/{doc_id}")
def update_document(
    doc_id: int,
    update: DocumentUpdate,
    db: Session = Depends(get_db)
):
    doc = db.query(Document).filter(Document.id == doc_id).first()

    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")

    doc.content = update.content
    doc.version += 1

    db.commit()
    db.refresh(doc)

    return doc