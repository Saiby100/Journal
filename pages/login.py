from kivy.uix.screenmanager import Screen
from kivy.animation import Animation
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.textfield import MDTextField
from functools import partial
from kivymd.uix.button import MDIconButton
from utils import config
from widgets.textfield import TextField


class DetailsLayout(MDRelativeLayout):
    login_expanded = False
    signup_expanded = False
    username_field = None
    password_field = None
    confirm_password_field = None
    fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.username_field = TextField(
            hint_text="Username",
            pos_hint={"center_x": .5, "top": .8},
            opacity=0)

        self.password_field = TextField(
            hint_text="Password",
            pos_hint={"center_x": .5, "top": .68},
            password=True,
            opacity=0)

        self.confirm_password_field = TextField(
            hint_text="Confirm Password",
            pos_hint={"center_x": .5, "top": .55},
            password=True,
            opacity=0)
    
    def expand_login_details(self, btn_fade, btn_slide):
        if self.signup_expanded or self.login_expanded:
            return

        self.login_expanded = True
        self.btn_fade = btn_fade
        self.btn_drop = btn_slide
        self.back_btn_layout = self._get_page().ids.back_btn_layout

        new_pos_hint_y = 0.55
        function = partial(self._slide,
                           [self.btn_drop], 
                           new_pos_hint_y, 
                           self._on_expand_complete)

        self._fade([self.btn_fade], 0, function)
    
    def expand_signup_details(self, btn_fade, btn_slide):
        if self.signup_expanded or self.login_expanded:
            return

        self.signup_expanded = True
        self.btn_fade = btn_fade
        self.btn_drop = btn_slide
        self.back_btn_layout = self._get_page().ids.back_btn_layout

        new_pos_hint_y = 0.42
        function = partial(self._slide, 
                           [self.btn_drop], 
                           new_pos_hint_y, 
                           self._on_expand_complete)

        self._fade([self.btn_fade], 0, function)
    
    def _fade(self, widgets, new_opacity, function, *args):
        fade_anim = Animation(opacity=new_opacity, duration=.2)
        if function is not None:
            fade_anim.bind(on_complete=function)

        for widget in widgets:
            fade_anim.start(widget)
    
    def _slide(self, widgets, new_pos_hint, function, *args):
        slide_anim = Animation(pos_hint={"top": new_pos_hint}, duration=.2)
        if function is not None:
            slide_anim.bind(on_complete=function)

        for widget in widgets:
            slide_anim.start(widget)
    
    def _on_expand_complete(self, *args):
        self._slide([self.btn_fade], 1.25, None)
        self._add_text_fields()
        self.back_btn = MDIconButton(icon="chevron-left",
                                     icon_size=30,
                                     theme_icon_color="Custom",
                                     icon_color=(1, 1, 1, 1),
                                     opacity=0)

        self.back_btn.bind(on_release=self._collapse_details)

        self.back_btn_layout.add_widget(self.back_btn)
        self._fade([self.back_btn], 1, None)

        self._update_gif("curious")
    
    def _on_collapse_complete(self, fade_btn, *args):
        self._fade([self.btn_fade], 1, None)
        self._fade([self.back_btn], 0, lambda *x: self.remove_widget(self.back_btn))
        self._clear_text_fields()

        self._update_gif("normal")

        for field in self.fields:
            self.remove_widget(field)

    def _add_text_fields(self):
        if len(self.fields) == 0:
            self.fields.append(self.username_field)
            self.fields.append(self.password_field)

        if self.signup_expanded and len(self.fields) < 3:
            self.fields.append(self.confirm_password_field)
        
        elif self.login_expanded and len(self.fields) == 3:
            self.fields.remove(self.confirm_password_field)

        for field in self.fields:
            self.add_widget(field)
         
        self._fade(self.fields, 1, None)

    def _collapse_details(self, *args):

        if self.login_expanded:
            function = partial(self._slide, 
                               [self.btn_drop], 
                               .8, 
                               self._on_collapse_complete)
            self.login_expanded = False
            self.btn_fade.pos_hint = {"center_x": .5, "top": .65}
            self._fade(self.fields[:2], 0, function)
        
        else:
            function = partial(self._slide, 
                               [self.btn_drop], 
                               .65, 
                               self._on_collapse_complete)
            self.signup_expanded = False
            self.btn_fade.pos_hint = {"center_x": .5, "top": .8}
            self._fade(self.fields, 0, function)
    
    def go_back(self):
        #TODO: set back button to disable after pushing it
        self._collapse_details()
    
    def _clear_text_fields(self):
        for field in self.fields:
            field.clear_text()
    
    def _get_page(self):
        return self.parent.parent
    
    def _update_gif(self, gif):
        if gif == "normal":
            function = partial(self._fade, 
                               [self._get_page().ids.gif_normal],
                               1,
                               None)
            self._fade([self._get_page().ids.gif_curious], 
                       0,
                       function)
        else: 
            function = partial(self._fade, 
                               [self._get_page().ids.gif_curious],
                               1,
                               None)
            self._fade([self._get_page().ids.gif_normal], 
                       0,
                       function)

    def is_expanded(self):
        return self.login_expanded or self.signup_expanded

class Login(Screen):

    def login_pressed(self, *args):
        login_btn = self.ids.login_btn
        signup_btn = self.ids.signup_btn
        details_layout = self.ids.details_layout

        if not details_layout.is_expanded():
            details_layout.expand_login_details(signup_btn, login_btn)
        
        else: 
            #TODO: Verify login credentials here
            config.sm.current = "journal_page"
            
    def signup_pressed(self, *args):
        login_btn = self.ids.login_btn
        signup_btn = self.ids.signup_btn
        details_layout = self.ids.details_layout

        if not details_layout.is_expanded():
            details_layout.expand_signup_details(login_btn, signup_btn)
        
        else: 
            #TODO: Verify login credentials here
            config.sm.current = "journal_page"
    