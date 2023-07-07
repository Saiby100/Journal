"""
M_CardTextField
"""
__all__ = ("M_CardTextField",)

import sys

# import emoji
from kivy.core.text.markup import MarkupLabel
from kivy.graphics.texture import Texture
from kivy.uix.textinput import TextInput, Cache_append, Cache_get
from kivy import platform, Logger
from kivy.factory import Factory
# from emoji import emojize
from kivy.lang.builder import Builder
from kivy.metrics import dp
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.widget import Widget, WidgetException
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.behaviors import CommonElevationBehavior

from kivy.properties import (
    StringProperty,
    BooleanProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    VariableListProperty,
    ColorProperty,
    DictProperty
)
from kivy.core.text import DEFAULT_FONT
from kivy.config import Config
from kivy.event import EventDispatcher

_is_desktop = False
if Config:
    _is_desktop = Config.getboolean('kivy', 'desktop')

Builder.load_string(
    """
# kv_start
<TextField>:
    adaptive_height: True
    md_bg_color: 1, 1, 1, 1

    MDCard:
        ripple_behavior: True
        radius: [dp(10)]
        padding: root.card_padding
        size_hint_y: None
        height: self.minimum_height
        elevation: 0
        pos_hint_y: {"center_y": .5}

        on_release: 
            root.dispatch("on_release")
        
        TextInput:
            focus: root.focus
            hint_text: root.hint_text
            multiline: root.multiline
            line_spacing: root.line_spacing
            font_family: root.font_family
            font_size: root.font_size
            font_name: root.font_name
            password: root.password
            height: 


<M_CardTextField>:
    adaptive_height: True
    md_bg_color: 1, 1, 1, 1
    padding: dp(2), dp(2), dp(10), dp(2)
    MDCard:
        id: card
        ripple_behavior: root.card_ripples
        radius: [dp(10)]
        padding: root.card_padding
        size_hint_y: None 
        height: self.minimum_height
        elevation: 0
        pos_hint: {"center_y": .5}
        on_release:
            root.dispatch("on_release")
        EmojiTextInput:
            id: textfield
            grow: True
            text: root.text 
            initial_height: 0
            focus: root.focus #on_focus of parent widget
            hint_text: root.hint_text 
            input_type: root.input_type #Type of data to accept (email, date, etc)
            multiline: root.multiline
            background_normal: root.text_field_background_normal
            background_active: root.text_field_background_active
            background_disabled_normal: root.background_disabled_normal
            cursor_color: root.cursor_color
            foreground_color: root.foreground_color
            disabled_foreground_color: root.disabled_foreground_color
            disabled: root.text_field_disabled
            input_filter: root.input_filter  #Type of values to accept (int, string)
            line_spacing: root.line_spacing #Spaces between lines
            allow_copy: root.allow_copy #Allow copying of text
            replace_crlf: root.replace_crlf
            auto_indent: root.auto_indent #Automatically indent multiline text
            # handle_image_middle: root.handle_image_middle
            # handle_image_left: root.handle_image_left
            # handle_image_right: root.handle_image_right
            write_tab: root.write_tab #Whether or not tab should move focus to next widget
            base_direction: root.base_direction  #Impacts horizontal alignment when "auto"
            font_family: root.font_family
            font_context: root.font_context
            font_size: root.font_size
            font_name: root.font_name
            selection_text: root.selection_text
            readonly: root.readonly #User can/cannot change text
            text_validate_unfocus: root.text_validate_unfocus
            password: root.password
            password_mask: root.password_mask
            keyboard_suggestions: root.keyboard_suggestions
            cursor_blink: root.cursor_blink
            cursor_width: root.cursor_width
            line_height: root.line_height
            tab_width: root.tab_width
            text_field_padding: root.text_field_padding
            halign: root.halign
            scroll_x: root.scroll_x
            scroll_y: root.scroll_y
            selection_color: root.selection_color
            background_color: root.background_color
            hint_text_color: root.hint_text_color
            border: root.border
            use_bubble: root.use_bubble
            use_handles: root.use_handles
            suggestion_text: root.suggestion_text
            size_hint_y: None if root.grow_card else root.text_field_size_hint_y
            height: 
                (self.minimum_height if self.height < root.text_field_max_height else root.text_field_max_height)\
                if root.grow_card else\
                (root.text_field_height if root.text_field_height and (not root.text_field_size_hint_y)\
                else self.minimum_height)
                
            on_text:
                self.initial_height = self.height if self.grow else self.initial_height
                self.grow = False
                self.height = self.initial_height if self.text == "" else self.height
                
            on_text:
                root.text = self.text
                root.dispatch("on_text")
                
            on_text_validate:
                root.dispatch("on_text_validate")
                
            on_focus:
                root.dispatch("on_focus", args[0], args[1])
                
            on_triple_tap:
                root.dispatch("on_triple_tap")
                
            on_double_tap:
                root.dispatch("on_double_tap")
                
            on_quad_touch:
                root.dispatch("on_quad_touch")
            
            on_cursor_blink:
                root.dispatch("on_cursor_blink")
                
            on_cursor:
                root.dispatch("on_cursor")
                
            on_size:
                root.dispatch("on_size")
                
            on_handle_image_middle:
                root.dispatch("on_handle_image_middle")
                
            on_handle_image_left:
                root.dispatch("on_handle_image_left")
            
            on_handle_image_right:
                root.dispatch("on_handle_image_right")      
# kv_end
"""
)

