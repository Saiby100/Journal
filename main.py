from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.label import Label
from kivy.clock import Clock
from functools import partial

class NotesApp(App):
    def build(self):
        global screen_manager
        screen_manager = ScreenManager(transition=FadeTransition())
        screen_manager.add_widget(Home())



        return screen_manager

class Home(Screen):
    def build(self):
        pass




if __name__ == '__main__':

    NotesApp().run()