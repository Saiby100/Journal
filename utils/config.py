from kivy.uix.screenmanager import ScreenManager, FadeTransition

def init():
    global sm
    sm = ScreenManager(transition=FadeTransition())
    

