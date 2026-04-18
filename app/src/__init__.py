from fastapi import FastAPI
from .books.routers import book_router

app = FastAPI()
app.include_router(book_router, prefix="/api")
