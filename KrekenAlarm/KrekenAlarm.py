
#!/usr/bin/env python3
import time
from Hoover import Hoover
from Observe import Observer

class StockMarket(Observer):
    def __init__(self, pair):
        self.pair = pair

    def update(self, *args, **kwargs):
        print("stock market received: {0}\n{1}".format(args, kwargs))
        return

eurxbt = StockMarket("XBXTZEUR")

hoover = Hoover()
hoover.register(eurxbt)
hoover.start()

print("thread start")
time.sleep(10)
hoover.stop()
print("thread stopping")
hoover.join()
print("stopped")




