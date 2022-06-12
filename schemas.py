from datetime import date
from typing import Union, List

from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

    # class Config:
    #     orm_mode = True


class Author(BaseModel):
    first_name: str
    last_name: str


class Book(BaseModel):
    name: str
    published: date
    author: List[Author]
    pages: int = None
