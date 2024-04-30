class InclusiveRange:
    def __init__(self, min, max):
        self.min = min
        self.max = max
        self.current = min

    def __iter__(self):
        return InclusiveRangeIterator(self.min, self.max)

class InclusiveRangeIterator:
    def __init__(self, min, max):
        self.min = min
        self.max = max
        self.current = min

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current<= self.max:
            result = self.current
            self.current+=1
            return result
        else:
            raise StopIteration("L bozo")