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


class OrderItem(BaseModel):
    product_id: int
    quantity: int
class Order(BaseModel):
    customer_name: str
    items: list[OrderItem]

@app.post("/orders")
def create_order(order: Order):
    return {
        "message": "Order created successfully",
        "order": order
    }


@app.put("/products/{product_id}")
def update_product(product_id: int, product: dict = Body(...), notify: bool = False):

    return {
        "product_id": product_id,
        "product": product,
        "notify": notify
    }






























