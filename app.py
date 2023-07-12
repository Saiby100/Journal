from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from pages.login import Login
from pages.home import Home
from pages.journal import Journal
from kivy.core.window import Window
from utils.theme import Theme
from utils import config

Window.minimum_width, Window.minimum_height = (890, 500)
Window.size = (890, 500)

class JournalApp(MDApp):

    def build(self):
        global screen_manager

        config.init()
        Theme("relaxing")

        return config.sm
    
    def on_start(self):
        # config.sm.add_widget(Login(name="login_page"))
        # config.sm.add_widget(Home(name="home_page"))
        config.sm.add_widget(Journal(name="journal_page"))

        # config.sm.current = "login_page"

if __name__ == "__main__":
    JournalApp().run()

