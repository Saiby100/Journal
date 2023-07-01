from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from pages.login import Login
from pages.journal import Journal
from kivy.core.window import Window
from utils.theme import Theme

Window.minimum_width, Window.minimum_height = (850, 500)
Window.size = (850, 500)

class JournalApp(MDApp):

    def build(self):
        global screen_manager

        Theme("relaxing")

        screen_manager = ScreenManager(transition=FadeTransition())
        screen_manager.add_widget(Login(name="login_page"))
        screen_manager.add_widget(Journal(name="journal_page"))

        return screen_manager

if __name__ == "__main__":
    JournalApp().run()

