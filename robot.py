from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.INFO)

class InsufficientBatteryError(Exception):

    def __init__(self, robot_name, required, available):
        self.robot_name = robot_name
        self.required = required
        self.available = available

        message = (
            f"{robot_name} needs {required}% battery for this task "
            f"but only has {available}%."
        )

        super().__init__(message)

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

    def use_battery(self, amount):
        if self.battery < amount:
            raise InsufficientBatteryError(
                self.name,
                amount,
                self.battery
            )
        self.battery -= amount

    @abstractmethod
    def perform_task(self):
        pass



class CleaningRobot(Robot):

    def __init__(self, name, battery=100, dust_capacity=10):
        super().__init__(name, battery)
        self.dust_capacity = dust_capacity

    def perform_task(self):
        self.use_battery(10)
        return f"{self.name} is cleaning the floor."

class DroneRobot(Robot):

    def __init__(self, name, battery=5, max_altitude=120):
        super().__init__(name, battery)
        self.max_altitude = max_altitude

    def perform_task(self):
        self.use_battery(20)
        return f"{self.name} is flying and surveying the area."


def run_task_safely(robot, **kwargs):
    try:
        result = robot.perform_task(**kwargs)

    except InsufficientBatteryError as error:
        logging.error(error)

    else:
        print(result)

    finally:
        print(f"{robot.name} now has {robot.battery}% battery.")