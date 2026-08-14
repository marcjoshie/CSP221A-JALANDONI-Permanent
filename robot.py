from abc import ABC, abstractmethod

class Robot(ABC):
    manufacturer = "RoboTech"
    population = 0

    def __init__(self, name, battery=100):
        self.name = name
        self.battery = battery
        Robot.population += 1

    @property
    def battery(self):
        return self._battery

    @battery.setter
    def battery(self, value):
        if value < 0:
            self._battery = 0
        elif value > 100:
            self._battery = 100
        else:
            self._battery = value

    def __str__(self):
        return f"{self.name} ({self.battery}% battery)"

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', battery={self.battery})"

    @abstractmethod
    def perform_task(self):
        pass



class CleaningRobot(Robot):

    def __init__(self, name, battery=100, dust_capacity=10):
        super().__init__(name, battery)
        self.dust_capacity = dust_capacity

    def perform_task(self):
        return f"{self.name} is cleaning the floor."

