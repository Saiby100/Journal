import mysql.connector
import json
from datetime import datetime

def fetch_params(path):
    '''

    '''
    with open(path, "r") as file:
        return json.load(file)

def create_database(cursor, name):
    query = f"CREATE DATABASE {name}"
    cursor.execute(query)

def add_table(cursor, table_name, **kwargs):
    query = f"CREATE TABLE {table_name}("

    for key in kwargs.keys():
        query += str(key) + " " + str(kwargs[key]) + ", "
    
    query = query[:len(query)-2] +")" #Remove comma, space, and add close parenthesis
    cursor.execute(query)

def describe_table(cursor, table_name):
    query = f"DESCRIBE {table_name}"
    cursor.execute(query)

    for param in cursor:
        print(param)

def add_entry(db, cursor, table_name, **kwargs):
    query = f"INSERT INTO {table_name} ("

    for key in kwargs.keys():
        query += key + ", "
    
    query = query[:len(query)-2] + ")" #remove comma and space and add close parenthesis
    query += " VALUES ("

    for i in range(len(kwargs.keys())):
        query += "%s, "
    
    query = query[:len(query)-2] + ")" #remove comma and space and add close parenthesis

    cursor.execute(query, tuple(kwargs.values()))
    db.commit()

def find_rows(cursor, table_name, *args, **kwargs):
    '''
        args = attributes to show.
        kwargs = conditions.
    '''

    if len(args) > 0:
        attr = ""
        for arg in args:
            attr  += (arg + ", ")
        
        attr = attr[:len(attr)-2]
    else:
        attr = "*"

    if len(kwargs) == 0:
        query = f"SELECT {attr} FROM {table_name}" 

    else:
        key = list(kwargs.keys())[0]
        query = f"SELECT {attr} FROM {table_name} WHERE {key} = {kwargs[key]}"

    cursor.execute(query)
    for row in cursor:
        print(row)

def delete_table(cursor, table_name):
    query = f"DROP TABLE {table_name}"

    cursor.execute(query)

def print_all_tables(cursor):
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()

    for table in tables:
        print(table[0])

def add_column(cursor, table_name, col_name, dtype):
    query = f"ALTER TABLE {table_name} ADD COLUMN {col_name} {dtype}"
    cursor.execute(query)

def delete_column(cursor, table_name, col_name):
    cursor.execute(f"ALTER TABLE {table_name} DROP {col_name}")

def change_column(cursor, table_name, old_col_name, col_name, col_type):
    query = f"ALTER TABLE {table_name} CHANGE {old_col_name} {col_name} {col_type}"
    cursor.execute(query)

def show_databases(cursor):
    cursor.execute("SHOW DATABASES")

    for database in cursor:
        print(database)

class Database:
    def __init__(self) -> None:
        with open("resources/info.json", "r") as file:
            params = json.load(file)

        self.db = mysql.connector.connect(
            host=params["host"],
            user=params["user"],
            passwd=params["password"],
            database="journalapp"
        )

        self.cursor = self.db.cursor()
    
    def add_user(self, username, password):
        if (self._user_exists(username)):
            return False

        query = f"INSERT INTO Users (name, passwd) VALUES (%s,%s)"
        self.cursor.execute(query, (username, password))
        self.db.commit()

        return True
    
    def add_note(self, username, tag, text):
        query = f"INSERT INTO Notes (username, tag, text) VALUES (%s,%s,%s)"

        self.cursor.execute(query, (username, tag, text))
        self.db.commit()
    
    def get_notes(self, username, tag=None):
        if tag is None:
            return self._find_rows("Notes", username=username)
        else:
            return self._find_rows("Notes", username=username, tag=tag)

    def _user_exists(self, username):
        uname = f"'{username}'"
        row = self._find_rows("Users", name=uname)

        return row.fetchone() is not None

    def _find_rows(self, table_name, *args, **kwargs):
        if len(args) > 0:
            attrs = ""

            for arg in args:
                attrs  += (arg + ", ")
            
            attrs = attrs[:len(attrs)-2]
        else:
            attrs = "*"
        
        if len(kwargs) == 0:
            query = f"SELECT {attrs} FROM {table_name}" 

        else: 
            key = list(kwargs.keys())[0]
            query = f"SELECT {attrs} FROM {table_name} WHERE "
            for key in kwargs.keys():
                query += (key + f" = {kwargs[key]} AND ")
            
            query = query[:len(query)-5]
        
        self.cursor.execute(query)
        return self.cursor
    
    def _describe_table(self, table_name):
        query = f"DESCRIBE {table_name}"
        self.cursor.execute(query)

        for param in self.cursor:
            print(param)
    
    def _delete_table(self, table_name):
        query = f"DROP TABLE {table_name}"
        self.cursor.execute(query)
    
    def _delete_column(self, table_name, col_name):
        self.cursor.execute(f"ALTER TABLE {table_name} DROP {col_name}")
    
    def _add_table(self, table_name, **kwargs):
        query = f"CREATE TABLE {table_name}("

        for key in kwargs.keys():
            query += str(key) + " " + str(kwargs[key]) + ", "
        
        query = query[:len(query)-2] +")" #Remove comma, space, and add close parenthesis
        self.cursor.execute(query)

    def _add_column(self, table_name, col_name, dtype):
        query = f"ALTER TABLE {table_name} ADD COLUMN {col_name} {dtype}"
        self.cursor.execute(query)
    
    def _print_table(self, table_name):
        '''
            Prints all entries from specified table
        '''
        for row in self._find_rows(table_name):
            print(row)
    
    def _clear_table(self, table_name):
        '''
            Clears all entries from the specified table.
        '''
        self.cursor.execute(f"DELETE FROM {table_name}")
        self.db.commit()

if __name__ == "__main__":
    db = Database()
