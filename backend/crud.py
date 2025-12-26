from sqlalchemy.orm import Session
import models
import schemas


def create_book(db: Session, book: schemas.BookCreate):
    new_book = models.Book(
        name=book.name,
        author=book.author,
        pages=book.pages,
        price=book.price,
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


def get_all_books(db: Session):
    # ✅ Always return books ordered by ID
    return db.query(models.Book).order_by(models.Book.id.asc()).all()


def get_book_by_id(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def update_book(db: Session, book_id: int, book: schemas.BookUpdate):
    db_book = get_book_by_id(db, book_id)
    if not db_book:
        return None

    db_book.name = book.name
    db_book.author = book.author
    db_book.pages = book.pages
    db_book.price = book.price

    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int):
    db_book = get_book_by_id(db, book_id)
    if not db_book:
        return None

    db.delete(db_book)
    db.commit()
    return db_book
