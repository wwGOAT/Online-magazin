from connect_db import Database
from classes import Person
from project import main


def delete_person():
    delete = input("""
           1. ID delete
           2. Data delete
                   >>> """)

    if delete == "1":
        column_name = "person_id"
        id = input("ID: ")
        print(Person.delete_id("person", column_name, id))
        return person()
    elif delete == "2":
        column_name = "first_name"
        data = input("Data: ")
        print(Person.delete("person", column_name, data))
        return person()
    else:
        print("Error")
        return person()


def update_person():
    column_name = input("Column Name: ")
    old_data = input("Old data ")
    new_data = input("New data ")
    if column_name.lower() == 'person_id':
        print(Person.update_id("person", column_name, old_data, new_data))
        return person()
    elif column_name.lower() == 'first_name' or column_name.lower() == 'last_name'or column_name.lower() == 'username' or column_name.lower() == 'password':
        print(Person.update("person", column_name, old_data, new_data))
        return person()
    else:
        print("Error")
        return person()

def insert_person():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    username = input("Username: ")
    password = input("Password: ")
    query = f"INSERT INTO person (first_name, last_name, username, password) VALUES ('{first_name}', '{last_name}', '{username}', '{password}')"
    print(Database.connect(query, "insert"))
    return person()


def select_person():
    query = "SELECT * FROM person"
    data = Database.connect(query, "select")

    for i in data:
        print(f"""
        ID: {i[0]}
        First Name: {i[1]}
        Last Name: {i[2]}
        Username: {i[3]}
        password: {i[4]}""")
    return person()


def person():
    user = input("""
    1. Select
    2. Insert
    3. Update
    4. Delete
    0. Back
        >>>""")

    if user == '1':
        return select_person()

    elif user == '2':
        return insert_person()

    elif user == '3':
        return update_person()

    elif user == '4':
        return delete_person()

    elif user == "0":
        return main()

    else:
        print("Error")
        return person()