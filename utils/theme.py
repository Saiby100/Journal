from kivy.utils import get_color_from_hex

class Theme:
    home_bg = None
    bg = None
    text_colour = None

    def __init__(self, style=None) -> None:

        if style is not None:
            self.init_static_variables(style)
    
    @classmethod
    def init_static_variables(cls, style):
        path = f"resources/images/{style}/"
        cls.home_bg = path + "home.png"
        cls.bg = path + "background.png"
        cls.text_colour = "white"
    
    @classmethod
    def get_home_bg(cls):
        return cls.home_bg
    
    @classmethod
    def get_bg(cls):
        return cls.bg
    
    @classmethod
    def get_text_colour(cls):
        return cls.text_colour

