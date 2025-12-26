from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import models
import schemas
import crud
from database import SessionLocal, engine

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Book Shop Management System")

# ✅ CORS configuration (FIXED)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # allow file:// frontend
    allow_credentials=False,  # MUST be False when using "*"
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/books", response_model=schemas.BookResponse)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)


@app.get("/books", response_model=list[schemas.BookResponse])
def read_books(db: Session = Depends(get_db)):
    return crud.get_all_books(db)


@app.get("/books/{book_id}", response_model=schemas.BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.put("/books/{book_id}", response_model=schemas.BookResponse)
def update_book(
    book_id: int,
    book: schemas.BookUpdate,
    db: Session = Depends(get_db),
):
    updated_book = crud.update_book(db, book_id, book)
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book


@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    deleted_book = crud.delete_book(db, book_id)
    if not deleted_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}
