import threading
import time
from threading import Thread
from Observe import Observable

class Hoover(Thread, Observable):
    """Download OHLC at continuous interval"""

    def __init__(self):
        Observable.__init__(self)
        Thread.__init__(self)
        self._stop_event = threading.Event()        
  
    def stop(self):
        self._stop_event.set()

    def run(self):

        while not self._stop_event.is_set():
            time.sleep(1);
            for observer in self.observers:
                observer.update(observer.pair, 16.5);

        return