class EmojiTextInput(TextInput):
    def insert_text(self, substring, from_undo=True):
        super().insert_text(substring, from_undo=True)

class M_CardTextField(MDBoxLayout, CommonElevationBehavior, ThemableBehavior):
    """
    This is a card text field that looks more like
    google website search textfield, you can use right_icon
    and left_icon with this widget and also add callback function to it

    read `Kivy TextInput doc` to understand more
    """

    elevation = NumericProperty(0)

    radius = VariableListProperty([10], length=4)

    text_field_disabled = BooleanProperty(False)

    card_ripples = BooleanProperty(False)

    focus = BooleanProperty(False)

    input_type = StringProperty("text")

    hint_text_color = ColorProperty([0.5, 0.5, 0.5, 1.0])

    multiline = BooleanProperty(True)

    hint_text = StringProperty("")

    text = StringProperty("")

    card_padding = dp(5)

    card_spacing = NumericProperty(0)

    grow_card = BooleanProperty(True)

    background_disabled_normal = StringProperty("")

    text_field_background_normal = StringProperty("")

    text_field_background_active = StringProperty("")

    text_field_max_height = NumericProperty(dp(110))

    text_field_size_hint_y = NumericProperty(None, allownone=True)

    text_field_height = NumericProperty(None, allownone=True)

    cursor_color = ListProperty([1, 0, 0, 0.8])

    foreground_color = ListProperty([0, 0, 0, 0.8])

    disabled_foreground_color = ColorProperty([0, 0, 0, .5])

    input_filter = ObjectProperty(None, allownone=True)

    background_color = ColorProperty([1, 1, 1, 1])

    line_spacing = NumericProperty(0)

    allow_copy = BooleanProperty(True)

    replace_crlf = BooleanProperty(True)

    auto_indent = BooleanProperty(False)

    handle_image_middle = StringProperty(
        'atlas://data/images/defaulttheme/selector_middle')

    handle_image_left = StringProperty(
        'atlas://data/images/defaulttheme/selector_left')

    handle_image_right = StringProperty(
        'atlas://data/images/defaulttheme/selector_right')

    write_tab = BooleanProperty(True)

    base_direction = OptionProperty(None,
                                    options=['ltr', 'rtl',
                                             'weak_rtl', 'weak_ltr', None],
                                    allownone=True)

    font_family = StringProperty(None, allownone=True)

    font_context = StringProperty(None, allownone=True)

    font_size = NumericProperty('15sp')

    font_name = StringProperty(DEFAULT_FONT)

    selection_text = StringProperty(u'')

    readonly = BooleanProperty(False)

    text_validate_unfocus = BooleanProperty(True)

    password = BooleanProperty(False)

    password_mask = StringProperty('*')

    keyboard_suggestions = BooleanProperty(False)

    cursor_blink = BooleanProperty(True)

    cursor_width = NumericProperty('1sp')

    line_height = NumericProperty(1)

    tab_width = NumericProperty(4)

    text_field_padding = VariableListProperty([6, 6, 6, 6])

    halign = OptionProperty('auto', options=['left', 'center', 'right',
                                             'auto'])

    scroll_x = NumericProperty(0)

    scroll_y = NumericProperty(0)

    selection_color = ColorProperty([0.1843, 0.6549, 0.8313, .5])

    border = ListProperty([4, 4, 4, 4])

    use_bubble = BooleanProperty(not _is_desktop)

    use_handles = BooleanProperty(not _is_desktop)

    suggestion_text = StringProperty('')

    """
    Do Not Use `extra_icons` on a `py` code use on `kv` code
    `extra_icons` is a work in progress for py code
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
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

if __name__ == "__main__":
    from kivymd.app import MDApp
    from kivy.uix.scrollview import ScrollView


    class Opera(MDApp):
        use_kivy_settings = False

        # kv_file = "main.kv"

        def build(self):
            root = MDBoxLayout(orientation='vertical', padding=dp(
                20), md_bg_color=[0, 0, 0, .15], spacing=dp(20))
            scroll = ScrollView()
            field = M_CardTextField(hint_text="text field with icon & can't grow", multiline=False, radius=20)
            field2 = M_CardTextField(
                hint_text="text field with no icon & can grow", grow_card=True, elevation=0)

            field3 = M_CardTextField(hint_text="text field with right icon & can't grow", grow_card=False)
            field4 = M_CardTextField(hint_text="text field with left icon & can't grow", grow_card=False)
            root.add_widget(field)
            root.add_widget(field2)
            root.add_widget(field3)
            root.add_widget(field4)
            root.add_widget(scroll)
            return root

        def search(self, instance):
            pass

        def login(self, instance):
            pass


    Opera().run()