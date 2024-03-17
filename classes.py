from connect_db import Database

class Eldor:
    @staticmethod
    def select(table):
        query = f"SELECT * FROM {table}"
        return Database.connect(query, "select")

    @staticmethod
    def delete_id(table, column_name, id):
        query = f"DELETE FROM {table} WHERE {column_name} = {id}"
        return Database.connect(query, "delete")

    @staticmethod
    def update_id(table, column_name, old_data, new_data):
        query = f"UPDATE {table} SET {column_name} = {new_data} WHERE {column_name} = {old_data}"
        return Database.connect(query, "update")

    @staticmethod
    def update(table, column_name, old_data, new_data):
        query = f"UPDATE {table} SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"
        return Database.connect(query, "update")

    @staticmethod
    def delete(table, column_name, data):
        query = f"DELETE FROM {table} WHERE {column_name} = {data}"
        return Database.connect(query, "delete")


class Person(Eldor):
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password


class Product(Eldor):
    def __init__(self, name, description):
        self.name = name
        self.description = description

