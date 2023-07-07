from kivy.uix.screenmanager import Screen
from kivymd.uix.textfield import MDTextFieldRect

class TestPage(Screen):
    def __init__(self, **kw):
        super().__init__(name="test_page", **kw)
        field = MDTextFieldRect()