from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


books_data = [
    {"title": "The Alchemist", "author": "Paulo Coelho"},
    {"title": "1984", "author": "George Orwell"},
    {"title": "Clean Code", "author": "Robert C. Martin"},
    {"title": "Atomic Habits", "author": "James Clear"}
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

