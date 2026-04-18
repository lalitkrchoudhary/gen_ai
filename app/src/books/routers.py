from fastapi import APIRouter
from fastapi import HTTPException
from typing import List
from .book_data import books_data
from .schemas import BookCreatModel, BookUpdateModel

book_router = APIRouter()



@book_router.get("/")
async def root() -> dict[str, str]:
    return {"success": "ok"}

@book_router.get("/get_books",response_model=List[BookCreatModel])
async def books():
    return books_data


@book_router.post("/book")
async def create_book(data: BookCreatModel):
    # books_data.append(data)
    # return {"message": "Book added"}
    books_data.append(data)
    return books_data

@book_router.get("/book/{book_id}")
async def get_book_id(book_id:int)->dict :
    for book in books_data:
        if book["id"]==book_id:
             return book
        
    raise HTTPException(status_code=404, detail="Book not found")



@book_router.patch("/book/{id}")
async def update_book(id:int,b:BookUpdateModel):
    for d in books_data:
        if d["id"]==id:
            d["title"]=b.title
            d["author"]=b.author
            return d
    raise HTTPException(status_code=404, detail="Book not update")

@book_router.delete("/book/{id}")
async def delete_book(id:int):
    for d in books_data:
        if d["id"]==id:
            books_data.remove(d)
            return {"success":"true"}
    return HTTPException(status_code=204, detail="Content delted")


