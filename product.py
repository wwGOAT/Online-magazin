from connect_db import Database
import project
from classes import Product


def select_product():
    query = "SELECT * FROM product"
    data = Database.connect(query, "select")

    for i in data:
        print(f"""
        ID: {i[0]}
        Name : {i[1]}
        description: {i[2]}
        Price: {i[3]}""")

    return product()

def insert_product():
    name = input("Enter product name: ")
    description = input("Enter product description: ")
    price = input("Enter product price: ")
    query = f"INSERT INTO product(name, description, price) VALUES('{name}', '{description}', '{price}')"
    print(Database.connect(query, "insert"))
    return product()


def delete_product():
    update = input("""
    1. ID delete
    2. Data delete
            >>> """)

    if update == "1":
        column_name = "product_id" or "price"
        id = input("ID: ")
        print(Product.delete_id("product", column_name, id))
        return product()
    elif update == "2":
        column_name = "name" or "description"
        data = input("Data: ")
        print(Product.delete("product", column_name, data))
        return product()
    else:
        return product()


def update_product():
    column_name = input("Column Name: ")
    old_data = input("Old data ")
    new_data = input("New data ")
    if column_name.lower() == 'product_id' or "price":
        print(Product.update_id("product", column_name, old_data, new_data))
        return product()
    elif column_name.lower() == 'name' or column_name.lower() == 'description':
        print(Product.update("product", column_name, old_data, new_data))
        return product()
    else:
        print("Error")
        return product()

def product():
    service = input("""
    1. Select
    2. Insert
    3. Update
    4. Delete
    0. Back
        >>>""")

    if service == "1":
        return select_product()

    elif service == "2":
        return insert_product()

    elif service == "3":
        return update_product()

    elif service == "4":
        return delete_product()

    elif service == "0":
        return project.main()

    else:
        print("Error")
        return product()