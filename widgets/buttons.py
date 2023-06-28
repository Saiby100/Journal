from kivymd.uix.button import MDFlatButton
from kivy.utils import get_color_from_hex
from utils.theme import Theme

class TextButton(MDFlatButton):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.font_size = "18sp"
        self.theme_text_color = "Custom"
        self.text_color = Theme.get_text_colour()
        self.line_color = Theme.get_text_colour()
        self._radius = 15
        self.padding = [0, 12]
    
    def login(self):
        pass

    def signup(self):
        pass