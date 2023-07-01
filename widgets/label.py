from kivymd.uix.label import MDLabel

class CategoryLabel(MDLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.size_hint = (1, None)
        self.color = "white"
        self.height = 60
        self.font_size = 24
        self.bold = True