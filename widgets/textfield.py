from kivymd.uix.textfield import MDTextField
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty, BooleanProperty

class TextField(MDTextField):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)