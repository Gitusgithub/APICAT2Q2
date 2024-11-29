import requests
import json

API_BASE_URL = "http://127.0.0.1:5000/products"

# Function to add a new product
def add_product(name, description, price):
    product_data = {
        'name': name,
        'description': description,
        'price': price
    }

    response = requests.post(API_BASE_URL, json=product_data)
    
    if response.status_code == 201:
        print(f"Product added successfully: {response.json()}")
    else:
        print(f"Failed to add product: {response.status_code}, {response.text}")

# Function to get all products
def get_products():
    response = requests.get(API_BASE_URL)
    
    if response.status_code == 200:
        products = response.json()
        print("Products:")
        for product in products:
            print(f"Name: {product['name']}, Description: {product['description']}, Price: {product['price']}")
    else:
        print(f"Failed to fetch products: {response.status_code}, {response.text}")

if __name__ == '__main__':
    # Example: Adding products
    add_product("Laptop", "A powerful laptop", 999.99)
    add_product("Smartphone", "Latest smartphone model", 499.99)

    # Example: Fetching all products
    get_products()