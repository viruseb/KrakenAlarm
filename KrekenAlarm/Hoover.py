from threading import Thread

class Hoover(Thread):
    """Download OHLC at continuous interval"""

    def __init__(self, listpair = {}, savedir = {}, saveperiod = 43200):
        Thread.__init__(self)
        self.savedir = savedir
        self.saveperiod = saveperiod
        self.listpair = listpair       
     
    def run(self):
        return


