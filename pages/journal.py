from kivy.uix.screenmanager import Screen
from utils.database import Database as db
from utils.theme import Theme
from widgets.card import JournalEntryCard
from functools import partial
from widgets.label import CategoryLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.stacklayout import MDStackLayout
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivy.animation import Animation
from utils import config

class Journal(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        self.init_account_options()

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
        self.menu.open()
        print("display options menu") 
        print("options: logout, change theme, change profile image")
    
    def add_note(self):
        self.note_category_popup()
        print("Add new journal entry")
        print("go to notes page")
    
    def note_category_popup(self):
        #TODO: Add gifs
        items = []
            
        layout = MDStackLayout(
            size_hint_y=None,
            adaptive_height=True,
            spacing=10,
            padding=10)

        for title in self.fetch_journal_titles()["Sad"]:
            entry = JournalEntryCard(title=title, size=(150, 100))
            layout.add_widget(entry)
            items.append(entry)

        self.dialog_box = MDDialog(
            title=f"[color={Theme.params['text_colour']}]Choose Mood[/color]",
            type="custom",
            auto_dismiss=True,
            content_cls=layout,
            md_bg_color=Theme.get_accent_colour(),
            radius=[20, 20, 20, 20]
        )
        self.dialog_box.open()
    
    def init_account_options(self):
        menu_text = ["Profile", "Log Out", "Change Theme", "Mute"]

        menu_items = [
            {
                "text": text,
                "viewclass": "OneLineListItem",
                "height": dp(54),
                "on_release": lambda x=text: self.menu_btn_pressed(x)
            } for text in menu_text
        ]

        self.menu = MDDropdownMenu(
            caller=self.ids.profile_btn,
            items=menu_items,
            width_mult=2.5,
            size_hint_y=None
        )
    
    def menu_btn_pressed(self, button_text):
        if button_text == "Log Out":
            config.sm.current = "login_page"

        elif button_text == "Change Theme": 
            #TODO: Show all theme options
            pass
        
        elif button_text == "Mute":
            #TODO: Mute background music
            pass
        
        elif button_text == "Profile":
            #TODO: Update profile picture
            pass
        
        self.menu.dismiss()
        print(button_text)
    
    def hide_buttons(self):
        fade_anim = Animation(opacity=0, duration=.3)

        self.ids.profile_btn.disabled = True
        self.ids.add_btn.disabled = True

        fade_anim.start(self.ids.profile_btn)
        fade_anim.start(self.ids.add_btn)

    def unhide_buttons(self):
        fade_anim = Animation(opacity=1, duration=.3)

        self.ids.profile_btn.disabled = False
        self.ids.add_btn.disabled = False

        fade_anim.start(self.ids.profile_btn)
        fade_anim.start(self.ids.add_btn)

