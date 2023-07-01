from kivy.uix.screenmanager import Screen
from utils.database import Database as db
from widgets.card import JournalEntryCard
from functools import partial
from widgets.label import CategoryLabel

class Journal(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        entry_titles = self.fetch_journal_titles()
        keys = entry_titles.keys()

        for key in keys: 
            self.ids.notes_layout.add_widget(CategoryLabel(text=key))

            for entry_title in entry_titles[key]:
                entry = JournalEntryCard(title=entry_title)
                entry.bind(on_release=partial(self.open_journal_entry, entry))

                self.ids.notes_layout.add_widget(entry)

    def open_journal_entry(self, *args):
        print(args[0].title)

    def fetch_journal_titles(self):
        # db.get_journal_entry_titles()
        titles = [
            "This is the first journal entry",
            "This is the second journal entry",
            "This is the third journal entry",
            "This is the third one",
            "And Finally, this is the fourth one"
        ]

        entry_titles = {
            "Embarrassing": titles,
            "Sad": titles,
            "Anoyying": titles,
            "Exciting": titles,
            "Love": titles,
            "Comforting": titles}
        
        return entry_titles
    
    def profile_button_pressed(self):
        print("display options menu") 
        print("options: logout, change theme, change profile image")
    
    def add_note(self):
        print("Add new journal entry")
        print("go to notes page")

    


