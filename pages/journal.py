from kivy.uix.screenmanager import Screen
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivy.lang.builder import Builder
from kivymd.uix.expansionpanel import MDExpansionPanelOneLine, MDExpansionPanel
from utils.theme import Theme
from kivymd.uix.label import MDLabel
from widgets.expansionpanel import ExpansionPage, ExpansionPanel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty

Builder.load_file("pages/journal.kv")

class Content(MDBoxLayout):
    text = StringProperty("None")
    pass

class Journal(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        self.init_profile_menu()
        self.add_pages()

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

    def profile_button_pressed(self):
        self.menu.open()
    
    def menu_btn_pressed(self, text):
        print(text)

    def add_pages(self):
        self.add_panel(
            "This is the subheading",
            "Lorem Ipsum is simply dummy text of the printing and typesetting\n\n industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
        )
        self.add_panel(
            "This is the subheading",
            "Lorem Ipsum is simply dummy text of the printing and typesetting\n\n industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\
            Lorem Ipsum is simply dummy text of the printing and typesetting\n\n industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
        )
        self.add_panel(
            "This is the subheading",
            "Lorem Ipsum is simply dummy text of the printing and typesetting\n\n industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
        )
        self.add_panel("This has shorter text", "This is all the text needed.")

    def add_panel(self, title, panel_text):
        self.ids.page_layout.add_widget(ExpansionPanel(title=title, text=panel_text))
            
