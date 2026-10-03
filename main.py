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

category=["electronics","fashion","home appliances"]
   

@app.get("/category")
def get_category():
    return {"category": category}