from datetime import date
from typing import Union, List

from pydantic import BaseModel, validator, Field


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

    # class Config:
    #     orm_mode = True


class Author(BaseModel):
    first_name: str = Field(..., max_length=20, description='name length should not exceed 20 characters')
    last_name: str
    age: int

    @validator('age')
    def check_age(cls, age):
        if age < 15:
            raise ValueError('Age shoud be greater than 15')
        return age


class Book(BaseModel):
    name: str
    published: date
    author: List[Author]
    pages: int = None
