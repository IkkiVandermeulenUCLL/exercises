# enter your code here to solve the housing assignment
# voer hier je code in om de huisvestingsvraag op te lossen
import re
from abc import ABC

class Person:
    def __init__(self, id, name , is_a_student):
        self.id = id
        self.name = name
        self.is_a_student = is_a_student

    @staticmethod
    def is_valid_name(name):
        return re.fullmatch('\w+( \w+)+', name)

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if( not self.is_valid_name(name)):
            raise ValueError()
        self.__name = name





class Residence(ABC):
    def __init__(self, address, area, number_of_rooms):
        self.address = address
        self.area = area
        self.number_of_rooms = number_of_rooms
        self.__occupants = {}

    @property
    def number_of_occupants(self):
        return len(self.__occupants)

    @property
    def maximum_occupants(self):
        return min(self.area//20, self.number_of_rooms*2)
    
    @property
    def resident_names(self):
        return [person.name for person in self.__occupants.values()]

    def register_resident(self, person):
        for id, _ in self.__occupants:
            if(person.id == id):
                raise RuntimeError()
        self.__occupants[person.id] = person

    def unregister_resident(self, id):
        del self.__occupants[id]
    
    @staticmethod
    def calculate_value(self):
        pass

class Villa(Residence):
    def __init__(self, address, area, number_of_rooms, garage_capacity):
        super().__init__(address, area, number_of_rooms)
        self.garage_capacity = garage_capacity

    def calculate_value(self):
        return (2500* self.number_of_rooms) + (2100 * self.area) + (10000 * self.garage_capacity)

class StudentKot(Residence):
    def __init__(self, address, area):
        super().__init__(address, area, 1)
    
    def register_resident(self, person):
        if(not person.is_a_student):
           raise RuntimeError()
        return super().register_resident(person)
    
    def calculate_value(self):
        return 150000 + (750*self.area)