import json
from kivy.utils import get_color_from_hex

class Theme:
    params = {}

    def __init__(self, style=None) -> None:

        if style is not None:
            self.init_static_variables(style)
    
    @classmethod
    def init_static_variables(cls, style):
        path = f"resources/themes/{style}/params.json"
        with open(path, "r") as file:
            cls.params = json.load(file)
    
    @classmethod
    def get_login_bg(cls):
        return cls.params["login_bg"]
    
    @classmethod
    def get_home_bg(cls):
        return cls.params["home_bg"]
    
    @classmethod
    def get_text_colour(cls):
        return get_color_from_hex(cls.params["text_colour"])

    @classmethod
    def get_focus_colour(cls):
        return get_color_from_hex(cls.params["focus_colour"])

    @classmethod
    def get_primary_colour(cls):
        return get_color_from_hex(cls.params["primary_colour"])

    @classmethod
    def get_accent_colour(cls):
        return get_color_from_hex(cls.params["accent_colour"])

