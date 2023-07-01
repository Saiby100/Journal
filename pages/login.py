from kivy.uix.screenmanager import Screen
from kivy.animation import Animation
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.textfield import MDTextField
from functools import partial
from kivymd.uix.button import MDIconButton


class DetailsLayout(MDRelativeLayout):
    login_expanded = False
    signup_expanded = False
    username_field = None
    password_field = None
    confirm_password_field = None
    fields = []
    
    def expand_login_details(self, btn_fade, btn_slide):
        if self.signup_expanded or self.login_expanded:
            return

        self.login_expanded = True
        self.btn_fade = btn_fade
        self.btn_drop = btn_slide
        self.back_btn_layout = self.children[2]

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
        self.back_btn_layout = self.children[2]

        new_pos_hint_y = 0.45
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
    
    def _on_collapse_complete(self, fade_btn, *args):
        self._fade([self.btn_fade], 1, None)
        self._fade([self.back_btn], 0, lambda *x: self.remove_widget(self.back_btn))
        self._clear_text_fields()

        for field in self.fields:
            self.remove_widget(field)

    def _add_text_fields(self):
        if self.username_field is None:
            self.username_field = MDTextField(
                hint_text="Username",
                pos_hint={"center_x": .5, "top": .8},
                opacity=0)

            self.password_field = MDTextField(
                hint_text="Password",
                pos_hint={"center_x": .5, "top": .7},
                password=True,
                opacity=0)

            self.confirm_password_field = MDTextField(
                hint_text="Confirm Password",
                pos_hint={"center_x": .5, "top": .6},
                password=True,
                opacity=0)

            self.fields.append(self.username_field)
            self.fields.append(self.password_field)

            if self.signup_expanded:
                self.fields.append(self.confirm_password_field)

        elif self.signup_expanded and len(self.fields) < 3:
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
            field.text = ""

class Login(Screen):

    def login_pressed(self, *args):
        login_btn = self.ids.login_btn
        signup_btn = self.ids.signup_btn
        self.ids.details_layout.expand_login_details(signup_btn, login_btn)
            
    def signup_pressed(self, *args):
        login_btn = self.ids.login_btn
        signup_btn = self.ids.signup_btn
        self.ids.details_layout.expand_signup_details(login_btn, signup_btn)
    