import sqlite3

class Database:

    def __init__():
        global connection
        connection = sqlite3.connect("user_data.db")
    
    def add(user):
        connection.execute("INSERT INTO userTB (username, email, note)")

    def close():
        connection.commit()
        connection.close()