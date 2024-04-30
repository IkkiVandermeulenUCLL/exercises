class PadZip:
    def __init__(self, t1, t2, padding=None):
        self.t1 = iter(t1)
        self.t2 = iter(t2)
        self.padding = padding
    
    def __iter__(self):
        return self

    def __next__(self):
        end_reached = 0

        try:
            tp1 = next(self.t1)
        except StopIteration:
            tp1 = self.padding
            end_reached += 1

        try:
            tp2 = next(self.t2)
        except StopIteration:
            tp2 = self.padding
            end_reached += 1

        if (end_reached==2):
            raise StopIteration
        return (tp1, tp2)