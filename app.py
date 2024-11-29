from flask import Flask, request, jsonify
from flask_api import status

app = Flask(__name__)

# In-memory product storage (this could be replaced with a database)
products = []

# Product model for validation
def validate_product(data):
    if not isinstance(data.get('name'), str) or not isinstance(data.get('description'), str) or not isinstance(data.get('price'), (int, float)):
        return False
    return True

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()

    if not data or not validate_product(data):
        return jsonify({"error": "Invalid data"}), status.HTTP_400_BAD_REQUEST

    # Create a new product and add to the list
    new_product = {
        'name': data['name'],
        'description': data['description'],
        'price': data['price']
    }
    products.append(new_product)
    
    return jsonify(new_product), status.HTTP_201_CREATED

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), status.HTTP_200_OK

if __name__ == '__main__':
    app.run(debug=True)
