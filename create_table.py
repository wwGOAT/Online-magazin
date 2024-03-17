from connect_db import Database

def craete_table():
    address_table = """
        CREATE TABLE address(
            address_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            create_date TIMESTAMP DEFAULT now())"""

    store_table = """
        CREATE TABLE store(
            store_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            address_id INT REFERENCES address(address_id)) 
    """

    person_table = """
        CREATE TABLE person(
            person_id SERIAL PRIMARY KEY,
            first_name VARCHAR(20),
            last_name VARCHAR(20), 
            username VARCHAR(30),
            password VARCHAR,
            create_date TIMESTAMP DEFAULT now())"""

    product_table = """
        CREATE TABLE product(
            product_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            description VARCHAR(50),
            Price NUMERIC,
            create_date TIMESTAMP DEFAULT now())"""

    order_table = """
        CREATE TABLE order_table(
            order_id SERIAL PRIMARY KEY,
            person_id INT REFERENCES person(person_id),
            address_id INT REFERENCES address(address_id),
            create_date TIMESTAMP DEFAULT now())"""

    cart_table = """
       CREATE TABLE cart(
           cart_id SERIAL PRIMARY KEY,
           person_id INT REFERENCES person(person_id),
           product_id INT REFERENCES product(product_id),
           store_id INT REFERENCES store(store_id))"""

    inventory_table = """
        CREATE TABLE inventory(
            inventory_id SERIAL PRIMARY KEY,
            product_id INT REFERENCES product(product_id),
            store_id INT REFERENCES store(store_id),
            create_date TIMESTAMP DEFAULT now())"""

    order_items_table = """
        CREATE TABLE order_items(
            order_items_id SERIAL PRIMARY KEY,
            product_id INT REFERENCES product(product_id),
            person_id INT REFERENCES person(person_id),
            order_id INT REFERENCES order_table(order_id),
            price NUMERIC,
            create_date TIMESTAMP DEFAULT now())"""

    data = {
        "address_table": address_table,
        "store_table": store_table,
        "person_table": person_table,
        "product_table": product_table,
        "order_table": order_table,
        "cart_table": cart_table,
        "inventory_table": inventory_table,
        "order_items_table": order_items_table
    }

    for i in data:
        print(f"{i} {Database.connect(data[i], "create")}")

if __name__ == "__main__":
    craete_table()