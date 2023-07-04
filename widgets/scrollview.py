from kivymd.uix.scrollview import ScrollView
from multiprocessing import Process, Queue
from threading import Thread

class CustomScrollView(ScrollView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.timer_started = False
        self.queue = Queue()

    def on_scroll_start(self, touch, check_children=True):
        super().on_scroll_start(touch, check_children)

        # Restart timer
        if not self.timer_started:
            self.parent.hide_buttons()

            self.proc = Process(target=self.start_time, args=(self.queue,))
            self.proc.start()

            Thread(target=self.on_proc_termination).start()

            self.timer_started = True

        else:
            self.queue.put(1)

    def start_time(self, queue, duration=.7):
        while True:
            try:
                queue.get(timeout=duration)
            
            except Exception:
                break
                
    def on_proc_termination(self):
        self.proc.join()

        self.parent.unhide_buttons()
        self.timer_started = False
        
