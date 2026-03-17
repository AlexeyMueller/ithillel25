
"""

select * from products

INSERT INTO products (Name, description, price)
VALUES ("Toyota", 'Blue', 55000);
INSERT INTO products (Name, description, price)
VALUES ("Volvo", 'White', 70000);
INSERT INTO products (Name, description, price)
VALUES ("BMW", 'Red', 44000);

select * from categories

INSERT INTO categories (Name, importance)
VALUES ("Car", 'Mid margin');
INSERT INTO categories (Name, importance)
VALUES ("Car", 'High margin');
INSERT INTO categories (Name, importance)
VALUES ("BMW", 'Low Margin');


SELECT p.name AS product_name, c.name AS category_name, c.importance, p.price
FROM products p
LEFT JOIN categories c ON p.id = c.id

"""
