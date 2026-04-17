from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List


books_data = [
    {"id": 1, "title": "The Alchemist", "author": "Paulo Coelho"},
    {"id": 2, "title": "1984", "author": "George Orwell"},
    {"id": 3, "title": "Clean Code", "author": "Robert C. Martin"},
    {"id": 4, "title": "Atomic Habits", "author": "James Clear"}
]

class BookCreatModel(BaseModel):
    title: str
    author: str


app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    return {"success": "ok"}

@app.get("/get_books",response_model=List[BookCreatModel])
async def books():
    return books_data


@app.post("/book")
async def create_book(data: BookCreatModel):
    # books_data.append(data)
    # return {"message": "Book added"}
    books_data.append(data)
    return books_data

@app.get("/book/{book_id}")
async def get_book_id(book_id:int)->dict :
    for book in books_data:
        if book["id"]==book_id:
             return book
        
    raise HTTPException(status_code=404, detail="Book not found")


