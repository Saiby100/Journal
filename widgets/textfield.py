from kivy.lang.builder import Builder
from kivy.metrics import dp
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import CommonElevationBehavior
from kivy.utils import get_color_from_hex
from kivy.properties import (
    StringProperty,
    BooleanProperty,
    NumericProperty,
    VariableListProperty,
    ColorProperty,
)
from kivy.core.text import DEFAULT_FONT

Builder.load_file("widgets/textfield.kv")

class TextField(MDBoxLayout, CommonElevationBehavior, ThemableBehavior):

    #Card (Background) parameters
    elevation = NumericProperty(0)
    radius = VariableListProperty([10], length=4)
    card_ripples = BooleanProperty(False)
    card_padding = dp(5)
    card_spacing = NumericProperty(0)
    focus = BooleanProperty(False)
    background_color = ColorProperty([1, 1, 1, 1])

    #TextInput parameters
    text = StringProperty("")
    hint_text = StringProperty("")
    hint_text_color = ColorProperty([0.5, 0.5, 0.5, 1.0])
    multiline = BooleanProperty(True)
    background_disabled_normal = StringProperty("")
    text_field_background_normal = StringProperty("")
    text_field_background_active = StringProperty("")
    line_spacing = NumericProperty(0)
    font_family = StringProperty(None, allownone=True)
    font_name = StringProperty(DEFAULT_FONT)
    font_size = NumericProperty('15sp')
    password = BooleanProperty(False)
    cursor_color = ColorProperty(get_color_from_hex("#F89E9E"))

    handle_image_middle = StringProperty(
        'atlas://data/images/defaulttheme/selector_middle')
    handle_image_left = StringProperty(
        'atlas://data/images/defaulttheme/selector_left')
    handle_image_right = StringProperty(
        'atlas://data/images/defaulttheme/selector_right')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #Register TextInput events
        self.register_event_type("on_text")
        self.register_event_type("on_triple_tap")
        self.register_event_type("on_double_tap")
        self.register_event_type("on_cursor_blink")
        self.register_event_type("on_cursor")
        self.register_event_type("on_size")
        self.register_event_type("on_handle_image_middle")
        self.register_event_type("on_handle_image_left")
        self.register_event_type("on_handle_image_right")
        self.register_event_type("on_text_validate")
        self.register_event_type("on_focus")
        self.register_event_type("on_quad_touch")
        self.register_event_type("on_release")

    def on_text(self, *args):
        """[summary]
        simulates the on_text event in kivy default
        TextInput
        """

    def on_triple_tap(self):
        """[summary]
        simulates on_triple_tap event in kivy default
        TextInput
        """

    def on_double_tap(self):
        """[summary]
        simulates on_double_tap event in kivy default
        TextInput
        """

    def on_cursor_blink(self):
        """[summary]
        simulates on_cursor_blink event in kivy default
        TextInput
        """

    def on_cursor(self):
        """[summary]
        simulates on_cursor event in kivy default
        TextInput
        """
    def on_size(self, *args):
        """[summary]
        simulates on_size event in kivy default
        TextInput
        """

    def on_handle_image_middle(self):
        """[summary]
        simulates on_handle_image_middle event in kivy default
        TextInput
        """

    def on_handle_image_left(self):
        """[summary]
        simulates on_handle_image_left event in kivy default
        TextInput
        """

    def on_handle_image_right(self):
        """[summary]
        simulates on_handle_image_right event in kivy default
        TextInput
        """

    def on_text_validate(self):
        """[summary]
        simulates on_text_validate event in kivy default
        TextInput
        """

    def on_focus(self, *args):
        """[summary]
        simulates on_focus event in kivy default
        TextInput
        """
        self.focus = args[1]
        """if platform == "android":
            from kvdroid import activity
            from android.runnable import run_on_ui_thread

            @run_on_ui_thread
            def fix_back_button():
                activity.onWindowFocusChanged(False)
                activity.onWindowFocusChanged(True)

            if not args[1]:
                fix_back_button()"""

    def on_quad_touch(self):
        """[summary]
        simulates on_quad_touch event in kivy default
        TextInput
        """

    def on_release(self):
        """
        simulates MDCard on_release event
        """

    def clear_text(self):
        self.ids.textfield.text = ""

if __name__ == "__main__":
    from kivymd.app import MDApp
    from kivy.uix.scrollview import ScrollView
    Builder.load_file("./textfield.kv")


    class Opera(MDApp):
        use_kivy_settings = False

        # kv_file = "main.kv"

        def build(self):
            root = MDBoxLayout(orientation='vertical', padding=dp(
                20), md_bg_color=[0, 0, 0, .15], spacing=dp(20))
            scroll = ScrollView()

            field5 = TextField(hint_text="This is a modified textfield")
            root.add_widget(field5)
            root.add_widget(scroll)
            return root
    
    Opera().run()