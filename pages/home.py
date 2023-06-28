from kivy.uix.screenmanager import Screen
from kivy.animation import Animation
from kivymd.uix.relativelayout import MDRelativeLayout
from widgets.buttons import TextButton
from kivymd.uix.textfield import MDTextField
from functools import partial
from kivy.properties import BooleanProperty
from kivymd.uix.button import MDIconButton


class Details(MDRelativeLayout):
    login_expanded = BooleanProperty(False)
    signup_expanded = BooleanProperty(False)
    
    def expand_login_details(self):
        if self.signup_expanded or self.login_expanded:
            return
        self._expand_login_details()

    
    def expand_signup_details(self):
        if self.signup_expanded or self.login_expanded:
            return
        
        self._expand_signup_details()
    
    def _expand_login_details(self):
        self.login_expanded = True
        self.btn_fade = self.children[0]
        self.btn_drop = self.children[1]
        self.new_pos_hint_y = 0.55

        self._fade_btn()
    
    def _expand_signup_details(self):
        self.signup_expanded = True
        self.btn_fade = self.children[1]
        self.btn_drop = self.children[0]
        self.new_pos_hint_y = 0.45

        self._fade_btn()
    
    def _fade_btn(self):
        fade_anim = Animation(opacity=0, duration=.2)
        fade_anim.bind(on_complete=self._drop_btn)

        fade_anim.start(self.btn_fade)
    
    def _drop_btn(self, *args):
        drop_anim = Animation(pos_hint={"top": self.new_pos_hint_y}, duration=.2)
        drop_anim.bind(on_complete=partial(self._on_animation_complete, True))
        
        drop_anim.start(self.btn_drop)
    
    '''
        Executed when expansion/collapse animation completes.
    '''
    def _on_animation_complete(self, expand=True, *args):
        if expand:
            self.remove_widget(self.btn_fade)
            self._add_text_fields()
            self.back_btn = MDIconButton(icon="chevron-left",
                                         icon_size=30,
                                         theme_icon_color="Custom",
                                         icon_color=(1, 1, 1, 1),
                                         opacity=0)

            self.children[3].add_widget(self.back_btn)
            Animation(opacity=1, duration=.3).start(self.back_btn)

        else: #Collapse details
            self.remove_widget(self.username_field)
            self.remove_widget(self.password_field)

            if self.signup_expanded:
                self.remove_widget(self.confirm_password_field)

    def _remove_text_fields(self):
        self.remove_widget(self.username_field)
        self.remove_widget(self.password_field)

        if self.signup_expanded:
            self.remove_widget(self.confirm_password_field)
        

    def _add_text_fields(self):
        fields = []
        self.username_field = MDTextField(
            hint_text="Username",
            pos_hint={"center_x": .5, "top": .8},
            opacity=0)

        self.password_field = MDTextField(
            hint_text="Password",
            pos_hint={"center_x": .5, "top": .7},
            password=True,
            opacity=0)
        
        fields.append(self.username_field)
        fields.append(self.password_field)

        if self.signup_expanded:
            self.confirm_password_field = MDTextField(
                hint_text="Confirm Password",
                pos_hint={"center_x": .5, "top": .6},
                password=True,
                opacity=0)

            fields.append(self.confirm_password_field)
        
        fade_in = Animation(opacity=1, duration=.3)

        for field in fields:
            self.add_widget(field)
            fade_in.start(field)

    def _collapse_details(self):
        pass

    def _raise_btn(self):
        new_y = .8
        raise_anim = Animation(pos_hint={'top':new_y}, duration=.3)
        raise_anim.bind(on_complete=lambda *x: self.add_widget(TextButton()))
        raise_anim.start(self.children[1])
    
    def go_back(self):
        self._collapse_details()

class Home(Screen):

    def login_pressed(self):
        self.ids.details_layout.expand_login_details()
            
    def signup_pressed(self):
        self.ids.details_layout.expand_signup_details()
    