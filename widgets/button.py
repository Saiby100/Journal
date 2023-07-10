from kivymd.uix.button import MDFlatButton
from utils.theme import Theme
from kivymd.uix.behaviors import CircularRippleBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.lang.builder import Builder

Builder.load_file("widgets/button.kv")


class TextButton(MDFlatButton):
    pass

class ProfileButton(CircularRippleBehavior, ButtonBehavior, Image):
    pass