from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Mouse", "price": 29.99},
    {"id": 3, "name": "Keyboard", "price": 79.99}
]

@app.route('/')
def home():
    return jsonify({"message": "Welcome to TechShop API", "status": "running"})

@app.route('/products')
def get_products():
    return jsonify({"products": products})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
