from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard
from utils.database import Database as db

class Journal(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        # for entry in db.get_journal_entries:
        #     pass

    


