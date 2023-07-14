import mysql.connector
import json
from datetime import datetime

def create_database(cursor, name):
    query = f"CREATE DATABASE {name}"
    cursor.execute(query)

def add_table(cursor, table_name, **kwargs):
    query = f"CREATE TABLE {table_name}("

    for key in kwargs.keys():
        query += str(key) + " " + str(kwargs[key]) + ", "
    
    query = query[:len(query)-2] +")" #Remove comma, space, and add close parenthesis
    cursor.execute(query)

def show_params(cursor, table_name):
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

def find_rows(cursor, table_name, **kwargs):
    if len(kwargs) == 0:
        query = f"SELECT * FROM {table_name}" 
    else:
        key = list(kwargs.keys())[0]
        query = f"SELECT * FROM {table_name} WHERE {key} = {kwargs[key]}"

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

params = {}
with open("utils/info.json", "r") as file:
    params = json.load(file)
db = mysql.connector.connect(
    host="localhost",
    user=params["user"],
    passwd=params["password"],
    database="testdatabase"
)

cursor = db.cursor()
table_name = "Test"

find_rows(cursor, table_name, name="Salahuddin")
