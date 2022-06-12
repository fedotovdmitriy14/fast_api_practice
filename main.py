from typing import Union

from fastapi import FastAPI, Query, Path

from schemas import Item, Book

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")        # http://127.0.0.1:8000/items/1?q=somequery
def read_item(item_id: int = Path(..., gt=0, le=5), q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.post("/book")
def post_new_book(book: Book):
    return {"book": book}


@app.get("/book")
def get_book(q: str = Query(..., deprecated=True, min_length=3, description="Search book")):
    return q
