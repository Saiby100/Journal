from kivy.uix.screenmanager import Screen
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
from widgets.gif import Gif
import os
from kivy.lang.builder import Builder

Builder.load_file("pages/home.kv")

class Home(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        self.init_profile_menu()
        self.dialog_box = None

        entry_titles = self.fetch_journal_titles()
        keys = entry_titles.keys()

        for key in keys: 
            self.ids.notes_layout.add_widget(CategoryLabel(text=key))

            for entry_title in entry_titles[key]:
                entry = JournalEntryCard(
                    title=entry_title,
                    size_hint=(None, None),
                    size=(180, 110),
                    radius=25
                    )
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
    
    def add_note(self):
        self.note_category_popup()
        #TODO
        # config.sm.current = "journal_page"
    
    def note_category_popup(self):
        if self.dialog_box is None:
            layout = MDStackLayout(
                size_hint_y=None,
                adaptive_height=True,
                spacing=10,
                padding=10)

            gifs_path = "resources/gifs/"
            gifs_arr = os.listdir(gifs_path)
            
            for gif in gifs_arr:
                entry = Gif(source=gifs_path+gif)
                layout.add_widget(entry)

            self.dialog_box = MDDialog(
                title=f"[color={Theme.params['text_colour']}]Choose Mood[/color]",
                type="custom",
                auto_dismiss=True,
                content_cls=layout,
                md_bg_color=Theme.get_accent_colour(),
                radius=[20, 20, 20, 20],
                size_hint_x=1
            )
        self.dialog_box.open()
    
    def init_profile_menu(self):
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

