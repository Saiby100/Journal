from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from pages.home import Home
from pages.journal import Journal
from kivy.core.window import Window
from kivymd.uix.button import MDFlatButton
from utils.theme import Theme

Window.minimum_width, Window.minimum_height = (850, 500)
Window.size = (850, 500)

class JournalApp(MDApp):

    def build(self):
        global screen_manager

        Theme("relaxing")

        screen_manager = ScreenManager(transition=FadeTransition())
        screen_manager.add_widget(Home(name="home_page"))
        screen_manager.add_widget(Journal(name="journal_page"))


        return screen_manager

if __name__ == "__main__":
    JournalApp().run()

