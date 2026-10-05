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


#1 dictionary
#2 list of string
#3 list of dictionary
#4 nested data

@app.get("/products/1")
def get_product_details():
    return {
        "id": 1,
        "name": "laptop",
        "price": 50000
    }

@app.get("/users/1")
def get_user_details():
    return {
        "id": 1,
        "name": "John Doe",
        "age": 25,
        "address": {
            "city": "New York",
            "zip": "10001"
        },
        "orders":[
            {"id":"order id 1",
                "product":"mobile"}
              ]
    }


category=["electronics","fashion","home appliances"]
   

@app.get("/category")
def get_category():
    return {"category": category}