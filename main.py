from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}


products = [
    {"id": 1, "name": "laptop", "price": 50000},
    {"id": 2, "name": "phone", "price": 20000}
]

@app.get("/products")
def get_products():
    return {"products": products}


@app.post("/products")
def create_product():
    return {"message": "Product added successfully"}


@app.put("/products/1")
def update_product():
    return {"message": "Product updated successfully"}


@app.delete("/products/1")
def delete_product():
    return {"message": "Product deleted successfully"}


category=["electronics","fashion","home appliances"]
   

@app.get("/category")
def get_category():
    return {"category": category}