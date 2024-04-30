class Cycle:
    def __init__(self, value):
        self.value = list(value)
        self.index = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.index = (self.index+1) % len(self.value)
        return self.value[self.index]