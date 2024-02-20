class AssocList:
    def __init__(self):
        self.__items = []

    def __setitem__(self, key, value):
        index = self.__findIndex(key)
        if index==-1:
            self.__items.append([key,value])
        else:
            self.__items[index][1] = value

    def __findIndex(self, key):
        for i in range(0,len(self.__items)):
            if self.__items[i][0]==key:
                return i
        return -1
    
    def __getitem__(self,key):
        index = self.__findIndex(key)
        if index !=-1:
            return self.__items[index][1]
        else:
            raise ValueError()
        
    def __contains__(self,key):
        return self.__findIndex(key)!=-1
    
    def __len__(self):
        return len(self.__items)
    
    @property
    def keys(self):
        return [k for k,_ in self.__items]
    
    @property
    def values(self):
        return [v for _,v in self.__items]