import sqlite3

class Database:
    initialised = False
    journal_titles = ["Place Holder Title"]

    def __init__(self, ) -> None:
        if not self.initialised:
            self.init_static_variables()
            self.initialised = True

    def init_static_variables():
        pass    
    
    '''
        Fetches note titles from database.
    '''
    @classmethod
    def get_journal_entry_titles(cls):
        return cls.journal_titles

    # def __init__():
    #     global connection
    #     connection = sqlite3.connect("user_data.db")
    
    # def add(user):
    #     connection.execute("INSERT INTO userTB (username, email, note)")

    # def close():
    #     connection.commit()
    #     connection.close()