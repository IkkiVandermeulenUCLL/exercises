class CircularBuffer:
    def __init__(self,n):
        self.__buffer=[]
        self.__size = n

    def __len__(self):
        return len(self.__buffer)
    
    def add(self, item):
        if len(self) == self.__size:
            self.__buffer.pop(0)
        self.__buffer.append(item)

    def __getitem__(self, index):
        return self.__buffer[index]