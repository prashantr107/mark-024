from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class Category(BaseModel):
    id: int
    name: str

class Product(BaseModel):
    name: str   
    price: float
    category: Category
 


@app.post("/products")
def create_product(product: Product):
    return {
        "message": "Product received",
        "product": product
    }






@app.put("/products/{product_id}")
def update_product(product_id: int, product: dict = Body(...), notify: bool = False):

    return {
        "product_id": product_id,
        "product": product,
        "notify": notify
    }






























