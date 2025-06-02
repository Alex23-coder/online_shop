DROP TABLE IF EXISTS products;

CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    image_url TEXT
);

INSERT INTO products (name, description, price, image_url) VALUES
('Smartphone X', 'High-end smartphone with 5G.', 799.99, 'smartphone_x.jpg'),
('Laptop Pro', 'Powerful laptop for professionals.', 1299.00, 'laptop_pro.jpg'),
('Wireless Headphones', 'Noise-cancelling wireless headphones.', 149.99, 'headphones.jpg');