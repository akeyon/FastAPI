from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Msg(BaseModel):
    msg: str

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    
@app.post("/items/")
async def create_item(item: Item):
    return item
    
@app.get("/")
async def root():
    return {"greeting": "Hello, World edited!", "message": "Welcome to FastAPI!"}

@app.get("/path")
async def demo_get():
    return {"message": "This is /path endpoint, use a post request to transform the text to uppercase"}


    


