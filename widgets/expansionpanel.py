from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang.builder import Builder
from kivy.properties import StringProperty, BooleanProperty, NumericProperty, ObjectProperty
from kivy.animation import Animation
from kivymd.uix.card import MDCard
from kivymd.uix.list import IconRightWidget

Builder.load_file("widgets/expansionpanel.kv")

class PanelContent(MDBoxLayout):
    text = StringProperty("")

    def fade_in_text(self):
        self._fade(1, self.ids.label)

    def fade_out_text(self):
        self._fade(0, self.ids.label)

    def _fade(self, new_opacity, widget):
        Animation(opacity=new_opacity, duration=.2).start(widget)

class ExpansionPanelTitle(MDExpansionPanelOneLine):
    pass


class ExpansionPage(MDExpansionPanel):
    title = StringProperty("")
    text = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(
            content=PanelContent(text=kwargs["text"]),
            panel_cls=ExpansionPanelTitle(text="  "+kwargs["title"]),
            **kwargs
        )

    def on_open(self, *args):
        # self.content.fade_in_text()
        self.panel_cls.radius = [10, 10, 0, 0]
    
    def on_close(self, *args):
        # self.content.fade_out_text()
        self.panel_cls.radius = 10

    
class RotateIcon(IconRightWidget):
    pass

class ExpansionPanel(MDCard):
    title = StringProperty("")
    text = StringProperty("")
    expanded = BooleanProperty(False)
    initial_height = NumericProperty(70)
    content = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.content = PanelContent(self.text)

    def expand(self):
        self._set_arrow_expanded()

        if self.content is not None:
            self._set_card_expanded()

        self.expanded = True
    
    def collapse(self):
        self._set_arrow_collapsed()

        if self.content is not None:
            self._set_card_collapsed()

        self.expanded = False

    def _set_arrow_expanded(self):
        Animation(angle=-90, duration=.2).start(self.ids.arrow)

    def _set_arrow_collapsed(self):
        Animation(angle=0, duration=.2).start(self.ids.arrow)
    
    def _set_card_expanded(self):
        self.add_widget(self.content)
        self.ids.title.size_hint_y = .15
        Animation(height=self.height+self.content.height, duration=.3).start(self)
    
    def _set_card_collapsed(self):
        shrink_anim = Animation(height=self.initial_height, duration=.3)
        shrink_anim.bind(on_complete=lambda *x: self.remove_widget(self.content))

        def shrink_title():
            self.ids.title.size_hint_y = 1        

        shrink_anim.bind(on_complete=lambda *x: shrink_title())

        shrink_anim.start(self)

