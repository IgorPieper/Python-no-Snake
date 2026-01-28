from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

fake_db = []

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

@app.get("/")
async def read_root():
    return {"message": "Hello World!"}

@app.post("/items")
async def create_item(item: Item):
    fake_db.append(item)
    return {"message": "Item added successfully", "item": item}

@app.get("/items")
async def read_items():
    return {"items": fake_db}
