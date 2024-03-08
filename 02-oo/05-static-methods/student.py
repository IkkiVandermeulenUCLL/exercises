class Duration:
    def __init__(self, duration):
        self.__duration= duration

    @property
    def seconds(self):
        return self.__duration
    
    @property
    def minutes(self):
        return self.__duration/60
    
    @property
    def hours(self):
        return self.__duration/3600
    
    @staticmethod
    def from_seconds(seconds):
        return Duration(seconds)
    
    @staticmethod
    def from_minutes(minutes):
        return Duration(minutes*60)
    
    @staticmethod
    def from_hours(hours):
        return Duration(hours*3600)
