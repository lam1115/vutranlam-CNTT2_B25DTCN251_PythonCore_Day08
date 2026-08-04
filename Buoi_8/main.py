from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session

from database import engine, Base, get_db
from models import BookModel
from schema import BookCreate, BookResponse

Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.post("/books", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    new_book = BookModel(
        code=book.code, title=book.title, price=book.price, pages=book.pages
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


@app.get("/books", response_model=list[BookResponse])
def get_books(db: Session = Depends(get_db)):
    books = db.query(BookModel).all()
    return books
