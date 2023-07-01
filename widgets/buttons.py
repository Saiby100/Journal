from kivymd.uix.button import MDFlatButton
from utils.theme import Theme
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty
from kivymd.uix.behaviors import HoverBehavior, CircularRippleBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image

class TextButton(MDFlatButton):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.font_size = "18sp"
        self.theme_text_color = "Custom"
        self.text_color = Theme.get_text_colour()
        self.line_color = Theme.get_text_colour()
        self._radius = 15
        self.padding = [0, 12]


class ProfileButton(CircularRippleBehavior, ButtonBehavior, Image):
    pass