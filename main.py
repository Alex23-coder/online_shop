from flask import Flask, jsonify, request, render_template
import sqlite3
import os
import secrets
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')

DATABASE = 'shop.db'

@app.route('/')
def index():
    print("Request to index() route received!")  # Добавлено логирование
    return render_template('index.html')

# -------------------  Database Functions -------------------

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Return rows as dictionaries
    return conn

def init_db():
    conn = get_db_connection()
    with open('schema.sql', mode='r') as f:
        conn.cursor().executescript(f.read())
    conn.commit()
    conn.close()

# -------------------  API Endpoints -------------------

@app.route('/products', methods=['GET'])
def get_products():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
    return jsonify([dict(row) for row in products]) #convert Row objects to dictionaries

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE id = ?', (product_id,)).fetchone()
    conn.close()
    if product:
        return jsonify(dict(product))
    return jsonify({'message': 'Product not found'}), 404


@app.route('/search', methods=['GET'])
def search_products():
    query = request.args.get('q')
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products WHERE name LIKE ? OR description LIKE ?', ('%' + query + '%', '%' + query + '%')).fetchall()
    conn.close()
    return jsonify([dict(row) for row in products])

@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)  # Default to 1 if quantity is not provided

    # Basic validation
    if not product_id or not isinstance(product_id, int) or quantity <= 0:
        return jsonify({'message': 'Invalid request'}), 400

    # In a real application, you'd manage cart state (e.g., in a session or database)
    # For simplicity, this example just returns a success message
    return jsonify({'message': 'Product added to cart'}), 201


@app.route('/orders/create', methods=['POST'])
def create_order():
    data = request.get_json()
    # Assuming data contains user info and cart items
    user_id = data.get('user_id')
    cart_items = data.get('cart_items')

    # TODO:  Validate data, process payment, update inventory, etc.

    return jsonify({'message': 'Order created successfully'}), 201

# Не запускаем приложение напрямую через app.run, когда используем Gunicorn
# if __name__ == '__main__':
#     #init_db()  # uncomment to init the database on first run.
#     app.run(debug=True, host='0.0.0.0', port=8000)
