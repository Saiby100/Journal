from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from login_functions import *
from kivy.clock import Clock
from functools import partial

class NotesApp(App):
    def build(self):
        global screen_manager
        screen_manager = ScreenManager(transition=FadeTransition())

        screen_manager.add_widget(Home('home_page'))
        screen_manager.add_widget(SignUp('signup_page'))
        screen_manager.add_widget(Login('login_page'))
        screen_manager.add_widget(Notes('notes_page'))

        return screen_manager

class Home(Screen):
    def __init__(self, page_name):
        super().__init__(name=page_name)
        #Initializing Layouts
        box_layout = BoxLayout(orientation='vertical', spacing=20, padding=20)

        #WIDGETS:
        #Labels
        option_label = Label(text='Choose an option: ',
                             font_size=30,
                             size_hint=(1, 0.7),
                             color=(0, 1, .4, 1)
                            )

        #Buttons
        login_btn = Button(text='Log in',
                           size_hint=(1, 0.3),
                           font_size=20,
                           background_color=(0, .77, .77, .3),
                           color=(0, 1, .4, 1)
                           )
        login_btn.bind(on_release=self.login)

        reg_btn = Button(text='Register',
                         size_hint=(1, 0.3),
                         font_size=20,
                         background_color=(0, .77, .77, .3),
                         color=(0, 1, .4, 1)
                        )
        reg_btn.bind(on_release=self.register)

        box_layout.add_widget(option_label)
        box_layout.add_widget(login_btn)
        box_layout.add_widget(reg_btn)

        self.add_widget(box_layout)

    def register(self, event):
        screen_manager.current = 'signup_page'

    def login(self, event):
        screen_manager.current = 'login_page'


class SignUp(Screen):
    def __init__(self, page_name):
        super().__init__(name=page_name)

        #Initializing layouts
        self.box_layout = BoxLayout(orientation='vertical', spacing=30, padding=30)
        self.box_layout.size_hint = (1, .9)
        self.box_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        anchor_layout = AnchorLayout(anchor_x='left', anchor_y='top', padding=10)

        #WIDGETS:
        #Labels
        email_label = Label(text='Email: ',
                            font_size=20,
                            size_hint=(1, 0.01),
                            color=(0, 1, .4, 1)
                           )

        username_label = Label(text='Username:',
                               font_size=email_label.font_size,
                               size_hint=email_label.size_hint,
                               color=email_label.color
                               )

        password_label = Label(text='Password:',
                               font_size=email_label.font_size,
                               size_hint=email_label.size_hint,
                               color=email_label.color
                               )

        conf_password_label = Label(text='Confirm Password:',
                                    font_size=email_label.font_size,
                                    size_hint=email_label.size_hint,
                                    color=email_label.color
                                    )

        #Text boxes
        self.email_box = TextInput(multiline=False,
                                   size_hint=(.75, None),
                                   height=40,
                                   font_size=20,
                                   pos_hint={'center_x': .5}
                                 )

        self.username_box = TextInput(multiline=False,
                                 size_hint=self.email_box.size_hint,
                                 height=self.email_box.height,
                                 font_size=self.email_box.font_size,
                                 pos_hint = {'center_x': .5}
                                 )

        self.password_box = TextInput(multiline=False,
                                 password=True,
                                 font_size=self.email_box.font_size,
                                 size_hint=self.email_box.size_hint,
                                 height=self.email_box.height,
                                 pos_hint={'center_x': .5}
                                 )

        self.conf_password_box = TextInput(multiline=False,
                                           password=True,
                                           font_size=self.email_box.font_size,
                                           size_hint=self.email_box.size_hint,
                                           height=self.email_box.height,
                                           pos_hint={'center_x': .5}
                                         )
        #Buttons
        reg_btn = Button(text='Register',
                         font_size=20,
                         size_hint=(.3, .1),
                         pos_hint={'center_x': .5},
                         background_color=(0, .77, .77, .3),
                         color=email_label.color
                         )
        reg_btn.bind(on_release=self.register)

        back_btn = Button(text='Back',
                          font_size=15,
                          size_hint=(.1, .1),
                          background_color=(0, .77, .77, .3),
                          color=email_label.color
                         )
        back_btn.bind(on_release=self.go_back)

        #Adding widgets to the layout
        self.box_layout.add_widget(email_label)
        self.box_layout.add_widget(self.email_box)
        self.box_layout.add_widget(username_label)
        self.box_layout.add_widget(self.username_box)
        self.box_layout.add_widget(password_label)
        self.box_layout.add_widget(self.password_box)
        self.box_layout.add_widget(conf_password_label)
        self.box_layout.add_widget(self.conf_password_box)
        self.box_layout.add_widget(reg_btn)

        anchor_layout.add_widget(back_btn)

        #Adding layouts to the screen
        self.add_widget(self.box_layout)
        self.add_widget(anchor_layout)

    def go_back(self, event):
        screen_manager.current = 'home_page'
        self.clear_text()

    def remove(self, widget, *largs):
        self.remove_widget(widget)

    def register(self, event):
        err_msg = check_cred(self.email_box.text, self.username_box.text, self.password_box.text, self.conf_password_box.text)
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='bottom')

        label = Label(text=err_msg,
                      size_hint=(1, .1),
                      font_size=15,
                      color=(0, 1, .4, 1)
                      )

        anchor_layout.add_widget(label)
        self.add_widget(anchor_layout)

        Clock.schedule_once(partial(self.remove, anchor_layout), 2)

        if err_msg == 'Successfully Registered!':
            create_account(self.email_box.text, self.username_box.text, self.password_box.text)
            screen_manager.current = 'login_page'
            self.clear_text()

    def clear_text(self):
        self.email_box.text = ''
        self.username_box.text = ''
        self.password_box.text = ''
        self.conf_password_box.text = ''


