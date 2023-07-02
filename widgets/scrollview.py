from kivymd.uix.scrollview import ScrollView
from threading import Thread
import time

class CustomScrollView(ScrollView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.timer_started = False        

    def on_scroll_start(self, touch, check_children=True):
        #Restart timer
        self.start_time = time.time()

        if not self.timer_started:
            self.parent.hide_buttons()

            t = Thread(target=self.start_timer)
            t.start()

            self.timer_started = True

        return super().on_scroll_start(touch, check_children)
    
    def start_timer(self, duration=1):
        while time.time() - self.start_time < duration:
            pass
        
        self.parent.unhide_buttons()
        self.timer_started = False
