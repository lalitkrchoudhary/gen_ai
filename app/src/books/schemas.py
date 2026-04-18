
from pydantic import BaseModel

class BookCreatModel(BaseModel):
    title: str
    author: str

class BookUpdateModel(BaseModel):
    title: str
    author: str