class Login(Screen):
    def __init__(self, page_name):
        super().__init__(name=page_name)
        #Initializing layouts
        box_layout = BoxLayout(orientation='vertical', spacing=30, padding=30)
        box_layout.size_hint = (1, .5)
        box_layout.pos_hint = {'center_x': .5, 'center_y': .6}

        anchor_layout = AnchorLayout(anchor_x='left', anchor_y='top', padding=10)

        #WIDGETS:
        #Labels
        username_label = Label(text='Username: ',
                               font_size=20,
                               size_hint=(1, 0.01),
                               color=(0, 1, .4, 1)
                               )

        password_label = Label(text='Password:',
                               font_size=20,
                               size_hint=(1, 0.01),
                               color=(0, 1, .4, 1)
                               )

        #Text boxes
        self.username_box = TextInput(multiline=False,
                               size_hint=(.75, None),
                               height=40,
                               font_size=20,
                               pos_hint={'center_x': .5}
                               )

        self.password_box = TextInput(multiline=False,
                                 password=True,
                                 size_hint=(.75, None),
                                 height=40,
                                 font_size=20,
                                 pos_hint={'center_x': .5}
                                 )

        #Buttons
        # view_btn = Button(text='(0)',
        #                   font_size=15,
        #                   size_hint=(.1, .1),
        #                   pos_hint={'center_x': self.password_box., 'center_y': self.password_box.center_y})

        log_btn = Button(text='Log in',
                         font_size=20,
                         size_hint=(.3, .5),
                         pos_hint={'center_x': .5},
                         background_color=(0, .77, .77, .3),
                         color=(0, 1, .4, 1)
                         )
        log_btn.bind(on_release=self.log_in)

        back_btn = Button(text='Back',
                          font_size=15,
                          size_hint=(.1, .1),
                          background_color=(0, .77, .77, .3),
                          color=(0, 1, .4, 1)
                          )
        back_btn.bind(on_release=self.go_back)

        #Adding widgets to layouts
        anchor_layout.add_widget(back_btn)
        box_layout.add_widget(username_label)
        box_layout.add_widget(self.username_box)
        box_layout.add_widget(password_label)
        box_layout.add_widget(self.password_box)
        box_layout.add_widget(log_btn)

        #Adding layouts to the window
        self.add_widget(anchor_layout)
        self.add_widget(box_layout)
        # self.add_widget(view_btn)

    def go_back(self, event):
        screen_manager.current = 'home_page'
        self.clear_text()

    def remove(self, widget, *largs):
        self.remove_widget(widget)

    def log_in(self, event):
        if login(self.username_box.text, self.password_box.text):
            screen_manager.current = 'notes_page'
            self.clear_text()

        else:
            anchor_layout = AnchorLayout(anchor_x='center', anchor_y='bottom')

            label = Label(text='Incorrect username or password',
                          size_hint=(1, .7),
                          font_size=15,
                          color=(0, 1, .4, 1)
                          )

            anchor_layout.add_widget(label)
            self.add_widget(anchor_layout)
            Clock.schedule_once(partial(self.remove, anchor_layout), 2)

    def clear_text(self):
        self.username_box.text = ''
        self.password_box.text = ''


class Notes(Screen):
    def __init__(self, page_name):
        super().__init__(name=page_name)
        #Initializing Layouts
        anchor_layout = AnchorLayout(anchor_x='left', anchor_y='top', padding=10)
        box_layout = BoxLayout(orientation='vertical')

        box_layout.add_widget(Label(text='This is the notes page', font_size=30))

        back_btn = Button(text='Back',
                          font_size=15,
                          size_hint=(.1, .1),
                          background_color=(0, .77, .77, .3),
                          color=(0, 1, .4, 1)
                          )
        back_btn.bind(on_release=self.go_back)

        anchor_layout.add_widget(back_btn)

        self.add_widget(anchor_layout)
        self.add_widget(box_layout)

    def go_back(self, event):
        screen_manager.current = 'login_page'

if __name__ == '__main__':
    NotesApp().run()