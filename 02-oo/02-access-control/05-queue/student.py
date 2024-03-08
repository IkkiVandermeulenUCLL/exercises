class Queue:
    def __init__(self):
        self.items= []
    
    def add(self, naam):
        self.items.append(naam)

    def next(self):
        return 